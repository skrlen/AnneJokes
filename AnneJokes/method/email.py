# -*-coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.core.mail import EmailMessage


def send_mails(title, content, to: list):
    """
    一封邮件发给多人
    :param title:
    :param content:
    :param to:
    :return:
    """
    try:
        send_mail(title, content, settings.DEFAULT_FROM_EMAIL, to)
        return
    except Exception as e:
        return e


def send_html_mail(title, content, to: list):
    try:
        msg = EmailMessage(title, content, "AnneJoke<skrlen@126.com>", to)
        msg.content_subtype = "html"
        msg.send()
    except Exception as e:
        print(e)


def send_mass_mails(content: tuple, **args):
    """
    发送多封邮件时，必须以元组的形式传入，例如
    (('title1', content1, settings.DEFAULT_FROM_EMAIL,[123@qq.com, 321@qq.com]), ('title2', content2, settings.DEFAULT_FROM_EMAIL,[123@qq.com, 321@qq.com]))
    :param content:
    :return:
    """
    try:
        send_mass_mail(content)
        return
    except Exception as e:
        return e


# def send_mail(email, b64_str, id, subject):
#     smtpserver = 'smtp.126.com'
#     username = 'skrlen@126.com'
#     password = 'Ren19980524.'
#     sender = '安妮网--二货聚集地'
#     receiver = email
#
#     msg = MIMEText('我们为了确定是您本人在操作，请验证您的身份<a href="121.36.249.255/activate/?data=%s&id=%s">点击激活</a>，如果您未订阅，此信息请忽略\r ' % (b64_str, id), 'html', 'utf-8')
#
#     msg['Subject'] = subject
#
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver)
#         smtp.login(username, password)
#         smtp.sendmail(sender, receiver, msg.as_string())
#         smtp.quit()
#         return True
#     except Exception as e:
#         print(e)
#         return False
