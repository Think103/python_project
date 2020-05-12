import requests
import os
from BeautifulGirl_Project.utils import useragentutil

"获取待爬取的网页信息"
def getHtml(url):
    html = requests.get(url,verify=False,headers=useragentutil.get_headers())
    # 处理乱码问题
    htmlContent = html.content.decode("gbk")
    return htmlContent

"""先将该首页的（第一页)数据保存起来"""
def save_Html_data(htmlContent):
    # 创建一个file文件夹
    dirName = "file"
    if not os.path.exists(dirName):
        os.makedirs(dirName)
    # 打开一个文件，没有就创建
    # file = open("./file/htmlContent.html","w",encoding="utf-8")
    file = open("./file/girlIntroduce_info.html", "w", encoding="utf-8")
    # 写入数据
    file.write(htmlContent)
    # 关闭文件
    file.close()
    print("文件保存成功")

def main():
    # url = "http://www.xueshengmai.com/list-1-0.html"
    details_url = "http://www.xueshengmai.com/p-1-2092.html"
    htmlContent = getHtml(details_url)
    save_Html_data(htmlContent)

if __name__ == '__main__':
    main()