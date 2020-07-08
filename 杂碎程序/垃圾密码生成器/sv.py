import requests
import random

def randomNum():
    dig1 = random.randrange(8, 12)    #生成位数
    dig2 = random.randrange(dig1, 12)
    rd = random.randrange(10**dig1, 9*10**dig2)
    return rd


url = 'http://www.aboverp.cn//1/q1q.php'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                  'AppleWebKit/537.36 (KHTML, '
                  'like Gecko) Chrome/67.0.3396.99 '
                  'Safari/537.36',
    'Connection': 'keep-alive',
    'Sec-Fetch-Site':'same-origin',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Dest':'empty',
    'Accept':'application/json, text/plain, */*',
}

data = {
    'p': '3f',
    's6dd1e4c402b7872f': '',
    'scfbad2e80f58d206': '',
    'sa7929578b408c909': '',
    's7ff2b2e95569f56d': '',   #账号
    'se6393254e72ffa4d': ''    #密码
}

def startfuck(id):
    while 1: 
        rdnum = randomNum()
        rdpwd = randomNum()
        data['s7ff2b2e95569f56d'] = str(rdnum)
        data['se6393254e72ffa4d'] = str(rdpwd)
        try:
            res = requests.post(url, data=data, timeout=10 ,headers=header)
            print(f'线程ID: {id}, 假账号:{rdnum}, 假密码:{rdpwd}')
            print(res)
        except:
            print(f'线程{id}超时')


