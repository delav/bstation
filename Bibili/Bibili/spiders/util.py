# coding: utf-8
import requests
import warnings

warnings.filterwarnings("ignore")  # 忽略警告提示
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/49.0.2623.112 Safari/537.36'}
video_url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={}'
author_url = 'http://api.bilibili.com/x/relation/stat?vmid={}'
num_url = 'http://api.bilibili.com/x/space/navnum?mid={}'
view_url = 'http://api.bilibili.com/x/space/upstat?mid={}'


def get_video_data(aid):
    msg_dict = {}
    try:
        response = requests.get(video_url.format(aid), headers=headers, verify=False, timeout=10)
        if response.status_code == 200:
            msg_dict = response.json()['data']
    except Exception as e:
        print e
    return msg_dict


def get_author_data(aid):
    msg_dict = {}
    try:
        response1 = requests.get(author_url.format(aid), headers=headers, verify=False, timeout=10)
        response2 = requests.get(num_url.format(aid), headers=headers, verify=False, timeout=10)
        response3 = requests.get(view_url.format(aid), headers=headers, verify=False, timeout=10)
        if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 200:
            stat_dict = response1.json()['data']
            navnum_dict = response2.json()['data']
            upstat_dict = response3.json()['data']
            msg_dict.update(stat_dict)
            msg_dict.update(navnum_dict)
            msg_dict.update(upstat_dict)
    except Exception as e:
        print e
    return msg_dict
