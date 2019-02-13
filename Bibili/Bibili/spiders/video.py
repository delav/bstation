# -*- coding: utf-8 -*-
import scrapy
from Bibili.items import VideoItem
from scrapy import Request
from util import get_video_data
from scrapy_splash.request import SplashRequest
from scrapy.selector import Selector


class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://bilibili.com/']

    def parse(self, response):
        # 获取所有分类地址
        res_all = response.xpath('//*[@id="primary_menu"]/ul/li/a/@href').extract()
        res = res_all[1:2]
        for ctg in res:
            url = 'https:' + ctg
            yield Request(url, callback=self.parse_category, dont_filter=True)

    def parse_category(self, response):
        # 获取大分类下的小分类地址
        res_all = response.xpath('//div[@id="subnav"]/ul/li/a/@href').extract()
        if res_all is None:
            res = [response.url]
        else:
            res = res_all[1:]
        for mctg in res:
            url = 'https://www.bilibili.com' + mctg
            yield SplashRequest(url, callback=self.get_pages, args={'wait': '3'})

    def get_pages(self, response):
        # 获取每页链接
        page_li = response.xpath('//*[@id="videolist_box"]/div[2]/div[2]/ul/li/button/text()')
        if len(page_li) > 5:
            max_page = page_li[5].extract()
        else:
            max_page = page_li[-1].extract()
        for i in range(1, int(max_page)):
            page_url = "https://www.bilibili.com/v/ad/ad/#/all/default/0/{}".format(i)
            yield SplashRequest(page_url, callback=self.parse_list, args={'wait': '0.5'})

    def parse_list(self, response):
        # 获取视频地址
        site = Selector(response)
        video_urls = site.xpath('//*[@id="videolist_box"]/div[2]/ul/li/div/div[2]/a/@href').extract()
        for v_url in video_urls:
            r_url = 'https:' + v_url
            splash_args = {"lua_source": """
                            --splash.response_body_enabled = true
                            splash.private_mode_enabled = false
                            splash:set_user_agent("Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36")
                            assert(splash:go("%s"))
                            splash:wait(3)
                            return {html = splash:html()}
                            """ % r_url}
            yield SplashRequest(r_url, endpoint='run', callback=self.parse_product, args=splash_args)

    def parse_product(self, response):
        v_url = response.url
        video_aid = v_url.split('/')[-2][2:]
        title = response.xpath('//*[@id="viewbox_report"]/h1/span/text()')  # 标题
        types1 = response.xpath('//*[@id="viewbox_report"]/div[1]/span/a[1]/text()')
        types2 = response.xpath('//*[@id="viewbox_report"]/div[1]/span/a[2]/text()')
        public_time = response.xpath('//*[@id="viewbox_report"]/div[1]/time/text()')  # 发布时间
        author_name = response.xpath('//*[@id="v_upinfo"]/div[2]/div[1]/a[1]/text()')  # 作者
        author_url = response.xpath('//*[@id="v_upinfo"]/div[2]/div[1]/a[1]/@href')  # 作者地址
        # view = response.xpath('//*[@id="viewbox_report"]/div/span[@class="v play"]/@title')  # 播放
        # danmaku = response.xpath('//*[@id="viewbox_report"]/div/span[@class="v dm"]/@title')  # 弹幕
        # likes = site.xpath('//*[@id="arc_toolbar_report"]/div[1]/span[1]/text()')  # 点赞
        # coins = site.xpath('//*[@id="arc_toolbar_report"]/div/span[@report-id="coinbtn1"]/@title')  # 硬币
        # favorites = site.xpath('//*[@id="arc_toolbar_report"]/div/span[@report-id="collect1"]/@title')  # 收藏
        # shares = site.xpath('//*[@id="arc_toolbar_report"]/div/div[@class="s-text"]/@title')  # 分享
        # replies = site.xpath('//*[@id="comment"]/div/div[1]/span[1]/text()')  # 评论
        other_json = get_video_data(video_aid)
        it = VideoItem()
        it['vid'] = video_aid
        it['url'] = v_url
        it['title'] = title[0].extract()
        it['types'] = types1[0].extract() + '-' + types2[0].extract()
        it['public_time'] = public_time[0].extract()
        it['author_name'] = author_name[0].extract()
        it['author_url'] = author_url[0].extract()
        it['author_id'] = author_url[0].extract().split('/')[-1]
        it['view'] = other_json['view']
        it['danmaku'] = other_json['danmaku']
        it['reply'] = other_json['reply']
        it['favorite'] = other_json['favorite']
        it['coin'] = other_json['coin']
        it['share'] = other_json['share']
        it['like'] = other_json['like']
        yield it
