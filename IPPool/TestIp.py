# coding: utf-8
import requests


def test_ip(ip, port):
    test_url = 'http://' + '%s:%s' % (ip, port)

    try:
        requests.get('http://wenshu.court.gov.cn/', proxies={"http": test_url})
    except:
        # print 'connect failed'
        return False
    else:
        # print 'success'
        return True