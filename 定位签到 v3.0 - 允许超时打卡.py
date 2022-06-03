from email import message
import requests
import json
import time
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
# **********************************************************************************************************
#                 定位签到强制签到版
#               请注意，本版本使用请慎重
# 本版本可以突破打卡时间限制，例如未到打卡时间，或超过打卡时间都可以打卡，甚至你还可以覆盖打卡（慎重使用）
#                   只要你不想被发现
# 推荐适用范围：
# 1.忘记打卡可以用这个补卡（挂了云函数后理论上不存在）
# 2.签到扣打卡的补卡（可以绕过物理设备的限制）
#                 综上所述，本版本的使用请慎重
#               @author：Smallway
# **********************************************************************************************************


def handler():
    sender = "xxx"  # 修改1：填写发件人的邮件
    pass_ = "xxx"  # 修改2：发件人邮箱授权码
    user = "xxx"  # 修改3：收件人的邮件
    username = "xxx"  # 修改4：手机号
    password = "xxx"  # 修改5：密码
    Referer = "xxx"  # 6抓包获取
    User_Agent = "xxx"  # 7抓包获取
    latitude = xxx  # 修改8：纬度
    longitude = xxx  # 修改9：经度
    country = "中国"  # 修改10：一般不用改，我不信还有国外的要用，有的话我把我电脑屏幕吃了
    province = "xx省"  # 修改11：省份
    city = "xx市"  # 修改12：城市
    district = "xx区"  # 修改13：区县
    township = ""  # 修改14：街道

# 获取jwsession
    header = {
        "Host": "student.wozaixiaoyuan.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-us,en",
        "Connection": "keep-alive",
        "User-Agent": str(User_Agent),
        "Referer": str(Referer),
        "Content-Length": "360",
    }
    loginUrl = "http://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username"
    data = "{}"
    session = requests.session()
    url = loginUrl + "?username=" + username + "&password=" + password
    respt = session.post(url, data=data, headers=header)
    res = json.loads(respt.text)
    if res["code"] == 0:
        print("登录成功.")
        jwsession = respt.headers['JWSESSION']

    else:
        print(res['message'])


# 第一部分，获取定位打卡的ID和signID
# 获取ID和signID
    getheaders = {
        "Host": "student.wozaixiaoyuan.com",
        "content-type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": str(User_Agent),
        "Referer": str(Referer),
        "Content-Length": "500",
        "JWSESSION": str(jwsession),
    }
    first = 'page=1&size=5'  # 获取id和signid所需要post的内容
    getapi = "http://student.wozaixiaoyuan.com/sign/getSignMessage.json"
    getdata = requests.post(getapi, headers=getheaders,
                            data=first, ).json()  # 获取id和signid
    time.sleep(1)
    getdata = getdata['data']  # 获取返回值中的data数据
    getdata = getdata[0]
    print(getdata)
    print("本公主正在为你打卡，好好给本公主等着")
    realdata = {
        "id": str(getdata['logId']),
        "signId": str(getdata['id']),
        "latitude": latitude,
        "longitude": longitude,
        "country": country,
        "province": province,
        "city": city,
        "district": district,
        "township": township,
    }
    print(realdata)
    api = "http://student.wozaixiaoyuan.com/sign/doSign.json/"
    signheaders = {
        "Host": "student.wozaixiaoyuan.com",
        "Content-Type": "application/json",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "User-Agent": str(User_Agent),
        "Referer": str(Referer),
        "Content-Length": "500",
        "Cookie": "",
        "JWSESSION": str(jwsession),
        "charset": "utf-8",
    }
    res = requests.post(api, headers=signheaders, json=realdata)  # 打卡提交
    time.sleep(1)
    res = eval(res.text)
    if res['code'] == 0:
        message = "本公主给你打过卡了，还不快跪下？"
        state = "打卡成功"
        mail(message, state, sender, pass_, user)
        print("打卡成功"+str(res))
        return "打卡成功"+str(res)
    else:
        message = "人...人家也不知道为什么会出错，喏，这是错误信息，请大人过目："+str(res)
        state = "打卡失败"
        mail(message, state, sender, pass_, user)
        print("打卡失败"+str(res))
        return "打卡失败"+str(res)


def mail(message, state, sender, pass_, user):
    msg = MIMEText(message, 'plain', 'utf-8')
    msg['From'] = formataddr(["我在校园", sender])
    msg['To'] = formataddr(["Me", user])
    msg['Subject'] = state
    server = smtplib.SMTP_SSL("smtp.qq.com", 465)
    server.login(sender, pass_)
    server.sendmail(sender, [user, ], msg.as_string())
    server.quit()


if __name__ == "__main__":
    handler()
