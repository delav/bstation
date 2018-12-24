# -*- coding: utf-8 -*-
import scrapy
from Bibili.items import AuthorItem
from util import get_author_data
from scrapy import Request
from scrapy_splash.request import SplashRequest
from scrapy.selector import Selector


class AuthorSpider(scrapy.Spider):
    name = 'author'
    allowed_domains = ['space.bilibili.com']
    end_aid = 50000

    def start_requests(self):
        for aid in xrange(1, self.end_aid):
            url_mod = 'https://space.bilibili.com/{}'
            url = url_mod.format(aid)
            yield SplashRequest(url, callback=self.space_info, args={'wait': '3', 'aid': aid}, dont_filter=True)

    def space_info(self, response):
        a_url = response.url
        aid = a_url.split('/')[-1]
        try:
            up_name = response.xpath('//*[@id="h-name"]/text()')[0].extract()
        except:
            up_name = '未知'
        try:
            register_time = response.xpath('//*[@id="page-index"]/div[2]/div[7]/div[2]/div/'
                                           'div/div[1]/div[2]/span[2]/text()')[0].extract().strip()
        except:
            register_time = '注册于 1949-01-01'
        try:
            sex = response.xpath('//*[@id="h-gender"]/@class')[0].extract().split()[2]
        except:
            sex = 'unknown'
        # follower = response.xpath('//*[@id="n-gz"]/text()')
        # following = response.xpath('//*[@id="n-fs"]/text()')
        # views = response.xpath('//*[@id="n-bf"]/text()')
        # album = response.xpath('//*[@id="page-index"]/div[1]/div[7]/h3/span/text()')
        it = AuthorItem()
        other_json = get_author_data(aid)
        it['aid'] = aid
        it['a_url'] = a_url
        it['up_name'] = up_name
        it['sex'] = sex
        it['register_time'] = register_time
        it['following'] = other_json['following']
        it['follower'] = other_json['follower']
        it['videos'] = other_json['video']
        it['album'] = other_json['album']
        it['views'] = other_json['archive']['view']
        yield it
