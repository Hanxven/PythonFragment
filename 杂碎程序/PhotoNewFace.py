import requests
from contextlib import closing
import os
import time
def showProgressBar(cur, all):
    pro = (cur / all) * 100
    grid = int(40 * (cur / all))
    if grid == 0:
        st = ' ' * 40
    elif grid == 40:
        st = '=' * 40
    else:
        st = '=' * (grid - 1) + '>' + ' ' * (40 - grid)
    if 1024 <= cur <= 1024 * 1024:
        cursize = f'{cur / 1024:6.2f}' + ' KB'
    elif cur < 1024:
        cursize = f'{cur:6}' + ' B'
    elif cur >= 1024 * 1024:
        cursize = f'{cur / (1024 * 1024):6.2f}' + ' MB'
    if 1024 <= all <= 1024 * 1024:
        allsize = f'{all / 1024:6.2f}' + ' KB'
    elif all < 1024:
        allsize = f'{all:6}' + ' B'
    elif all >= 1024 * 1024:
        allsize = f'{all / (1024 * 1024):6.2f}' + ' MB'
    print(f'[{st}] {pro:6.2f} %, {cursize}/{allsize}', end='\r')
    
# Hanxven Wired Program
url = 'https://thispersondoesnotexist.com/image'

headers = {
    'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': '__cfduid=d0adc2a00d2614c7ce7dea8fa731bd0ae1591334627',
    'referer': 'https://thispersondoesnotexist.com/',
    'sec-fetch-dest': 'image',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44'
}

if not os.path.exists('Pictures'):
    os.mkdir('Pictures')

failed = 0
i = 0
while True:
    if os.path.exists('Pictures/' + str(i) + '.jpg'):
        i += 1
        continue 
    else:
        break

while i < 10000:
    try:
        os.system('cls')
        print(f'current downloading: {i}.jpg:')
        print('connecting...', end='\r')
        with closing(requests.get(url, headers=headers, stream=True, timeout=(5, 5))) as res:
            chunk_size = 1024
            data_count = 0
            content_size = int(res.headers['content-length'])
            print(res.headers)       
            with open('Pictures/' + str(i) + '.jpg', 'wb') as file:
                for data in res.iter_content(chunk_size=chunk_size):
                    data_count += len(data)
                    file.write(data)
                    showProgressBar(data_count, content_size)
        print('')
        i += 1
        failed = 0 
    except requests.Timeout:
        print('Failed, TIMEOUT.')
        failed += 1
        time.sleep(0.5)
    except requests.exceptions.ConnectionError:
        print('\nDownloading TIMEOUT.')
        failed += 1
        time.sleep(0.5)
    finally:
        if failed > 5:
            print('Failures have reached 5 times, the program was forced to stop.')
            break

