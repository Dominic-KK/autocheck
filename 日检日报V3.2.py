import json
import logging
import requests
import time
import random
import datetime
# @Time:2022年5月4日22:36:26
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
# 注意，本代码仅供学习使用，请勿用于盈利等等，作者QQ1097123142，欢迎交流学习
# 日检日报V3.2.1版本（没有什么改进，就是从底层优化了代码，更加的方便使用）
# 此外，特别鸣谢@DominicKK在我学习的路上的帮助

# ********************************使用说明********************************
# **************将以下14个修改项"xxx" 修改为对应的内容即可*******************
# **************将以下14个修改项"xxx" 修改为对应的内容即可*******************
# **************将以下14个修改项"xxx" 修改为对应的内容即可*******************
# **************将以下14个修改项"xxx" 修改为对应的内容即可*******************
# **************将以下14个修改项"xxx" 修改为对应的内容即可*******************
# **************将以下14个修改项"xxx" 修改为对应的内容即可*******************

发件人 = "xxx"  # 修改1：填写发件人的邮件
邮箱授权码 = "xxx"  # 修改2：发件人邮箱授权码
收件人邮箱 = "xxx"  # 修改3：收件人的邮件
我在校园用户名 = "xxx"  # 修改4：你不会看不懂要修改啥吧
我在校园密码 = "xxx"  # 修改5：emmmmmm
Referer = "xxx"  # 修改6：抓包获取
User_Agent = "xxx"  # 修改7：抓包获取
latitude = xxx  # 修改8：纬度
longitude = xxx  # 修改9：经度
country = "中国"  # 修改10：一般不用改，我不信还有国外的要用，有的话我把我电脑屏幕吃了
province = "xx省"  # 修改11：省份
city = "xx市"  # 修改12：城市
district = "xx区"  # 修改13：区县
township = ""  # 修改14：街道

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def get_status(self):
    if self['code'] == 0:
        return "日检日报成功"
    elif self['code'] == 1:
        return "日检日报时间结束"
    elif self['code'] == -10:
        return "···Token已失效"
    else:
        return "！！！发生未知错误"


class answer:
    def __init__(self):      #
        username = str(我在校园用户名)
        password = str(我在校园密码)
        header = {
            "Host": "student.wozaixiaoyuan.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-us,en",
            "Connection": "keep-alive",
            "User-Agent": str(User_Agent),
            "Content-Length": "360",
        }
        loginUrl = "https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username"
        data = "{}"
        session = requests.session()
        url = loginUrl + "?username=" + username + "&password=" + password
        respt = session.post(url, data=data, headers=header)
        res = json.loads(respt.text)
        if res["code"] == 0:
            print("登陆成功")
            jwsession = respt.headers['JWSESSION']
        else:
            print(res)
            print('登录失败')

        self.my_Name = "xxx"
        self.my_sender = str(发件人)
        self.my_pass = str(邮箱授权码)
        self.my_user = str(收件人邮箱)

        self.api = "https://student.wozaixiaoyuan.com/heat/save.json"
        self.headers = {
            "Host": "student.wozaixiaoyuan.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "User-Agent": str(User_Agent),
            "Referer": str(Referer),
            "Content-Length": "360",
            "JWSESSION": str(jwsession),
        }
        self.data = {
            "answers": '["0"]',
            "seq": self.get_seq(),
            "temperature": self.get_random_temprature(),
            "timestampHeader": "",

            "longitude": str(longitude),
            "latitude": str(latitude),
            "country": str(country),
            "province": str(province),
            "city": str(city),
            "district": str(district),
        }

    # 获取随机体温
    def get_random_temprature(self):
        random.seed(time.ctime())
        return "{:.1f}".format(random.uniform(36.2, 36.7))

    # seq的1,2,3代表早，中，晚
    def get_seq(self):
        current_hour = datetime.datetime.now()
        current_hour = current_hour.hour + 8
        if 6 <= current_hour <= 9:
            return "1"
        elif 12 <= current_hour < 15:
            return "2"
        elif 19 <= current_hour < 22:
            return "3"
        else:
            return 1

    def run(self):
        datatime = time.time()
        self.data["timestampHeader"] = int(datatime)
        res = requests.post(self.api, headers=self.headers,
                            data=self.data, ).json()  # 打卡提交
        print(res['message'])
        try:
            msg = MIMEText(self.my_Name+"  "+get_status(res),
                           'plain', 'utf-8')  # 填写邮件内容
            # 括号里的对应发件人邮箱昵称、发件人邮箱账号
            msg['From'] = formataddr(["我在校园", self.my_sender])
            # 括号里的对应收件人邮箱昵称、收件人邮箱账号，此处xxx可选择性修改
            msg['To'] = formataddr(["xxxxx", self.my_user])
            msg['Subject'] = get_status(res)  # 邮件的主题，也可以说是标题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器
            server.login(self.my_sender, self.my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
            # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.sendmail(self.my_sender, [self.my_user, ], msg.as_string())
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            res = False
        return True


if __name__ == "__main__":
    answer().run()


def handler(event, context):
    logger.info('got event{}'.format(event))
    return answer().run()
