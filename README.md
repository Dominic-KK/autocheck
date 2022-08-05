# 🌹我可以不在校园🌹

## :loudspeaker:公告

:newspaper:**VERSION 4.0**

- 由于业务更新，旧的版本逐渐无法使用，至此请全部转到本版本。

- 如有学习之前版本的需求，可以点击分支或标签。

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/08/051946-c5f.png" alt="image-20220805194627169" style="zoom: 67%;" />

- 学习过程中有任何疑问，请优先从文档最后的`Q&A`寻找答案，两位作者都有自己的事情，不一定能随时回复:smile:。

- 作者DominicKK  [QQ 3330900358:link:](tencent://AddContact/?fromId=45&fromSubId=1&subcmd=all&uin=3330900358&[website=www.oicqzone.com](http://website/%3Dwww.oicqzone.com/))

- 作者SmallWay  [QQ 1097123142:link:](tencent://AddContact/?fromId=45&fromSubId=1&subcmd=all&uin=1097123142&[website=www.oicqzone.com](http://website/%3Dwww.oicqzone.com/))

- 欢迎关注我的个人博客：[DominicKK - 博客园](https://cnblogs.com/dominickk/):link:

- 友链：[小白 (smallway) - Gitee.com](https://gitee.com/smallway):link:

<p><strong>- 2022.08.05 20:00 -</strong></p>



---

## :bell:**特别声明**

:heavy_exclamation_mark:  本仓库发布的文章及代码等全部内容，仅用于测试和学习研究，禁止用于商业用途，作者不保证其准确性、完整性以及合法性，请使用者依个人情况自行合理判断。

:heavy_exclamation_mark:  因私自用于商业或非法用途，所产生的后果由使用者自负，均与作者无关。

:heavy_exclamation_mark:  本仓库项目所有文章及资源，除引用第三方内容外，禁止任何自媒体进行任何形式的转载、发布。

:heavy_exclamation_mark:  若任何单位或个人认为该仓库内容可能存在侵犯其权力的行为，应及时通知作者并提供身份证明、所有权证明，作者在收到之后将在第一时间删除相关内容。

:heavy_exclamation_mark:  疫情反复均属未知，请保护好自己，健康生活，认真打卡。

:o:  无论您以任何途径、任何方式，一旦您一经下载或使用本仓库内容，即代表您  :white_check_mark:`已接受`  以上声明，请知悉。

---

[TOC]

---

 本教程灵感来源于生活。

**《食用前必读.txt》**真的很重要，**建议阅读**（不听作者言，吃亏在眼前）。

 **所有文件以及相关代码已在文件列表上传，下载即可使用**

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-a23.png" alt="Untitled" style="zoom:67%;" />

## :globe_with_meridians:Fiddler 抓包工具

### 1.安装和配置

安装包下载：Fiddler 安装包和 Fiddler 证书生成器

蓝奏云链接：https://dominic.lanzouq.com/iKszLzyh5gh :link:

下载后解压，先双击 `FiddlerSetup.exe` 进行安装，另一个是证书生成器，暂时不用。

打开 Fiddler ，点击工具栏中的 `Tools` → `Options`

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-55f.png" alt="Untitled" style="zoom:67%;" />

点击 `HTTPS` 标签，勾选框住的三项，然后点击右边的 `Actions`，选择第二项，会弹出一个弹窗，点击确定，之后点击 `OK` 完成设置

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-208.png" alt="Untitled" style="zoom:67%;" />

这时会发现桌面上多了一个证书文件（如下图），接下来马上会用到

![Untitled](https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-a6b.png)

打开电脑上任何一个浏览器，在这里我用的是 win10 自带的 Edge，打开设置，找到`证书管理`，实在找不到也可以直接搜索

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-f29.png" alt="Untitled" style="zoom:67%;" />

点击`管理证书`，点击`导入`进入证书导入向导

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-5bb.png" alt="Untitled" style="zoom:67%;" />

点击`下一页`继续

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-142.png" alt="Untitled" style="zoom:67%;" />

点击`浏览`，选择要导入的文件

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-e23.png" alt="Untitled" style="zoom:67%;" />

在桌面找到刚刚导出的证书文件，点一下证书文件，选择`打开`

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-d6a.png" alt="Untitled" style="zoom:67%;" />

之后一直点击`下一步`，直到完成证书导入。到这里配置工作基本完成，可以进行抓包了，刚刚导出在桌面的证书文件也可以删除

### 2.*抓取重要信息（非必选）

在本版本中，提供了所需的信息，（如不嫌弃）可以直接使用。

接下来从微信电脑端打开我在校园小程序，然后打开日检日报或者健康打卡，会发现 Fiddler 中显示了很多内容，我们找到`gw.wozaixiaoyuan.com`这一行（图是旧图，大概就这么个意思，看懂就好），双击打开，在右边选择`Headers`标签，复制 `User-Agent`、`Referer`。

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-d2c.png" alt="Untitled" style="zoom:67%;" />

如果抓包失败，请参考最下面的`Q8：Fiddler抓包失败`以及`Q9：抓不到小程序`

复制的内容可以发给你的工具人小伙伴，或者你的小号，总之先保留下来备用。

### 3.*抓取图片（非必选）

最新的健康打卡存在上传图片的情况，如果检查并不是很严格，可以选择不上传图片。

如果需要上传，目前的解决方案如下：

由于目前打开系统有所限制，故需要使用fiddler抓取手机端的网络包，关于这一点网上的教程很多，本文在最后也提供了可用的参考：`Q10.fiddler手机抓包`

使用手机打卡，准备好需要上传的图片（一张图片用一年），有必要的话可以p掉图片上的时间，点击打卡之后，会在fiddler中看到如图信息，在下方切换到`JSON`栏，复制`data`后面的链接，这就是需要的图片了，之后填入代码中的对应地方。

![image-20220805173541701](https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/08/051735-d11.png)

## :mailbox:QQ邮箱

### 获取授权码

用QQ邮箱发件也需要登录，不是用账号密码，而是授权码（更安全），接下来获取授权码

进入QQ邮箱网页版，进入`设置`，选择`账户`

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-9b5.png" alt="Untitled" style="zoom:67%;" />

往下翻找到 `POP3/SMTP服务`，确保第一项是`已开启`状态，如果不是，点击后面的开启，然后选择下面的`生成授权码`

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-3ed.png" alt="Untitled" style="zoom:67%;" />

根据提示验证后，得到授权码，和抓包步骤一样，把授权码复制保存下来备用。

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-ff9.png" alt="Untitled" style="zoom:67%;" />

## :snake:Python 代码

### 1.经纬度获取

:laughing:嗨害！不需要啦！

### 2.打卡题目

在代码文件中，预设了基本通用的题目答案，但打卡题目不一定都相同，若和下图的题目相同，则无需修改代码。**否则一定要修改代码，请[QQ联系作者](tencent://AddContact/?fromId=45&fromSubId=1&subcmd=all&uin=3330900358&website=www.oicqzone.com):link:。**

### 3.日检日报

代码中的“xxx”部分都需要手动填入，其中包括上面步骤中保存的那些内容，**代码文件已上传至文件列表**，**下载即可编辑使用**。

### 4.健康打卡

代码中的“xxx”部分都需要手动填入，其中包括上面步骤中保存的那些内容，**代码文件已上传至文件列表**，**下载即可编辑使用**。

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/08/051741-80a.png" alt="image-20220805174126663" style="zoom:67%;" />

### 5.定位签到

定位签到由作者 **[小白](https://gitee.com/smallway)**:link: 协助完成，点击链接跳转：[我在校园定位签到](https://gitee.com/smallway/autosign):link:。

## :chart_with_upwards_trend:阿里云函数

注册过程就不再赘述，注册完记得完成实名认证，这里给出阿里云官网链接：[阿里云(aliyun.com)](https://www.aliyun.com/) :link:

### 1.使用云函数

进入阿里云先登录，搜索`函数计算FC`

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-074.png" alt="Untitled" style="zoom:67%;" />

开通并进入管理界面

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-3b3.png" alt="Untitled" style="zoom:67%;" />

创建一个新服务，名称自定义，其他设置默认即可

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-f01.png" alt="Untitled" style="zoom:67%;" />

进入到刚刚创建的服务，创建一个新函数

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-edb.png" alt="Untitled" style="zoom:67%;" />

按照图示进行设置

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-de2.png" alt="Untitled" style="zoom:67%;" />

这里尤其注意：一定要选择**弹性实例**，涉及到免费额度（`Q6`会做解释）

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-c9d.png" alt="Untitled" style="zoom:67%;" />

创建完成后双击打开代码文件，将上面修改好的代码粘贴进去

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-f77.png" alt="Untitled" style="zoom:67%;" />

部署并调用，会收到邮件

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-01f.png" alt="Untitled" style="zoom:67%;" />

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-643.png" alt="Untitled" style="zoom:67%;" />

### 2.定时触发

设置定时触发之后，就可以按照自己的时间定时运行一次代码，这样就解放了双手

触发器管理 → 创建触发器

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-b20.png" alt="Untitled" style="zoom:67%;" />

触发周期选择自定义，这里要输入 Cron 表达式，健康打卡是每天一次，只要过了零点就可以打卡，所以 Cron 表达式是 `CRON_TZ=Asia/Shanghai 0 01 00 * * *`，表示每天00:01运行一次代码；日检日报是每天三次，这里根据我们学校的时间，我写的是 `CRON_TZ=Asia/Shanghai 0 35 6,12,19 * * * *`，表示每天6:35、12:35、19:35各运行一次；其他设置保持默认即可，点击提交。

教程到这里就结束了，如果需要其他时间打卡，可以直接更改 Cron表达式，为了方便大家更改，关于 Cron 表达式的语法在下面的`Q&A`中也讲解一下

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-1aa.png" alt="Untitled" style="zoom:67%;" />

## :wheelchair:Q&A

最后在这里放一个问答板块，如果大家有什么问题可以在评论区提问（评论区可能回复不及时，推荐使用qq联系），我会定期更新在这里

### ！**重要**：账号或密码错误

1. 账号密码登录，代码有时候会报密码错误，如果出现错误，可以做一次修改密

码操作，新密码与旧密码可以一样

2. 当然，如果还是报错，继续修改密码，（新旧密码可以相同，这里没有检测机制
   ，所以只改密码，不用改代码里的密码），直到成功为止
3. 如果手机端进我在校园发现需要重新登陆，这时候如果用账号密码登录了，那么
   代码那边也会报错误，所以记得及时再改密码
4. 这个目前没有解决方案，只能说没什么特别的事（比如签到）尽量不去开小程序

### 1.Cron表达式

Cron表达式有7个字段，以空格分割

| 字段                                                         | 区值范围和描述                                               |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| [CRON_TZ](https://www.notion.so/CRON_TZ-3e67bdfa11094dea80356a482bea3473) | 这一部分为可选，不设置代表使用 UTC 时间。例如：CRON_TZ=Asia/Shanghai 代表北京时间。 |
| [秒](https://www.notion.so/145e51a8e0f244299fdf21f8ed20bee9) | 表达式中的第一位，取值范围为 0～59，不允许设置特殊字符。     |
| [分](https://www.notion.so/72beba1eefc64105ad00474c82c52431) | 表达式中的第二位，取值范围为 0～59，允许设置特殊字符 **, - \* /**。 |
| [小时](https://www.notion.so/d7a6f7f99f6249c2bdebf4ac59640dda) | 表达式中的第三位，取值范围为 0～23，允许设置特殊字符 **, - \* /**。 |
| [日期](https://www.notion.so/d2ca30c9d7c54e6a98507ece51bf8811) | 表达式中的第四位，取值范围为 1～31，允许设置特殊字符 **, - \* ？/**。 |
| [月份](https://www.notion.so/c0bee3b95754492a87a7a061ec40cd18) | 表达式中的第五位，取值范围为 1～12 或 JAN～DEC，允许设置特殊字符 **, - \* /**。 |
| [星期](https://www.notion.so/82391ac8f578427fa06c94b3ffe7f246) | 表达式中的第六位，取值范围为 0～6 或 MON～SUN，允许设置特殊字符 **, - \* ?**。 |

特殊字符说明

| 特殊字符                                                    | 说明                                                         |
| :---------------------------------------------------------- | :----------------------------------------------------------- |
| [*](https://www.notion.so/4b52bffb10cf485580e3cec7d928fa08) | 表示任一或每一。例如：分钟字段 * 表示每分钟。                |
| [,](https://www.notion.so/279d822ed86940838ce09388f1453bdd) | 表示列表值。例如：星期字段中 MON,WED,FRI 表示星期一，星期三和星期五。 |
| [-](https://www.notion.so/2a3488b840f745eb9f7c2eb453eb9313) | 表示一个范围。例如：小时字段中 10-12 表示 UTC 时间从10点到12点。 |
| [?](https://www.notion.so/eaa42f2c875847c096fb1cf97673b0ec) | 表示不确定的值。例如：如果指定了一个特定的日期，但您不在乎它是星期几，那么在星期字段中就可以使用问号这个特殊符号。 |
| [/](https://www.notion.so/2a2dc79f4d9f4c30b924360fa5520837) | 表示一个值的增加幅度，n/m表示从n开始，每次增加m。例如：在分钟字段中：3/5表示从3分钟开始，每隔5分钟执行一次。 |

示例

| 示例                                                         | Cron 表达式 （UTC 时间）  | Cron 表达式（北京时间）                          |
| :----------------------------------------------------------- | :------------------------ | :----------------------------------------------- |
| [每天12:00调度函数](https://www.notion.so/12-00-56103a5bd0234c568c6d99256a252c8a) | 0 0 4 * * *               | CRON_TZ=Asia/Shanghai 0 0 12 * * *               |
| [每天12:30调度函数](https://www.notion.so/12-30-e9fad035547c4a6fa410fd7b2ac7b49b) | 0 30 4 * * *              | CRON_TZ=Asia/Shanghai 0 30 12 * * *              |
| [每小时的26分，29分，33分调度函数](https://www.notion.so/26-29-33-354008990af248bf9f676fc71d37753f) | 0 26,29,33 * * * *        | CRON_TZ=Asia/Shanghai 0 26,29,33 * * * *         |
| [周一到周五的每天12:30调度函数](https://www.notion.so/12-30-2a58673b71c744928010d80f1c49060e) | 0 30 4 ? * MON-FRI        | CRON_TZ=Asia/Shanghai 0 30 12 ? * MON-FRI        |
| [周一到周五的每天12:00～14:00每5分钟调度函数](https://www.notion.so/12-00-14-00-5-c583dc94aaa7429793ffa6cf8c758b8a) | 0 0/5 4-6 ? * MON-FRI     | CRON_TZ=Asia/Shanghai 0 0/5 12-14 ? * MON-FRI    |
| [一月到四月每天12:00调度函数](https://www.notion.so/12-00-7d354ee122b94e248fa7c5ea7a160ff3) | 0 0 4 ? JAN,FEB,MAR,APR * | CRON_TZ=Asia/Shanghai 0 0 12 ? JAN,FEB,MAR,APR * |

### 2.如何第一时间收到QQ邮件

如果每次都打开邮箱网页查看打卡状态，那自然很麻烦，最简单的方法就是手机下载QQ邮箱客户端，并打开消息提醒，这样每次代码运行结束都能及时收到打卡状态。如果不想下载软件，也可以用微信的QQ邮件提醒，不过这需要一些设置：

首先确保微信和QQ号已经绑定，找到【设置】-【账号与安全】-【更多安全设置】来绑定QQ号

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-833.png" alt="Untitled" style="zoom:67%;" />

绑定好之后，点击微信上方的搜索，搜“QQ邮箱提醒”功能并启用，这样就可以在微信收到邮件了

<img src="https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-d18.png" alt="Untitled" style="zoom:67%;" />

### 3.下载了QQ邮箱APP后，邮箱公众号收不到邮箱消息了

进入qq邮箱app，点开头像，选择新邮件提醒，拉到下面选择你的qq邮箱账号，然后关闭下面的仅在qq邮箱客户端提醒，然后公众号就可以正常接收信息了。

### 4.errorcode

若出现类似于`{"errorCode":1,"errorMessage":"Traceback (most recent call last):\n ......,"statusCode":443}`的错误，可尝试重新建一个云函数，即重复`步骤四`

### 5.为什么不用”喵提醒“、”pushplus 推送加“等公众号作为打卡提醒方式

原因只有一个：麻烦。

用过的同学应该知道，这些提醒类公众号都有一个共性：需要发送激活48小时消息，也就是发送激活消息后才能收到提醒，这是为什么？这并不是公众号博主为了广告效应或是其他，而是由于公众号的后台限制：公众号后台无法回复用户超过48小时的消息（参考官方解释：[客服帐号管理 | 微信开放文档 (qq.com)](https://developers.weixin.qq.com/doc/offiaccount/Message_Management/Service_Center_messages.html) :link:）；那么自然无法发送打卡成功的提醒。

但是，如果真的喜欢用微信作为提醒渠道，可以参考上面`Q2：如何第一时间收到QQ邮件`即可

### 6.如何将腾讯云函数的代码转移到阿里云函数计算FC

参考上文中使用阿里云函数的步骤之后，将腾讯云的代码复制到阿里云，修改代码中的`main_handler`为`handler` ，具体操作：在编辑器中按下键盘上的`ctrl + H` 调出查找替换，点击全部替换；之后填写触发器Cron表达式也应当注意两边的差异，详情参考`Q1：Cron表达式`

![Untitled](https://dominickk.oss-cn-hangzhou.aliyuncs.com/typora/2022/06/031900-9f9.png)

### 7.阿里云函数计算FC免费额度

详情参考[官方帮助文档](https://help.aliyun.com/document_detail/54301.html) :link:

**注意：**免费额度仅适用**弹性实例**，并且函数使用过程产生的**公网出流量不在免费额度中**，但其费用极小，几乎可以忽略，如有产生相关费用，支付即可（几毛几分钱没有人会特别在意的吧）

**免费额度**

函数计算每月为您提供一定的免费额度（每月约46元，年度总计约552元）。您的阿里云账户与RAM用户共享每月免费的调用次数和执行时间额度。免费额度不会按月累积，在下一自然月的起始时刻，即01号零点，会清零然后重新计算。

**公网出流量**

函数计算根据每月使用的公网出流量总和计费。公网出流量费用=函数内数据传输流量×流量单价+函数请求响应流量×流量单价+CDN回源流量×流量单价。

- 函数内数据传输流量：通过函数访问公网，函数向公网发起网络请求（Request）时所产生的流量。
- 函数请求响应流量：通过公网调用函数，函数执行完成，返回响应（Response）时所产生的流量。
- CDN回源流量：以函数计算作为CDN的源站，CDN回源时所产生的流量。

| 计量项                                                       | 单价      | 免费额度（每月） |
| :----------------------------------------------------------- | :-------- | :--------------- |
| [函数内数据传输流量](https://www.notion.so/9b7bf8c58e3e43369cec66bdb9ab61d0) | 0.80元/GB | 无               |
| [函数请求响应流量](https://www.notion.so/5b1cce3f51424bda9efc112a3a9e91a4) | 0.50元/GB | 无               |
| [CDN回源流量](https://www.notion.so/CDN-6804ff0308784088a2a15b7d15f14deb) | 0.50元/GB | 无               |

### 8.Fiddler抓包失败

**卸载证书 - 重启电脑 - 重装证书**

**卸载证书 - 重启电脑 - 重装证书**

**卸载证书 - 重启电脑 - 重装证书**

抓包失败的原因是证书安装失败，需要重装，参考：[Fiddler证书清除并重新配置](https://blog.csdn.net/w6082819920919/article/details/112174650):link:

**注意**：卸载干净后一定重启电脑，再重装！

**卸载证书 - 重启电脑 - 重装证书**

**卸载证书 - 重启电脑 - 重装证书**

**卸载证书 - 重启电脑 - 重装证书**

### 9.抓不到小程序

是由于小程序的更新，可以参考：[fiddler抓包PC微信小程序失败解决方案](https://www.jianshu.com/p/f87512ed7b21):link:

该方案只可以临时使用，下次抓包可能还需要处理一次

### 10.fiddler手机抓包

推荐使用安卓手机，抓包时一定把电脑和手机连接同一个wifi

参考：[使用Fiddler实现手机抓包 - EastJason - 博客园 (cnblogs.com)](https://www.cnblogs.com/eastnapoleon/p/14654451.html):link:





