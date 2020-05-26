import msvcrt
import random
import os

# Hanxven_Marvels

# 先固定大小4*4的地图，初始化为0
GameMap = []

# 随机生成的数列表, 本处只生成2或4
NumberList = [2, 4]

# 地图大小
MapSize = 4

# 判定胜利的数
WinNum = 2048


def IniMap(MapSize = 4):
    """
    用于指定地图的大小
    默认为4, 成功返回1, 否则为0
    """

    # 思想: 这个函数是留给之后的扩展的. 本函数生成一个指定宽高的正方形地图
    # 在本程序中只为4, 暂时不可设置其他值

    if MapSize < 3:
        print('地图下限为3')
        return 0
    try:
        cur = 0
        while cur < MapSize:
            GameMap.append([])
            cur += 1
        cur = 0
        while cur < MapSize:
            each = 0
            while each < MapSize:
                GameMap[cur].append(0)
                each += 1
            cur += 1
    except:
        return 0

    return 1


# 打印当前地图
def PrintMap():
    """
    绘制整个地图, 无返回值
    """
    # 思想: 先找出长度最大的数, 之后以本数为基准, 开始排版

    MaxLen = 1

    for line in GameMap:
        MaxNumber = max(line)
        Len = len(str(MaxNumber))
        if Len > MaxLen:
            MaxLen = Len
    MaxLen += 2

    line = ''.center(MaxLen * MapSize + MapSize + 1, '-')

    os.system('cls')

    curLine = 0
    print(line)
    while curLine < len(GameMap):
        curColumn = 0
        print('|', end='')
        while curColumn < len(GameMap[curLine]):
            if GameMap[curLine][curColumn] == 0:
                print(f'{" ":^{MaxLen}}|', end='')
            else:
                print(f'{GameMap[curLine][curColumn]:^{MaxLen}}|', end='')
            curColumn += 1
        print('\n', end='')
        curLine += 1
    print(line)


def isFinished():
    for line in GameMap:
        if WinNum in line:
            return 1
    return 0


