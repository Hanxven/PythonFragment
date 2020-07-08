# 官方接口

import json
import requests

HEADERS = {
    'Host': 'api.bilibili.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.58',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
}

AV = 'http://api.bilibili.com/x/web-interface/archive/stat?aid='
BV = 'http://api.bilibili.com/x/web-interface/archive/stat?bvid='

string = 'BV1ae411s7Ti'


prefix = string[0:2].lower()
if prefix == 'av' or prefix == 'bv':
    string = string[2:]

AV += string
BV += string

resAV = requests.get(AV, headers=HEADERS)
resBV = requests.get(BV, headers=HEADERS)


resAVJ = json.loads(resAV.text)
resBVJ = json.loads(resBV.text)

if resAVJ['code'] == 0:
    print(f'转化成BV: BV{resAVJ["data"]["bvid"]}')
if resBVJ['code'] == 0:
    print(f'转化成AV: AV{resBVJ["data"]["aid"]}')