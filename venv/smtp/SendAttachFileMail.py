#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="155113995@qq.com"    #用户名
mail_pass="ecfjqngdmspabhbg"   #口令
sender="155113995@qq.com"
receivers=["suchangcheng1984@163.com"]
htmlMsg='''
<p>Python HTML  邮件发送测试...</p>
<p><a href="http://www.banmachewu.com">这是一个链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1" style="width:500;height:200"></p>
<p>网络链接图片演示：</p>
<p><img src="http://www.banmachewu.com/images/bm-pc-top-1.jpg" style="width:500;height:200"/></p>
'''
# message=MIMEText(htmlMsg,"html","utf-8")
#创建一个带附件的实例
message = MIMEMultipart()
message["From"]=_format_addr("苏长城<155113995@qq.com>")
message["To"]=_format_addr("阿城<suchangcheng1984@163.com>")
subject = 'Python SMTP HTML邮件测试'
message['Subject'] = Header(subject, 'utf-8')
#构造邮件正文内容
message.attach(MIMEText(htmlMsg,"html","utf-8"))
# 构造附件1，添加word文档
att1 = MIMEApplication(open('E:/梦网平台API V5.3接口说明.docx', 'rb').read())
att1.add_header('Content-Disposition', 'attachment', filename="梦网平台API V5.3接口说明.doc")
message.attach(att1)
#构造附件2，添加Excel
att2 = MIMEApplication(open('E:/区域2018.xlsx', 'rb').read())
att2.add_header('Content-Disposition', 'attachment', filename="区域2018.xlsx")
message.attach(att2)
#Html文档中添加图片
fp = open('E:/滴滴合作图片.jpg', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

smtpObj=smtplib.SMTP()
smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
smtpObj.login(mail_user, mail_pass)

smtpObj.sendmail(sender,receivers,message.as_string())
print("邮件发送成功")
smtpObj.quit()