def MoveMap(moveDirc):
    """
    移动地图, 有返回值, 1为成功, 0为失败, 用于判断游戏结束
    担任计算的核心函数
    接收一个方向, 将地图按照方向进行合并或移动
    """

    # 思想: 本函数控制实际的移动. 在canMove()函数判断该方向可移动后, 本函数将会
    # 对棋盘进行真正的移动, 具体步骤如下:
    # 首先把所有非0的值记录同时填充该位置为0, 非0值保存为一个临时列表. 之后从[指定方向的相反方向]开始,
    # 在临时列表依次检测相邻两数是否相等, 若相等, 则相加, 并将结果堆积到地图相应列底部, 若不等
    # 
    # [指定方向的相反方向]: 指定方向指的是键盘输入的, 要移动的方向. 反向开始是保证最"底下"的数被优先压扁

    if moveDirc == b'w' or moveDirc == b'W':
        curColumn = 0
        while curColumn < MapSize:
            # 先补齐空位置, 再进行计算
            TempLine = 0
            TempList = []
            # 记录所有的非0值, 并填充原位置为0
            while TempLine < MapSize:
                if GameMap[TempLine][curColumn] != 0:
                    TempList.append(GameMap[TempLine][curColumn])
                GameMap[TempLine][curColumn] = 0
                TempLine += 1
            # 开始挤压计算
            curTempLine = 0
            GameMapLine = 0
            while curTempLine < len(TempList):
                curNum = TempList[curTempLine]
                if curTempLine + 1 >= len(TempList):
                    GameMap[GameMapLine][curColumn] = curNum
                elif curNum == TempList[curTempLine + 1]:
                    GameMap[GameMapLine][curColumn] = 2 * curNum
                    curTempLine += 1
                    GameMapLine += 1
                else:
                    GameMap[GameMapLine][curColumn] = curNum
                    GameMapLine += 1
                curTempLine += 1
            curColumn += 1
    elif moveDirc == b's' or moveDirc == b'S':
        curColumn = 0
        while curColumn < MapSize:
            TempLine = 0
            TempList = []
            while TempLine < MapSize:
                if GameMap[TempLine][curColumn] != 0:
                    TempList.append(GameMap[TempLine][curColumn])
                GameMap[TempLine][curColumn] = 0
                TempLine += 1
            curTempLine = len(TempList) - 1
            GameMapLine = MapSize - 1
            while curTempLine >= 0:
                curNum = TempList[curTempLine]
                if curTempLine <= 0:
                    GameMap[GameMapLine][curColumn] = curNum
                elif curNum == TempList[curTempLine - 1]:
                    GameMap[GameMapLine][curColumn] = 2 * curNum
                    curTempLine -= 1
                    GameMapLine -= 1
                else:
                    GameMap[GameMapLine][curColumn] = curNum
                    GameMapLine -= 1
                curTempLine -= 1
            curColumn += 1
    elif moveDirc == b'a' or moveDirc == b'A':
        curLine = 0
        while curLine < MapSize:
            TempColumn = 0
            TempList = []
            while TempColumn < MapSize:
                if GameMap[curLine][TempColumn] != 0:
                    TempList.append(GameMap[curLine][TempColumn])
                GameMap[curLine][TempColumn] = 0
                TempColumn += 1
            curTempColumn = 0
            GameMapColumn = 0
            while curTempColumn < len(TempList):
                curNum = TempList[curTempColumn]
                if curTempColumn >= len(TempList) - 1:
                    GameMap[curLine][GameMapColumn] = curNum
                elif curNum == TempList[curTempColumn + 1]:
                    GameMap[curLine][GameMapColumn] = 2 * curNum
                    curTempColumn += 1
                    GameMapColumn += 1
                else:
                    GameMap[curLine][GameMapColumn] = curNum
                    GameMapColumn += 1
                curTempColumn += 1
            curLine += 1
    elif moveDirc == b'd' or moveDirc == b'D':
        curLine = 0
        while curLine < MapSize:
            TempColumn = 0
            TempList = []
            while TempColumn < MapSize:
                if GameMap[curLine][TempColumn] != 0:
                    TempList.append(GameMap[curLine][TempColumn])
                GameMap[curLine][TempColumn] = 0
                TempColumn += 1
            curTempColumn = len(TempList) - 1
            GameMapColumn = MapSize - 1
            while curTempColumn >= 0:
                curNum = TempList[curTempColumn]
                if curTempColumn <= 0:
                    GameMap[curLine][GameMapColumn] = curNum
                elif curNum == TempList[curTempColumn - 1]:
                    GameMap[curLine][GameMapColumn] = 2 * curNum
                    curTempColumn -= 1
                    GameMapColumn -= 1
                else:
                    GameMap[curLine][GameMapColumn] = curNum
                    GameMapColumn -= 1
                curTempColumn -= 1
            curLine += 1


