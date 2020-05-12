"""此.py文件是用来爬取美女的个人信息的"""
from BeautifulGirl_Project import downloadGirl_picture
from BeautifulGirl_Project.utils import save_ListData_to_json as save
import os
import requests
from BeautifulGirl_Project.utils import useragentutil
import lxml.html


"""该函数：用于获取美女的详情链接，并于列表形式返回"""
def getGirl_detatils_url_list(girlAll_info):
    # 定义一个大列表
    girlDetails_url_list = []
    for list in girlAll_info:
        for elements_dict in list:
            # 定义一个字典，用来存放美女信息
            girlDetails_url_dict = {}
            # 美女名字
            girlName = elements_dict["girlName"]
            # 详情链接
            girlDetails_url = elements_dict["girlDetails_url"]
            girlDetails_url_dict["girlName"] = girlName
            girlDetails_url_dict["Details_link"] = girlDetails_url
            # 加入到列表中
            girlDetails_url_list.append(girlDetails_url_dict)
    return girlDetails_url_list


"""该函数：用于保存每个校花的详细资料，用txt文本格式"""
def create_Introduce_txt(girlName,detailsContent_list):
    fileDir = "./GirlInformation"
    if not os.path.exists(fileDir):
        os.makedirs(fileDir)
    fileName = girlName+"个人资料"
    # 打开文件
    file = open(fileDir+"/"+fileName+".txt","a",encoding="utf-8")
    for str in detailsContent_list:
        # 写入数据
        file.writelines(str+"\n")
    # 关闭文件
    file.close()
    # print("数据写入成功")



def getGirl_introduce(girlDetail_url_list):
    i = 0
    for dict in girlDetail_url_list:
        # 美女名字
        girlName = dict["girlName"]
        # 美女详情链接
        girlDetail_link = dict["Details_link"]
        # 获取详情的网页内容
        htmlContent = requests.get(girlDetail_link,verify=False,headers=useragentutil.get_headers()).content.decode("gbk")
        # 获取解析器
        metree = lxml.html.etree
        # 获取解析器对象
        parse = metree.HTML(htmlContent)
        # 开始解析网页内容，获取美女详情信息
        detailsContent_list = parse.xpath("//div[@class='infocontent']/p/span/text()")
        # 用于填充没有爬取到的美女信息
        lessContent_list = parse.xpath("//*[ @ id = 'post']/div[1]/div[1]/div[4]/table/tbody/tr[5]/td[2]/text()")
        # 以下三句，只是用来填充无法获取到详细信息时的文本信息
        schoolName = "学校:"+lessContent_list[0]
        lessContent_list[0] = girlName
        lessContent_list.append(schoolName)
        # 判断detailsContent_list是否为空
        if detailsContent_list:
            # 创建文本
            create_Introduce_txt(girlName, detailsContent_list)
        else:
            # 为空，填充基本信息
            # 创建文本
            create_Introduce_txt(girlName, lessContent_list)
        # 用来记录下载数
        i = i + 1
        print(i)

def main():
    filePath = "./file/girlInfor.json"
    # 读取数据
    girlAll_info = downloadGirl_picture.load_Json_to_data(filePath)
    # 从美女信息中获取详情地址
    girlDetails_url_list = getGirl_detatils_url_list(girlAll_info)
    # 将美女详情地址的数据保存在json中
    girlDetail_Json_path = "D:/python练习/校花美女图片爬取/BeautifulGirl_Project/file/girlDetail_url.json"
    save.save_Data_to_json(girlDetail_Json_path,girlDetails_url_list,"w")
    girlDetail_url_path = "./file/girlDetail_url.json"
    # 读取数据
    girlDetail_url_list = downloadGirl_picture.load_Json_to_data(girlDetail_url_path)
    # 获取美女资料
    getGirl_introduce(girlDetail_url_list)
    print("程序已走完")

if __name__ == '__main__':
    main()