import json
import logging
import requests, time, random
import datetime
# @Time    : 2021/08/10 15:30
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_status(self):
    if self['code'] == 0:
        return "健康打卡成功"
    elif self['code'] == 1:
        return "健康打卡时间结束"
    elif self['code'] == -10:
        return "···JWSESSION已失效"
    else:
        return "！！！发生未知错误"

class answer:
    def __init__(self):

        self.jwsessionName = ["xxx"]  # 修改1：姓名

        self.my_sender = 'XXX'  # 修改2：发信人的邮箱账号,写自己的QQ邮箱号
        self.my_pass = 'xxx'  # 修改3：发件人邮箱授权码
        self.my_user = 'xxx'  # 修改4：收件人邮箱账号，同样写自己的

        self.api = "https://student.wozaixiaoyuan.com/health/save.json"
        self.headers = {
            "Host": "student.wozaixiaoyuan.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "User-Agent": "xxx",  # 修改5：User-Agent
            "Referer": "xxx",  # 修改6：Referer
            "Content-Length": "360",
            "JWSESSION": "xxx",  # 修改7：JWSESSION
        }

        self.data = {
            "answers": '["0"]',

            # 修改8：打卡地址
           "longitude": "xxx",  # 经度
            "latitude": "xxx",  # 纬度
            "country": "中国",
            "province": "xxx省",
            "city": "xxx市",
            "district": "xxx区",
            "township": "xxx街道",
            "street": "xxx路",
        }
    
    def get_seq(self):
        current_hour = datetime.datetime.now()
        current_hour = current_hour.hour + 8 
        # @Author  : Dominic.
        if 0 <= current_hour <=18:
            return 0
        else:
            return 1

    def run(self):
        # @FileName: 健康打卡.py
        print("JWSESSION:" + self.headers["JWSESSION"])
        print(datetime.datetime.now())
        res = requests.post(self.api, headers=self.headers, data=self.data, ).json()  # 打卡提交
        time.sleep(1)
        print(res)
        print(random.randint(1, 100))

        try:
            msg = MIMEText(self.jwsessionName[0]+"  "+get_status(res), 'plain', 'utf-8')  # 填写邮件内容
            msg['From'] = formataddr(["我在校园", self.my_sender])  # 发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["Me", self.my_user])  # 收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = get_status(res)  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
            server.login(self.my_sender, self.my_pass)  # 发件人邮箱账号、邮箱授权码
            server.sendmail(self.my_sender, [self.my_user, ], msg.as_string())  # 发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            res = False
        return True


if __name__ == "__main__":
    answer().run()


def main_handler(event, context):
    logger.info('got event{}'.format(event))
    # @Author  : Dominic.
    return answer().run()