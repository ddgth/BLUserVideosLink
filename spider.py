#-*- coding: utf-8 -*-
import configparser
import requests
import json
import re

current = 0

cf = configparser.ConfigParser()
cf.read('config.conf')
# baseUrl = cf.get('baseinfo','base_url')
userAgent = cf.get('baseinfo','user_agent')



def getBetweenStr(str, start, end):
    regex = r''+start+'([\s\S]*)'+end+''
    matches = re.findall(regex, str)
    for match in matches:
        return match
    return ''

def getLinks(baseUrl, file):
    global current 
    current =  current + 100
    response = requests.get(baseUrl, headers={'user-agent': userAgent})
    res = json.loads(response.text)
    vlist = res['data']['vlist']
    with open(file, 'a+') as f:
        for item in range(len(vlist)):
            f.write('https://www.bilibili.com/video/av' + str(vlist[item]['aid']) + '\n')
    count = int(getBetweenStr(str(res['data']['tlist']), 'count\': ', ', \'name'))
    if count > current:
        getLinks(baseUrl, file)



if __name__ == "__main__":
    userId = '407784079'
    getLinks('https://space.bilibili.com/ajax/member/getSubmitVideos?mid='+userId+'&pagesize=100&tid=0&page=1&keyword=&order=pubdate', 'link.csv')
  
    # baseUrl = 'https://space.bilibili.com/ajax/member/getSubmitVideos?mid=407784079&pagesize=100&tid=0&page=1&keyword=&order=pubdate'
    # response = requests.get(baseUrl, headers={'user-agent': userAgent})
    # res = json.loads(response.text)
    # vlist = res['data']['vlist']
    # count = int(getBetweenStr(str(res['data']['tlist']), 'count\': ', ', \'name'))
    # links = []
    # for item in range(len(vlist)):
    #     links.append('https://www.bilibili.com/video/av' + str(vlist[item]['aid']))
    # print(links)