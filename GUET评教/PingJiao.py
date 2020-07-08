# coding:utf-8
import configparser
import requests
import json
import random
import re
import time
import os


# Hanxven20200705




# 设置学期, 这里是2019-2020下学期
TERM = '2019-2020_2'


# 吹评语大全, 可自行增加, 在每个老师的评语中会随机选择一条
goodlist = [
    '好。',
    '老师上课认真，工作负责。',
    '细心，认真批改作业。',
    '上课幽默风趣，为人大大方方。',
    '很棒。',
    '循循善诱，水平精湛。',
    '讲题清晰，认真大度。',
    '具有创造力的老师。',
]

# _dc生成器, 也就是1970年到现在的毫秒数
def _dc() -> int:
    return int(time.time() * 1000)

if os.path.exists('setting.json'):
    print('配置文件存在，将读取文件内的设置.')
    with open('setting.json', 'r', encoding='utf-8') as file:
        jsondata = file.readlines()
    jsondata = ''.join(jsondata)
    try:
        jsondata = json.loads(jsondata)
        TERM = jsondata['TERM']
        goodlist = jsondata['goodlist']
    except:
        print('文件读取出现错误，将使用默认设置.')
    


# 建立一个session以供处理
ss = requests.session()

# 登录获取
loginurl = 'http://bkjw.guet.edu.cn/Login/SubmitLogin'

# 验证码链接获取
ckurl = 'http://bkjw.guet.edu.cn/login/GetValidateCode?id=' + str(random.random())

