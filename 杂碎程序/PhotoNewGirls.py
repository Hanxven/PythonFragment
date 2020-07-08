import requests
from contextlib import closing
import os
import time
import random
import threading

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

def beginGetGirls(threadno):    
# Hanxven Wired Program
    url = 'https://www.thiswaifudoesnotexist.net/'

    headers = {
        'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': '__cfduid=d0adc2a00d2614c7ce7dea8fa731bd0ae1591334627',
        #'referer': 'https://thispersondoesnotexist.com/',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.44'
    }

    if not os.path.exists('GirlPictures'):
        os.mkdir('GirlPictures')

    failed = 0
    i = 0


    while i < 10000:
        try:
            #os.system('cls')
            randomnum = random.randrange(0, 100000)
            if os.path.exists('GirlPictures/' + str(randomnum) + '.jpg'):
                continue
            url = 'https://www.thiswaifudoesnotexist.net/example-' + str(randomnum) + '.jpg'
            #print(f'current downloading: {i}.jpg, example-{randomnum}.jpg:')
            #print('connecting...', end='\r')
            with closing(requests.get(url, headers=headers, stream=True, timeout=(5, 5))) as res:
                if res.status_code == 404:
                    continue
                chunk_size = 1024
                data_count = 0
                #content_size = int(res.headers['content-length'])
                with open('GirlPictures/' + str(randomnum) + '.jpg', 'wb') as file:
                    for data in res.iter_content(chunk_size=chunk_size):
                        data_count += len(data)
                        file.write(data)
                        #showProgressBar(data_count, content_size)
            print(f'Thread {threadno} finished downloading example-{randomnum}.jpg')
            i += 1
            failed = 0 
        except requests.Timeout:
            print(f'Thread {threadno} Timeout')
            failed += 1
            time.sleep(0.5)
        except requests.exceptions.ConnectionError:
            print(f'Thread {threadno} Timeout')
            failed += 1
            time.sleep(0.5)
        finally:
            if failed > 5:
                print('Failures have reached 5 times, the program was forced to stop.')
                break


if __name__ == '__main__':
    th1 = threading.Thread(target=beginGetGirls, args=(1,))
    th2 = threading.Thread(target=beginGetGirls, args=(2,))
    th3 = threading.Thread(target=beginGetGirls, args=(3,))
    th4 = threading.Thread(target=beginGetGirls, args=(4,))
    th5 = threading.Thread(target=beginGetGirls, args=(5,))
    th6 = threading.Thread(target=beginGetGirls, args=(6,))
    th7 = threading.Thread(target=beginGetGirls, args=(7,))
    th8 = threading.Thread(target=beginGetGirls, args=(8,))

    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
    th6.start()
    th7.start()
    th8.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()
    th6.join()
    th7.join()
    th8.join()
