import os

import requests

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
    print("Downloading: " + str(i) + '.jpg, size: ', end='')
    try:
        data = requests.get(url, headers=headers, timeout=(2, 5))
        if len(data.content) / 1024 >= 950.0:
            print(f'{len(data.content) / (1024 * 1024):.2f} MB')
        else:
            print(f'{len(data.content)/1024:.2f} KB')
        with open('Pictures/' + str(i) + '.jpg', 'wb') as file:
            file.write(data.content)
        i += 1
        
        failed = 0
    except:
        print('Failed.')
        failed += 1
        if failed > 5:
            print('Failure reached 5 times, the Program has stopped.')
            break
