# encoding: utf-8
import time,os
from bs4 import BeautifulSoup
import smtplib #smtp服务器
from email.mime.text import MIMEText #邮件文本
from email.header import Header
two = False #切换获取页面方法True:undetected_chromedriver  Flase:request

dm=[('杏吧免V仓','sex8'),('黄车一仓','hsck822'),('快播四仓','2028d'),('91PORNY仓','91porny'),('网红爆料仓','51cg1'),('欧美18禁仓','xxx18'),('SGPAI高清仓','sgpai'),('日本超清','cn532'),('sae8资源仓','sae8'),('黄车七仓','yuexia6')]
url1="https://bbs.672z.org/2048/"
url3="thread.php?fid=291&woo={}"
path='./'
#('综合速播仓','nv002'),

def send_email(subject="chinadaily推送提醒",content="chinadaily头条，请查看",recver="xingchen035@live.com"):
    # 第三方 SMTP 服务
    mail_host="smtp.office365.com"  #设置服务器
    mail_user="xingchen035@live.com"    #用户名
    mail_pass="97JUAN1011xc"   #口令 
    sender = 'xingchen035@live.com'
    receivers = recver # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj = smtplib.SMTP(mail_host,port=587) 
    smtpObj.connect(mail_host,port=587)    # 25 为 SMTP 端口号
    # 必须先登录
    smtpObj.ehlo() # 用户认证 
    smtpObj.starttls() # 明文通信协议的扩展，能够让明文的通信连线直接成为加密连线（使用SSL或TLS加密），而不需要使用另一个特别的端口来进行加密通信，属于机会性加密
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功')

def web_fw(url):
    if two:
        global onetime   
        try:
            browser.get(url)
            if onetime:
                time.sleep(30)
                onetime = False
            html=browser.page_source
            return html
        except Exception as e:
            print(e)
    #browser.quit()
    else:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'}
        #try:
        html = request.Request(url=url,headers=headers)
        res = request.urlopen(url=html,timeout=30)
        return res
        #except Exception as e:
        #    print(e)
        #    return False

def savem3(url2,fn,dm_name,x='a'):
    soup = BeautifulSoup(web_fw(url2),"html.parser")#,from_encoding="utf-8"
    #links = soup.find_all('div',class_='colVideoList')
    links = soup.find_all('a',class_='text-truncate')
    f=open(fn,x, encoding='utf-8')
    #if x=='w':   
    f.write(dm_name+',#genre#\n')
    for link in links:
        try:
            cont = link['title']
            link=url1+link['href']
            soup = BeautifulSoup(web_fw(link),"html.parser")#,from_encoding="utf-8")
            link = soup.iframe['src']
            if link.find('http')==0:
                pass
            else:
                link=url1+link
            soup = BeautifulSoup(web_fw(link),"html.parser")
            wer= str(soup.body.select('script')[0])
            wer=wer[wer.find("src:'")+5:wer.find("poster:")]
            wer=wer[:wer.find("',")]
            if wer.find('http')==0:
                pass
            else:
                wer='https://bbs.672z.org'+wer
            link = cont+','+wer
            print(link)
            f.write(link+'\n')
        except Exception as e:
            print(e)
            continue
    f.close()
    return False

sexname=''
if two:
    import undetected_chromedriver as uc
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('–headless')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--profile-directory=Default")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-plugins-discovery")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument('--no-first-run')
    chrome_options.add_argument('--no-service-autorun')
    chrome_options.add_argument('--no-default-browser-check')
    chrome_options.add_argument('--password-store=basic')
    chrome_options.add_argument('--no-sandbox')
    browser = uc.Chrome(options=chrome_options, version_main=113)
    browser.delete_all_cookies()
    onetime = True
else:
    from urllib import request
    

l=os.listdir(path)
zt='w'
for dm_one in dm:
    filename = 'sexlist.txt'
    url=url1+url3.format(dm_one[1])
    print(dm_one[0],'going......')
    savem3(url,path+filename,dm_one[0],zt)
    print(dm_one[0],'ok')
    zt='a'
    
send_email(subject="更新提示",content="更新成功")

if two:
    browser.quit()


