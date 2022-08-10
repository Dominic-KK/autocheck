import json
import logging
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

import requests

# @Time     : 2022年8月5日10:10:10
# @Author   : Dominic & Smallway
# ***************************使用说明***********************************
# **************  将以下12个修改项改为对应的内容即可  ***************
# **************  作者很忙，有问题优先查阅文档最后的 Q&A  *******************
# **************  作者很忙，有问题优先查阅文档最后的 Q&A  *******************
# **************  作者很忙，有问题优先查阅文档最后的 Q&A  *******************

mySender = "xxxxx"  # 修改1：发件人邮箱
myToken = "xxxxx"  # 修改2：发件人邮箱授权码
myReceiver = "xxxxx"  # 修改3：收件人邮箱，可以和发件人邮箱相同
username = "xxxxx"  # 修改4：通常是手机号
password = "xxxxx"  # 修改5：我不看我不看
province = "xx省"  # 修改6：魔仙堡省
city = "xx市"  # 修改7：女王市
district = "xx区"  # 修改8：游乐区
signArea = ""  # 修改9：巴啦啦魔法大学，不在校区打卡一定不要填
t1 = "绿色" # 修改10：您所在地的健康码颜色
t2 = "已完成接种" # 修改11：您是否已接种新冠疫苗
User_Agent = "User-Agent: Mozilla/5.0 (Linux; Android 11; V2055A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4277 MMWEBSDK/20220706 Mobile Safari/537.36 MMWEBID/815 MicroMessenger/8.0.25.2200(0x2800193B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxce6d08f781975d91"  # 修改12：安卓端UA，抓包获取，可以不改


class loginUser:
    def __init__(self):
        self.headers = {
            "Host": "gw.wozaixiaoyuan.com",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "User-Agent": str(User_Agent),
        }
        self.login_api = "https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username?"
        self.ch_pwd_api = "https://gw.wozaixiaoyuan.com/basicinfo/mobile/my/changePassword?"

    def login(self):
        print("〇 Be logging in…… ")
        url = self.login_api + "username=" + username + "&password=" + password
        self.headers['Referer'] = "https://gw.wozaixiaoyuan.com/h5/mobile/basicinfo/index/login/index"
        resp = requests.session().post(url, data="{}", headers=self.headers)
        res = json.loads(resp.text)
        jwsession = ""
        status = False
        if res["code"] == 0:
            print("√ Login success.")
            jwsession = self.headers['JWSESSION'] = resp.headers['JWSESSION']
            status = True
        elif res['code'] == 101:
            print("× Incorrect password. Please fix it!")
            print("× Error: ", res['message'])
            # self.change_pwd()
        else:
            print("× Login failed.")
            print("× Error: ", res['message'])
        return {'status': status, 'data': jwsession}


class checker:
    def __init__(self, jwsession):
        self.headers = loginUser().headers
        self.headers['JWSESSION'] = jwsession
        self.jkdk_api = "https://gw.wozaixiaoyuan.com/health/mobile/health/save?batch="

    def check_jkdk(self):
        batchId = self.getBatch()
        url = self.jkdk_api + batchId
        self.headers['Referer'] = 'https://gw.wozaixiaoyuan.com/h5/mobile/health/0.1.6/health/detail?id=' + batchId
        if signArea is "":
            data1 = {
                'locationType': 0,
                'inSchool': 0,
                'location': "中国/" + province + "/" + city + "/" + district
            }
        else:
            data1 = {
                'locationType': 1,
                'inSchool': 1,
                'location': 0,
                'signArea': signArea
            }
        data2 = {
            "t1": t1,
            "t2": t2,
            "type": 0,
            "locationState": -1,
        }
        data = json.dumps(dict(data1, **data2))
        res = requests.post(url, headers=self.headers, data=data).json()
        res['status'] = False
        if res['code'] == 0:
            print("√ Check in success.")
            res['status'] = True
        else:
            print("× Check in failed!")
            print("× Error: ", res['message'])

        return res

    def getBatch(self):
        url = 'https://gw.wozaixiaoyuan.com/health/mobile/health/getBatch'
        self.headers['Referer'] = 'https://gw.wozaixiaoyuan.com/h5/mobile/health/0.1.8/health'
        res = requests.post(url, headers=self.headers).json()
        batchId = res['data']['list'][0]['id']
        return batchId


class observer:
    def __init__(self, status):
        self.status = status
        self.my_Name = "嗨害 冤种！"  # 我叫冤种
        self.my_sender = str(mySender)
        self.my_pass = str(myToken)
        self.my_user = str(myReceiver)

    def sendEmail(self):
        status = False
        try:
            msg = MIMEText(self.my_Name + "  " + self.get_status(self.status), 'plain', 'utf-8')
            msg['From'] = formataddr(["我在校园", self.my_sender])  # 双引号内是发件人昵称，可以自定义
            msg['To'] = formataddr(["不爱打卡的大冤种", self.my_user])  # 双引号内是收件人邮箱昵称，可以自定义
            msg['Subject'] = self.get_status(self.status)
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)
            server.login(self.my_sender, self.my_pass)
            server.sendmail(self.my_sender, [self.my_user, ], msg.as_string())
            server.quit()
            print("√ Send email success.")
            status = True
        except Exception as e:
            print("× Send email failed!")
            print("× Error: ", e)
        return {'status': status}

    @staticmethod
    def get_status(status):
        if status == 0:
            return "健康打卡成了！"
        elif status == 1:
            return "晚了，一切都晚了"
        elif status == -10:
            return "···我喊破喉咙都登录不了哇"
        else:
            return "！！！快来看看，这咋滴了"


if __name__ == "__main__":
    myLogin = loginUser()
    loginRes = checkRes = emailRes = {'status': False}
    loginRes = myLogin.login()
    if loginRes['status']:
        myCheck = checker(loginRes['data'])
        checkRes = myCheck.check_jkdk()
    emailRes = observer(checkRes['code']).sendEmail()


def handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info('got event{}'.format(event))
    res = {'@Author ': 'Dominic&Smallway'}
    if not loginRes['status']:
        res['Login Exception': 'Please read the console log.']
    if not checkRes['status']:
        res['Check Exception': 'Please read the console log.']
    if not emailRes['status']:
        res['Email Exception': 'Please read the console log.']

    return res