# 下载验证码图片的headers，也可用于之后的所有操作，必要部分
ckheaders = {
    'Host': 'bkjw.guet.edu.cn',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36 Edg/83.0.478.37',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'http://bkjw.guet.edu.cn/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

# 接收字符串输入
userinput = input("输入账号, 密码, 以空格或其他分隔符分割. 比如: 1900301037 123456\n")
print('验证码已经保存到当前运行路径, 若未自动打开，请手动查看.')
infolst = re.split(r'[,，|/；;、\s]', userinput)

# 获取图片
ckcoderes = ss.get(ckurl, headers=ckheaders)
# 写入文件
with open(r'ck.jpg', 'wb') as fp:
    fp.write(ckcoderes.content)
os.system('start ck.jpg')

ckcode = input('输入得到的验证码:')



# 虽说是空格分割，实际上以下字符都是可以的，包括各种空白


ckcodesubmit = {
    'us': infolst[0],
    'pwd': infolst[1],
    'ck': ckcode
}
studentid = ckcodesubmit['us']

# 登录尝试
loginres = ss.post(loginurl, data=ckcodesubmit)
ckcoderes = json.loads(loginres.text)


if ckcoderes['success'] == False:
    print('无法登录. 请确认用户名, 密码以及验证码的正确性.')
    os._exit(0)

# debug
#print(loginres.text)


# 获取当前学期的所有待评教老师：
courselist = 'http://bkjw.guet.edu.cn/student/getpjcno?_dc=' + str(_dc()) + '&term=' + TERM +  '&page=1&start=0&limit=100'

courseinfolist = ss.get(courselist, headers = ckheaders)

sublistjson = json.loads(courseinfolist.text)

#print(sublistjson)

sublist = []

# 老师名字，课程名称，课程ID，课程序号，老师编号
for item in sublistjson['data']:
    curlist = []
    curlist.append(item['name'])
    curlist.append(item['cname'])
    curlist.append(item['courseid'])
    curlist.append(item['courseno'])
    curlist.append(item['teacherno'])
    sublist.append(curlist)

#print(sublist)

# 开始设置自动保存
savedata = {
    'term' : TERM,
    'courseno' : '',
    'stid' : studentid,
    'cname' : '',
    'name' : '',
    'teacherno' : '',
    'courseid' : '',
    'lb' : '1',
    'chk' : '',
    'can' : 'true',
    'userid' : '',
    'bz' : '',
    'score' : '100'
}
savestr = '[{"term":"","lsh":1129,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"1","zbnh":"老师上课不迟到，不早退，不擅自离开课堂，不在课内接打电话，不随便调停课，无停课不补","qz":0.02,"zp":0},{"term":"","lsh":1130,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"2","zbnh":"老师对该门课程怀有热情和兴趣","qz":0.06,"zp":0},{"term":"","lsh":1131,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"3","zbnh":"老师将授课目标和学习要求在第一次课前告知你","qz":0.05,"zp":0},{"term":"","lsh":1132,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"4","zbnh":"课程内容组织条理清晰","qz":0.03,"zp":0},{"term":"","lsh":1133,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"5","zbnh":"老师对概念、原理、新的术语解说清晰","qz":0.08,"zp":0},{"term":"","lsh":1134,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"6","zbnh":"课堂问题有效的给我提供了自学和独立客观的思考机会","qz":0.04,"zp":0},{"term":"","lsh":1135,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"7","zbnh":"有效的课程教学互动，激发了我对课程内容的兴趣","qz":0.12,"zp":0},{"term":"","lsh":1136,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"8","zbnh":"老师采用多种方法来评价学生的学习，监控进步情况，及时提出建设性的反馈","qz":0.08,"zp":0},{"term":"","lsh":1137,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"9","zbnh":"老师在教学上以学生为中心，尊重和关心学生，帮助你设定有一定挑战性的学习目标，并鼓励你完成目标","qz":0.09,"zp":0},{"term":"","lsh":1138,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"10","zbnh":"作业和考试覆盖了课程的重要方面","qz":0.04,"zp":0},{"term":"","lsh":1139,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"11","zbnh":"作业的批改详细，反馈及时、不拖延","qz":0.03,"zp":0},{"term":"","lsh":1140,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"12","zbnh":"老师提供的课程补充材料实用性强，对我学习帮助很大","qz":0.04,"zp":0},{"term":"","lsh":1141,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"13","zbnh":"老师鼓励你对课程内容、教学方法等方面提出意见和建议，以改进教学","qz":0.09,"zp":0},{"term":"","lsh":1142,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"14","zbnh":"通过本课程学习，我掌握了该门课程的主要内容和中心问题，并且具备了针对该课程进行交流的能力","qz":0.1,"zp":0},{"term":"","lsh":1143,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"15","zbnh":"通过本课程学习，我加深了对这门课程研究对象的兴趣","qz":0.03,"zp":0},{"term":"","lsh":1144,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"完全同意","afz":100,"djb":"大部分同意","bfz":85,"djc":"部分同意","cfz":70,"djd":"大部分不同意","dfz":40,"dje":"完全不同意","efz":0,"nr":"16","zbnh":"我基本完成了本课程的学习目标","qz":0.07,"zp":0},{"term":"","lsh":1145,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"好","afz":100,"djb":"比较好","bfz":85,"djc":"一般","cfz":70,"djd":"比较差","dfz":40,"dje":"差","efz":0,"nr":"17","zbnh":"你对该老师的总体评价","qz":0.02,"zp":0},{"term":"","lsh":1146,"courseid":"BG0000041X0","lb":1,"score":100,"teacherno":"090944","courseno":"1920218","dja":"好","afz":100,"djb":"比较好","bfz":85,"djc":"一般","cfz":70,"djd":"比较差","dfz":40,"dje":"差","efz":0,"nr":"18","zbnh":"你对本课程的总体评价","qz":0.01,"zp":0}]'
savedict = json.loads(savestr)


for item in sublist:
    try:
        # 需要同时提交两个类似的数据
        saveurl = 'http://bkjw.guet.edu.cn/student/SaveJxpg?_dc=' + str(_dc()) + '&term=' + TERM + '&courseno=' + item[3] + '&teacherno=' + item[4]
        saveurl2 = 'http://bkjw.guet.edu.cn/student/SaveJxpgJg'
        submiturl = 'http://bkjw.guet.edu.cn/student/SaveJxpgJg/1'

        # 设置好里面的信息
        for each in savedict:
            each['term'] = TERM
            each['courseid'] = item[2]
            each['courseno'] = item[3]
            each['teacherno'] = item[4]
    
        # 设置好里面的信息
        savedata['courseno'] = item[3]
        savedata['cname'] = item[1]
        savedata['name'] = item[0]
        savedata['teacherno'] = item[4]
        savedata['courseid'] = item[2]
        savedata['bz'] = random.choice(goodlist)

        res = ss.post(saveurl, headers = ckheaders, json = savedict)
        res2 = ss.post(saveurl2, headers = ckheaders, data = savedata)
        submit = ss.post(submiturl, headers = ckheaders, data = savedata)
    
        res = json.loads(res.text)
        res2 = json.loads(res2.text)
        submit = json.loads(submit.text)

        if res['success'] == True and res2['success'] == True and submit['success'] == True:
            print(f'老师{item[0]}, 课程{item[1]}: 评教成功.')
        else:
            print(f'老师: {item[0]}, 未知原因评教失败, 可能已经提交过.')
    except:
        print(f'未知原因, 老师{item[0]}, 评教失败了, 或许是网络太卡了?')


os.system('pause')
    


