import random


# 电话号码开头
pwdphone = ['134', '135', '136', '137', '138', '139', '150',
            '151', '152', '157', '158', '159', '182', '187',
            '188', '147', '130', '131', '132', '155', '156',
            '186', '145', '133', '153', '189', '191', '147',
            '145'
]

pwdH = ['q', 'w', 'r', 't', 'y', 'p', 's', 'd', 'f',
        'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'b',
        'n', 'm', 'v'
]

pwdE = ['e', 'o', 'a', 'i', 'u', 'oo', 'ee', 'io', 'oi', 'une', 'en'
        'ao', 'ae', 'one', 'ang', 'ung', 'ie', 'ei', 'aa', 'ii', 'ou',
        'ex', 'ss', 'ast', 'est', 'ab', 'ool'
]

pwdS = [
    '-', '*', '/' ,'+', '\\', ']', '[', '{', '}', '=', '_', '@',
    '#', '!', '%', '^', '&', '*', '?'  
]

# 密码随机组合方式：n为数字, p为手机号码, w为单词, s为符号
pwdCombie = [
    'nnn', 'pn', 'nw', 'ns', 'wnn', 'nnw', 'pw', 'ns', 'wws', 'wn', 'ww', 'nsn', 'nsw',
    'nwn', 'wsw', 'www', 'nns'
]


def GenerateFakeNumber(lenL = 4, lenR = 6, mode = 0):
    """
    函数生成一个虚假的数字串
    返回一个字符串, 长度默认9~12
    mode: 0为开头非0, 1为无限制
    """
    dig = random.randrange(lenL, lenR)
    string = ''
    i = 1
    if mode == 0:
        string += str(random.randrange(1, 9))
    elif mode == 1:
        string += str(random.randrange(0, 9))

    while i <= dig - 1:
        string += str(random.randrange(0, 9))
        i += 1
    return string

def GenerateFakePassword():
    """
    函数生成一个虚假的密码组合
    返回一个字符串
    """
    pwd = ''
    combie = random.choice(pwdCombie)
    for ch in combie:
        if ch == 'n':
            pwd += GenerateFakeNumber()
        elif ch == 'p':
            pwd += GenerateFakePhoneNumber()
        elif ch == 's':
            pwd += GenerateFakeSymbol()
        elif ch == 'w':
            i = random.randrange(0, 3)
            pwd += GenerateFakeWord(mode=i)

    if len(pwd) <= 8:
        pwd += GenerateFakeNumber()

    return pwd[:16]

def GenerateFakePhoneNumber():
    """
    生成了一个随机手机号
    """
    head = random.choice(pwdphone)
    i = 0
    while i < 8:
        head += str(random.randrange(0, 9))
        i += 1
    return head

def GenerateFakeWord(lenL = 1, lenR = 3, mode = 0):
    """
    生成一个随机的单词
    最大长度取决于输入
    默认为6
    输入模式: 0为首字母大写, 1为全小写, 2为全大写
    """
    count = random.randrange(lenL, lenR)
    fakeword = ''
    i = 0
    if mode == 0:
        fakeword += random.choice(pwdH).upper()
    elif mode == 1:
        fakeword += random.choice(pwdH)

    fakeword += random.choice(pwdE)
    while i < count - 1:
        fakeword += random.choice(pwdH)
        fakeword += random.choice(pwdE)
        i += 1
    
    if mode == 2:
        return fakeword.upper()
    else:
        return fakeword

def GenerateFakeSymbol(lenL = 1, lenR = 2):
    dig = random.randrange(lenL, lenR)
    i = 0
    st = ''
    while i <= dig:
        st += random.choice(pwdS)
        i += 1
    return st

if __name__ == '__main__':
    for i in range(0,100):
        #print('虚假账号:' + GenerateFakeNumber())
        #print('虚假手机:' + GenerateFakePhoneNumber())
        #print('虚假单词:' + GenerateFakeWord())
        #print('虚假符号:' + GenerateFakeSymbol())
        print('虚假密码:' + GenerateFakePassword())


