import base64
import datetime
import json
import logging
import random
import smtplib
import time
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
signArea = "xx学校"  # 修改9：巴啦啦魔法大学，或其他地址
QRcode = ""  # 修改10：图片，不需要可不填，需要则参考教程
Referer = "https://gw.wozaixiaoyuan.com/h5/mobile/health/0.1.6/health/detail?id=1300001"  # 修改11：抓包获取，可以不改
User_Agent = "User-Agent: Mozilla/5.0 (Linux; Android 11; V2055A Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4277 MMWEBSDK/20220706 Mobile Safari/537.36 MMWEBID/815 MicroMessenger/8.0.25.2200(0x2800193B) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxce6d08f781975d91"  # 修改12：安卓端UA，抓包获取，可以不改

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_status(self):
    if self['code'] == 0:
        return "哎！健康打卡成了！"
    elif self['code'] == 1:
        return "晚了，一切都晚了"
    elif self['code'] == -10:
        return "···我喊破喉咙都登录不了哇"
    else:
        return "！！！快来看看，这咋滴了"


class answer:
    def __init__(self):
        header = {
            "Host": "gw.wozaixiaoyuan.com",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "User-Agent": str(User_Agent),
            "Referer": str(Referer),
            "Content-Length": "360",
        }
        loginUrl = "https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username"
        data = "{}"
        session = requests.session()
        url = loginUrl + "?username=" + username + "&password=" + password
        respt = session.post(url, data=data, headers=header)
        res = json.loads(respt.text)
        if res["code"] == 0:
            print("Login success.")
            jwsession = respt.headers['JWSESSION']
        else:
            print("Login failed!!!")
            print(res['message'])

        self.my_Name = ""  # 我叫冤种
        self.my_sender = str(mySender)
        self.my_pass = str(myToken)
        self.my_user = str(myReceiver)

        self.api = "https://gw.wozaixiaoyuan.com/health/mobile/health/save?batch=1300001"
        self.headers = {
            "Host": "gw.wozaixiaoyuan.com",
            "Content-Type": "application/json;charset=UTF-8",
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "User-Agent": str(User_Agent),
            "Referer": str(Referer),
            "Content-Length": "360",
            "JWSESSION": str(jwsession),
        }
        self.data = json.dumps({
            "t1": self.get_random_temprature(),
            "t2": self.upload_img(),
            "type": 0,
            "locationType": 1,
            "signArea": signArea,
            "province": province,
            "city": city,
            "district": district,
        })

    # 检查图片是否存在
    def isImage(self, image):
        if image == "":
            print("〇 No image. Download test image now……")
            from urllib.request import urlretrieve
            urlretrieve(
                "https://th.bing.com/th/id/OIP.3Z0rpHpGBoHf9ECKS5FRwwHaHa?w=188&h=188&c=7&r=0&o=5&dpr=1.25&pid=1.7",
                '/tmp/testImage.jpg')
            image = "/tmp/testImage.jpg"
            print("√ Download test image complete.")
        return image

    def imageDecode(self, image):
        with open(image, 'rb') as f:
            image_byte = base64.b64encode(f.read())
        image_de = image_byte.decode('ascii')
        return image_de

    # 上传图片
    def upload_img(self):
        url = "https://gw.wozaixiaoyuan.com/gw/aoss/uploadBase64"
        data = json.dumps({
            "bucket": "health",
            "base64": "data:image/jpeg;base64," + self.imageDecode(self.isImage(QRcode)),
        })
        res = requests.post(url, headers=self.headers, data=data).json()
        if res['code'] == 0:
            print("√ Upload image success.")
        else:
            print("× Upload image failed!")
        return res['data']

    # 随机体温
    def get_random_temprature(self):
        random.seed(time.ctime())
        return "{:.1f}".format(random.uniform(36.2, 36.7))

    def get_seq(self):
        current_hour = datetime.datetime.now()
        current_hour = current_hour.hour + 8
        if 0 <= current_hour <= 18:
            return "1"
        else:
            return 1

    def run(self):
        # @FileName: 健康打卡4.0.py
        res = requests.post(self.api, headers=self.headers, data=self.data).json()  # 打卡提交
        if res['code'] == 0:
            print("√ Check in success.")
        else:
            print("× Check in failed!!!")
        try:
            msg = MIMEText(self.my_Name+"  "+get_status(res), 'plain', 'utf-8')
            msg['From'] = formataddr(["我在校园", self.my_sender])  # 双引号内是发件人昵称，可以自定义
            msg['To'] = formataddr(["不爱打卡的大冤种", self.my_user])  # 双引号内是收件人邮箱昵称，可以自定义
            msg['Subject'] = get_status(res)
            server = smtplib.SMTP_SSL("smtp.qq.com", 465)
            server.login(self.my_sender, self.my_pass)
            server.sendmail(self.my_sender, [self.my_user, ], msg.as_string())
            server.quit()  # 关闭邮箱连接
            print("√ Send email success.")
        except Exception:
            print("× Send email failed!")
            print(res)
            res = False
            print(res)
        return True


if __name__ == "__main__":
    answer().run()


def handler(event, context):
    logger.info('got event{}'.format(event))
    # @Author  : Dominic&Smallway
    return answer().run()
