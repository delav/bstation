# coding:utf-8
from gevent import monkey
monkey.patch_all()

import sys
import time
import gevent
from gevent.pool import Pool
from multiprocessing import Queue, Process, Value
from config import THREADNUM, parserList, MAX_DOWNLOAD_CONCURRENT
from HtmlDownloader import download, parser
from DataStore import store_data
from TestIp import test_ip

'''
爬取代理IP/端口并存入数据库
'''


def start_proxy_crawl(queue, db_proxy_num):
    crawl = ProxyCrawl(queue, db_proxy_num)
    crawl.run()


class ProxyCrawl(object):

    def __init__(self, queue, db_proxy_num):
        self.crawl_pool = Pool(THREADNUM)
        self.queue = queue
        self.db_proxy_num = db_proxy_num

    def run(self):
        while True:
            strs = 'IPProxyPool----->>>>>>>>beginning'
            sys.stdout.write(strs + "\r\n")
            sys.stdout.flush()

            spawns = []
            for p in parserList:
                spawns.append(gevent.spawn(self.crawl, p))
                if len(spawns) >= MAX_DOWNLOAD_CONCURRENT:
                    gevent.joinall(spawns)
                    spawns = []
            gevent.joinall(spawns)

    def crawl(self, p_dict):
        for url in p_dict['urls']:
            print "url:", url
            response = download(url)
            print response
            if response is not None:
                proxylist = parser(response, p_dict)
                if proxylist is not None:
                    for proxy in proxylist:
                        ip = proxy['ip']
                        port = proxy['port']
                        proxy_str = '%s:%s' % (ip, port)
                        flag = test_ip(ip, port)
                        if flag == 'True':
                            print "proxy_str", proxy_str
                            if self.queue.full():
                                time.sleep(0.5)
                            else:
                                self.queue.put(proxy)
                                break


if __name__ == "__main__":
    DB_PROXY_NUM = Value('i', 0)
    q = Queue()
    p1 = Process(target=start_proxy_crawl, args=(q, DB_PROXY_NUM))
    p2 = Process(target=store_data, args=(q, DB_PROXY_NUM))
    p1.start()
    p2.start()

    # spider = ProxyCrawl()
    # spider.run()
