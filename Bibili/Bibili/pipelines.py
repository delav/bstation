# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import json
import codecs
import pymysql
from items import VideoItem, AuthorItem


# 保存为json文件
# class BibiliPipeline(object):
#
#     def __init__(self):
#         self.file1 = codecs.open('author.json', 'w+', encoding='utf-8')
#         # self.file2 = codecs.open('video.json', 'w+', encoding='utf-8')
#         self.file1.write('[')
#         # self.file2.write('[')
#
#     def process_item(self, item, spider):
#         if isinstance(item, VideoItem):
#             line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
#             self.file1.write(line)
#         # elif isinstance(item, AuthorItem):
#         #     line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
#         #     self.file2.write(line)
#         return item
#
#     def close_spider(self, spider):
#         self.file1.seek(-1, 2)  # 删除最后一行的逗号和换行符
#         # self.file2.seek(-1, 2)
#         self.file1.write(']')
#         # self.file2.write(']')
#         self.file1.close()
#         # self.file2.close()

# 保存为csv文件(windows打开中文是乱码)
# class BibiliPipeline(object):
#
#     video_col_name = ['vid', 'url', 'title', 'types', 'public_time', 'author_name', 'author_url', 'author_id',
#                       'view', 'danmaku', 'reply', 'favorite', 'coin', 'share', 'like']
#     author_col_name = ['aid', 'a_url', 'up_name', 'sex', 'register_time', 'following', 'follower', 'videos',
#                        'album', 'views']
#
#     def __init__(self):
#         self.file1 = codecs.open('video.csv', 'w+', encoding='utf-8')
#         self.file2 = codecs.open('author.csv', 'w+', encoding='utf-8')
#         # 启动csv的字典写入方法
#         self.writer1 = csv.DictWriter(self.file1, self.video_col_name)
#         self.writer2 = csv.DictWriter(self.file2, self.author_col_name)
#         # 写入字段名称作为首行
#         self.writer1.writeheader()
#         self.writer2.writeheader()
#
#     def process_item(self, item, spider):
#         if isinstance(item, VideoItem):
#             self.writer1.writerow(item)
#         elif isinstance(item, AuthorItem):
#             self.writer2.writerow(item)
#         return item
#
#     def close_spider(self, spider):
#         self.file1.close()
#         self.file2.close()

# 保存到数据库
class BibiliPipeline(object):

    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            db='bilibili',
            user='root',
            passwd='729814',
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        video_sql = 'insert into video_video(id,url,title,types,public_time,author_name,author_url,' \
                    'views,danmaku,reply,favorite,coin,share,likes)'
        author_sql = 'insert into author_author(id, a_url, up_name, sex, register_time, following,' \
                     'follower, videos, album, views)'
        if isinstance(item, VideoItem):
            self.cursor.execute(video_sql, (
                item['id'], item['url'], item['title'], item['types'], item['public_time'], item['author_name'],
                item['author_url'], item['views'], item['danmaku'], item['reply'], item['favorite'], item['coin'],
                item['share'], item['likes']))
            self.connect.commit()

        elif isinstance(item, AuthorItem):
            self.cursor.execute(author_sql, (
                item['id'], item['a_url'], item['up_name'], item['sex'], item['register_time'], item['following'],
                item['follower'], item['videos'], item['album'], item['views']))
            self.connect.commit()

    def close_spider(self, spider):
        self.connect.close()