def canMove(moveDirc=1):
    """
    判断是否还能移动, 判定游戏结束
    提供一个方向, 如不提供, 则判断所有方向
    """
    # 根据地图大小设定数值, 此处对应4*4地图
    # wcnm 怎么写的这么复杂, 我服了

    # 思想: 以向上为例: 需要判断每一列是否可以移动, 首先从下到上[寻找第一个不为0]的数值, 如果到最后一个才
    # 为非0值, 则判断本列不可移动, 跳出循环开始下一列的寻找. 如果找到了一个非0值, 且不是末尾, 那么判断
    # 其后面是否存在0, 如果存在, 则可以移动, 反之不能. 之后, 以[第一个不为0]且[不是最后一个值]的位置开始, 判
    # 断是否存在连续相同的数, 如果存在, 则可以移动(合并), 反之不能.

    judged = 0
    if moveDirc == b'w' or moveDirc == b'W' or moveDirc == 1:
        judged += 1
        curColumn = 0
        while curColumn < MapSize:
            curLine = MapSize - 1
            skip = 0
            # 找到以一个不为0的值, 判断是否有空位置
            while GameMap[curLine][curColumn] == 0:
                curLine -= 1
                # 在全是0的情况下本列不可移动
                if curLine == 0:
                    skip = 1
                    break
            if skip == 1:
                curColumn += 1
                continue
            FirstNoZero = curLine
            curLine -= 1
            while curLine >= 0:
                if GameMap[curLine][curColumn] == 0:
                    return 1
                curLine -= 1
            curLine = FirstNoZero
            while curLine > 0:
                if GameMap[curLine][curColumn] == GameMap[curLine - 1][curColumn]:
                    return 1
                curLine -= 1
            curColumn += 1
    if moveDirc == b's' or moveDirc == b'S' or moveDirc == 1:
        judged += 1
        curColumn = 0
        while curColumn < MapSize:
            curLine = 0
            skip = 0
            while GameMap[curLine][curColumn] == 0:
                curLine += 1
                if curLine == MapSize - 1:
                    skip = 1
                    break
            if skip == 1:
                curColumn += 1
                continue
            FirstNoZero = curLine
            curLine += 1
            while curLine < MapSize:
                if GameMap[curLine][curColumn] == 0:
                    return 1
                curLine += 1
            curLine = FirstNoZero
            while curLine < MapSize - 1:
                if GameMap[curLine][curColumn] == GameMap[curLine + 1][curColumn]:
                    return 1
                curLine += 1
            curColumn += 1
    if moveDirc == b'a' or moveDirc == b'A' or moveDirc == 1:
        judged += 1
        curLine = 0
        while curLine < MapSize:
            curColumn = MapSize - 1
            skip = 0
            while GameMap[curLine][curColumn] == 0:
                curColumn -= 1
                if curColumn == 0:
                    skip = 1
                    break
            if skip == 1:
                curLine += 1
                continue
            FirstNoZero = curColumn
            curColumn -= 1
            while curColumn >= 0:
                if GameMap[curLine][curColumn] == 0:
                    return 1
                curColumn -= 1
            curColumn = FirstNoZero
            while curColumn > 0:
                if GameMap[curLine][curColumn] == GameMap[curLine][curColumn - 1]:
                    return 1
                curColumn -= 1
            curLine += 1
    if moveDirc == b'd' or moveDirc == b'D' or moveDirc == 1:
        judged += 1
        curLine = 0
        while curLine < MapSize:
            curColumn = 0
            skip = 0
            while GameMap[curLine][curColumn] == 0:
                curColumn += 1
                if curColumn == MapSize - 1:
                    skip = 1
                    break
            if skip == 1:
                curLine += 1
                continue
            FirstNoZero = curColumn
            curColumn += 1
            while curColumn < MapSize:
                if GameMap[curLine][curColumn] == 0:
                    return 1
                curColumn += 1
            curColumn = FirstNoZero
            while curColumn < MapSize - 1:
                if GameMap[curLine][curColumn] == GameMap[curLine][curColumn + 1]:
                    return 1
                curColumn += 1
            curLine += 1

    if judged != 0:
        return 0


def AddRandomBlock(count):
    """
    生成随机块, 块的种类和数量取决于列表和输入参数
    会寻找当前空余的块, 并随机填充
    返回成功生成块的数量
    """

    # 思想: 先找出所有空闲位置的坐标, 之后随机选定一个坐标, 填充一个随机值. 这个随机值
    # 是从预设的列表中随机选择的.

    i = 1
    addedGrid = 0
    freeBlocks = []
    while i <= count:
        freeBlocks.clear()
        line = 0
        column = 0
        while line < MapSize:
            column = 0
            while column < MapSize:
                if GameMap[line][column] == 0:
                    freeBlocks.append([line, column])
                column += 1
            line += 1
        if len(freeBlocks) != 0:
            choosed = random.choice(freeBlocks)
            GameMap[choosed[0]][choosed[1]] = random.choice(NumberList)
            addedGrid += 1
        i += 1
    return addedGrid


if __name__ == '__main__':
    step = 0
    IniMap(MapSize)
    print(f'初始化设置: 地图大小{MapSize}, 规则: 达到{WinNum}')
    os.system('pause')
    AddRandomBlock(2)
    PrintMap()
    while True:
        key = msvcrt.getch()

        # 按Q退出
        if key == b'q' or key == b'Q':
            break

        if canMove(key):
            # 可以移动时, 将移动地图, 同时刷新
            MoveMap(key)
            PrintMap()

            # 如果赢了, 退出循环
            if isFinished():
                print('Finished')
                break

            # 加入随机块, 然后刷新地图
            AddRandomBlock(1)
            PrintMap()

            # 统计+1
            step += 1
        else:
            print('当前方向不可移动')

        # 不能移动, 即游戏结束
        if not canMove():
            break

    print(f'游戏结束, 总步数{step}')
    os.system('pause')
