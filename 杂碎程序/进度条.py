# coding:utf-8
import time
# 蛋疼的进度条
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

if __name__ == '__main__':
    # example
    i = 0
    while i <= 15630:
        showProgressBar(i, 15630)
        time.sleep(0.5)
        i += 521
    print('')