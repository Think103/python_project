"""使用浏览器自动化工具来加载页面，获取动态的页面数据"""
from selenium import webdriver
import time

#返回浏览器对象
def getBrowser_object():
    # （1）获得浏览器对象；    -->Chrome/PhantomJS
    chrome_path = r"D:\QQ垃圾文件\4.软件工具(2)\4.软件工具(2)\Selenium驱动文件\Selenium驱动文件\chrome驱动文件\chromedriver.exe"
    browser = webdriver.Chrome(chrome_path)
    # 设定窗口为最大
    browser.maximize_window()
    # （2）发送请求；  --get()
    # browser.get(url)
    return browser




