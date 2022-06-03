   由于我在校园进行了版本升级，抓包获取 Token 时发现 Token 并没有发生改变，所以写下来这篇教程，仅针对新版我在校园，大致思路：腾讯云函数定时触发脚本，打卡状态通过QQ邮箱进行提醒。这里为什么要用QQ邮箱作为提醒，有两点原因： 其一是我个人觉得旧版教程中的喵提醒使用非常麻烦，喵提醒公众号虽然免费，但是使用过程中需要不断激活48小时，这违背了自动打卡教程省时省力的初衷；其二，QQ号基本上每个人都有，而QQ邮箱是默认注册的，所以用QQ邮箱非常适合大众使用。 作者QQ 3330900358 有疑问欢迎随时交流

------------
2021.08.12更新：因为新版的机制原因，抓包过程只用进行一次，相比之下比旧版方便很多。


[TOC]

------------



### 一、Fiddler 抓包工具

#### 1.安装

安装包下载： Fiddler 安装包和 Fiddler 证书生成器

阿里云盘地址：https://www.aliyundrive.com/s/7gtFaLxH7f5

两个文件都下载下来后，先双击 FiddlerSetup.exe 进行安装，另一个是证书生成器，暂时不用。

#### 2.配置

打开 Fiddler ，点击工具栏中的 Tools → Options

![image-20210802134532161](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802134532161-1627956867319.png)

点击 HTTPS 标签，勾选框住的三项，然后点击右边的 Actions，选择第二项，会弹出一个弹窗，点击确定，之后点击 OK 完成设置

![](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802140021903.png)

这时会发现桌面上多了一个证书文件（如下图），接下来马上会用到

![image-20210802140437482](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802140437482.png)

打开电脑上任何一个浏览器，在这里我用的是 win10 自带的 Edge，打开设置，找到“证书管理”，实在找不到也可以直接搜索

![image-20210802140839373](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802140839373.png)

点击“管理证书”，点击“导入”进入证书导入向导

![image-20210802141018230](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802140839373.png)

点击下一步继续

![image-20210802141144696](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802141018230.png)

选择要导入的文件，点击“浏览”

![image-20210802141332680](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802141332680.png)

在桌面找到刚刚导出的证书文件，点一下证书文件，选择打开

![image-20210802141716446](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802141332680.png)

之后一直点击下一步，直到完成证书导入。到这里配置工作基本完成，可以进行抓包了，刚刚导出在桌面的证书文件也可以删除

#### 3.抓包

接下来从微信电脑端打开我在校园小程序，然后打开日检日报或者健康打卡，会发现 Fiddler 中显示了很多内容，我们找到“student.wozaixiaoyuan.com”这一行，双击打开，在右边选择“Headers”标签，复制三项内容 User-Agent（设备信息）、JWSESSION（作用相当于旧版的 Token）、Referer（学校信息）。在这里先留一个空白，因为还没观察到 JWSESSION 多久会变一次，我在写教程时已经用了第四天了，之后观察到会补上。
​2021.08.12更新：目前 JWSESSION 已经用了半个月，盲猜不会再变了。

![](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802145622192.png)

复制的内容可以发给你的工具人小伙伴，或者你的小号，总之先保留下来备用。

### 二、QQ邮箱

#### 获取授权码

用QQ邮箱发件也需要登录，不是用账号密码，而是授权码，接下来获取授权码

进入QQ邮箱网页版，进入设置，选择账户

![image-20210802152812320](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802152812320.png)

往下翻找到 POP3……服务，确保第一项是“已开启”状态，如果不是，点击后面的开启，然后选择下面的“生成授权码”

![image-20210802152944128](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802152944128.png)

根据提示验证后，得到授权码，和抓包步骤一样，把授权码复制保存下来备用。

![image-20210802153128652](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802153128652.png)

### 三、Python 代码

代码中直接会填入打卡的地址，所以代码正常运行后，即使人不在学校，打卡也会在学校，这时候就要留意会不会穿帮了。

