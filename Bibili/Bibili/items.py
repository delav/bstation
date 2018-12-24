# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    vid = scrapy.Field()  # 视频Id
    url = scrapy.Field()  # 地址
    title = scrapy.Field()  # 标题
    types = scrapy.Field()  # 类型
    public_time = scrapy.Field()  # 发布时间
    author_name = scrapy.Field()  # 作者昵称
    author_url = scrapy.Field()  # 作者空间地址
    author_id = scrapy.Field()  # 作者Id
    view = scrapy.Field()  # 播放
    danmaku = scrapy.Field()  # 弹幕
    reply = scrapy.Field()  # 评论
    favorite = scrapy.Field()  # 收藏
    coin = scrapy.Field()  # 硬币
    share = scrapy.Field()  # 分享
    like = scrapy.Field()  # 点赞


class AuthorItem(scrapy.Item):
    # define the fields for your item here like:
    aid = scrapy.Field()  # 作者Id
    a_url = scrapy.Field()  # 作者空间地址
    up_name = scrapy.Field()  # 作者昵称
    sex = scrapy.Field()  # 性别
    register_time = scrapy.Field()  # 注册时间
    following = scrapy.Field()  # 粉丝
    follower = scrapy.Field()  # 关注
    videos = scrapy.Field()  # 投稿
    album = scrapy.Field()  # 相簿
    views = scrapy.Field()  # 播放数
