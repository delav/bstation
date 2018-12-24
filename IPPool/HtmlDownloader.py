# coding:utf-8

import config
import requests
import chardet
from lxml import etree


def download(url):
    try:
        r = requests.get(url=url, headers=config.get_header(), timeout=config.TIMEOUT)
        r.encoding = chardet.detect(r.content)['encoding']
        if (not r.ok) or len(r.content) < 500:
            raise
        else:
            return r.text

    except Exception:
        count = 0  # 重试次数

        while count < config.RETRY_TIME:
            try:
                r = requests.get(url=url, headers=config.get_header(), timeout=config.TIMEOUT)
                r.encoding = chardet.detect(r.content)['encoding']
                if (not r.ok) or len(r.content) < 500:
                    raise
                else:
                    return r.text
            except Exception:
                count += 1
    return None


def parser(response, p_dict):
    proxylist = []
    root = etree.HTML(response)
    proxys = root.xpath(p_dict['pattern'])
    for proxy in proxys:
        try:
            ip = proxy.xpath(p_dict['position']['ip'])[0].text
            port = proxy.xpath(p_dict['position']['port'])[0].text
            protocol = proxy.xpath(p_dict['position']['protocol'])[0].text
        except Exception:
            continue
        proxy = {'ip': ip, 'port': int(port), 'protocol': protocol}
        proxylist.append(proxy)
    return proxylist
