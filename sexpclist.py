from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time,os
from bs4 import BeautifulSoup



url1="https://2048.biz/"
url3="thread.php?fid=291&woo=100vod"
path='./'

# 配置浏览器（Chrome）
options = webdriver.ChromeOptions()
# 可选：无头模式（后台运行，无需打开浏览器界面）
options.add_argument('--headless')
# 创建驱动并指定路径和选项
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
zt='w'
count=0

def get_source(url):
    driver.get(url)
    html_source=driver.page_source
    soup = BeautifulSoup(html_source,"html.parser")#,from_encoding="utf-8"
    return soup



def savem3(url2,fn,x='a'):
#     driver.get(url2)
#     html=driver.page_source
#     soup = BeautifulSoup(html,"html.parser")#,from_encoding="utf-8"
#        links = soup.find_all('div',class_='colVideoList')
    soup = get_source(url2)
    links = soup.find_all('div',class_='colVideoList')
#        print(links)#测试用
#        if x=='w':   
#        f.write(name+',#genre#\n')
    m3u=""
    m3u+=name+',#genre#\n'
    for link in links:
        time.sleep(2)
#           print("名字：",link.a[0],"链接：",link.a['href'])
        try:
            cont = link.span.text
            link=url1+link.a['href']
#             driver.get(link)
#             html=driver.page_source
#             soup = BeautifulSoup(html,"html.parser")#,from_encoding="utf-8")
            soup = get_source(link)
            link = soup.iframe['src']
            cont = soup.h1.text
            if link.find('http')==0:
                pass
            else:
                link=url1+link
#             driver.get(link)
#             html=driver.page_source
#             soup = BeautifulSoup(html,"html.parser")
            soup = get_source(link)
            wer= str(soup.body.select('script')[2])
            wer=wer[wer.find('"src":')+8:wer.find('.m3u8')+5]
            if wer.find('http')==0:
                pass

            else:
                wer=url1+wer
            m3u += cont+','+wer+'\n'
#             print("名字：",cont,"链接：",wer)#测试用
        except Exception as e:
            print(e)
            continue
    print(m3u)    
    f=open(fn,x, encoding='utf-8')
    f.write(m3u)
    f.close()





# 打开目标网页
driver.get(url1+url3)

try:
    # 等待按钮可见（最长 10 秒）
    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//p[@class='enter-btn'][1]")  # 定位第一个按钮
        )
    )
    # 点击按钮
    button.click()
    print("按钮点击成功！")
    # 继续其他操作（如输入账号密码或跳转页面）
    filename = 'sexlist.txt'
    time.sleep(5)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source,"html.parser")
    linksall = soup.find_all('a',style='display: block;')
    for linkall in linksall:
        name=linkall.text.strip()
        linkall=url1+linkall['href']
        if count==0:
            zt="w"
        else:
            zt="a"
        savem3(linkall,path+filename,zt)
        count+=1
except Exception as e:
    print(f"点击失败或元素未找到: {e}")
finally:
    # 关闭浏览器
    driver.quit()
    pass  # 注释掉 quit() 可保持浏览器页面打开以便观察结果

# 如需继续操作（如填写信息或点击其他按钮），在此添加代码


#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39'}
#        try:
#html = request.Request(url=url1,headers=headers)
#res = request.urlopen(url=html,timeout=30)
#soup = BeautifulSoup(res,"html.parser")
#print(soup)