需要填写经纬度，可以通过百度的拾取坐标系统获取：[拾取坐标系统 (baidu.com)](https://api.map.baidu.com/lbsapi/getpoint/index.html)

![image-20210802155049310](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802155049310.png)

#### 1.日检日报

代码中的“xxx”部分都需要手动填入，其中包括上面步骤中保存的那些内容，日检日报代码中有8处需要修改

```python
import json
import logging
import requests, time, random
import datetime
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_status(self):
    if self['code'] == 0:
        return "日检日报打卡成功"
    elif self['code'] == 1:
        return "日检日报时间结束"
    elif self['code'] == -10:
        return "···JWSESSION已失效!!!"
    else:
        return "!!!未知错误!!!"

class answer:
    def __init__(self):

        self.jwsessionName = ["xxx"]  # 修改1：姓名

        self.my_sender = 'XXX'  # 修改2：发信人的邮箱账号,写自己的QQ邮箱号
        self.my_pass = 'xxx'  # 修改3：发件人邮箱授权码
        self.my_user = 'xxx'  # 修改4：收件人邮箱账号，同样写自己的

        self.api = "https://student.wozaixiaoyuan.com/heat/save.json"
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
            "seq": self.get_seq(),
            "temperature": self.get_random_temprature(),

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
    return answer().run()

```



#### 2.健康打卡

健康打卡同样有8处需要修改

```python
import json
import logging
import requests, time, random
import datetime
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
        if 0 <= current_hour <=18:
            return 0
        else:
            return 1

    def run(self):
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
    return answer().run()

```

走到这里就已经完成了一大半了，打卡的代码已经改好，接下来就是怎么让代码定时运行了，这里用到腾讯云函数

### 四、腾讯云函数

注册过程就不再赘述，注册完记得完成实名认证，这里给出腾讯云官网链接：[腾讯云(tencent.com)](https://cloud.tencent.com/)

#### 1.使用云函数

进入腾讯云先登录，搜索云函数

![image-20210802160948779](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802160948779.png)

管理控制台

![](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802161241550.png)

函数服务 → 新建

![image-20210802161459839](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210802161459839.png)

选择自定义创建，函数名称可以改一下，方便区分，这里用健康打卡做例子，由于名称不能写中文，所以就写了健康打卡的拼音缩写

![image-20210803080018644](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210803080018644.png)

往下翻，函数代码选择在线编辑，把刚刚编辑好的代码粘贴在这里

![image-20210803080356200](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210803080356200.png)

其他设置保持默认即可，然后点击完成。这样就把代码部署在腾讯云上了，可以尝试运行一下，直接点击测试按钮，立马就能收到一封邮件，提示打卡状态

![image-20210803081027997](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210803081027997.png)

![image-20210803081034094](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210803081034094.png)

#### 2.定时触发

设置定时触发之后，就可以按照自己的时间定时运行一次代码，这样就解放了双手

触发管理 → 创建触发器

![image-20210803083310441](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210803083310441.png)

触发周期选择自定义，这里要输入 Cron 表达式，健康打卡是每天一次，只要过了零点就可以打卡，所以 Cron 表达式是 0 01 00 * * * *，表示每天00:01运行一次代码；日检日报是每天三次，这里根据我们学校的时间，我写的是 0 35 6,12,19 * * * *，表示每天6:35、12:35、19:35各运行一次；其他设置保持默认即可，点击提交。

教程到这里就结束了，如果需要其他时间打卡，可以直接更改 Cron表达式，为了方便大家更改，关于 Cron 表达式的语法下面也讲解一下

![image-20210803083504283](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210803083504283.png)

#### 3.Cron表达式

Cron表达式有7个字段，以空格分割

| 第一位 | 第二位 | 第三位 | 第四位 | 第五位 | 第六位 | 第七位 |
| :----- | :----- | :----- | :----- | :----- | :----- | :----- |
| 秒     | 分钟   | 小时   | 日     | 月     | 星期   | 年     |

每一位都有一定的取值范围

| 字段 | 值                                                           | 通配符  |
| :--- | :----------------------------------------------------------- | :------ |
| 秒   | 0 - 59的整数                                                 | , - * / |
| 分钟 | 0 - 59的整数                                                 | , - * / |
| 小时 | 0 - 23的整数                                                 | , - * / |
| 日   | 1 - 31的整数（需要考虑月的天数）                             | , - * / |
| 月   | 1 - 12的整数或 JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC | , - * / |
| 星期 | 0 - 6的整数或 SUN,MON,TUE,WED,THU,FRI,SAT。其中0指星期日，1指星期一，以此类推 | , - * / |
| 年   | 1970 - 2099的整数                                            | , - * / |

举例说明：

| 日检日报 |  0   |  35  |    6，12，19    |  *   |  *   |     *      |  *   |
| :------: | :--: | :--: | :-------------: | :--: | :--: | :--------: | :--: |
|   含义   | 0秒  | 35分 | 6时，12时，19时 | 每日 | 每月 | 每星期每天 | 每年 |

| 健康打卡 |  0   |  01  |  00  |  *   |  *   |     *      |  *   |
| :------: | :--: | :--: | :--: | :--: | :--: | :--------: | :--: |
|   含义   | 0秒  | 01分 | 0时  | 每日 | 每月 | 每星期每天 | 每年 |

### 五、Q&A

最后在这里放一个问答板块，如果大家有什么问题可以在评论区提问，我会定期更新在这里

#### ·如何第一时间收到QQ邮件？

如果每次都打开邮箱网页查看打卡状态，那自然很麻烦，最简单的方法就是手机下载QQ邮箱客户端，并打开消息提醒，这样每次代码运行结束都能及时收到打卡状态。如果不想下载软件，也可以用微信的QQ邮件提醒，不过这需要一些设置：

首先确保微信和QQ号已经绑定，找到【设置】-【账号与安全】-【更多安全设置】来绑定QQ号

![image-20210803090822826](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210803090822826.png)

绑定好之后，点击微信上方的搜索，搜“QQ邮箱提醒”功能并启用，这样就可以在微信收到邮件了

![](https://gitee.com/dominic548/picgo/raw/master/Typora/image-20210803091352067.png)
