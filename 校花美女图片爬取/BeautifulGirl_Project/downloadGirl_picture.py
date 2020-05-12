"""此.py用于下载美女图片"""
import json
import os
import requests
from BeautifulGirl_Project.utils import useragentutil


"""将json数据转成python基本数据类型,并返回 """
def load_Json_to_data(filePath):
    # 将json数据转成python基本数据类型,并返回
    # 打开文件
    file = open(filePath,"r",encoding="utf-8")
    # 加载数据
    girlAll_list = json.load(file)
    # 关闭文件
    file.close()
    return girlAll_list


"""为每个美女创建一个文件夹，名就是她的名字"""
def createGirlDir(girlAll_list):
    # 创建一个Picture文件夹
    pictureDir = "./GirlPicture"
    if not os.path.exists(pictureDir):
        os.makedirs(pictureDir)
    for list in girlAll_list:
        for elements_dict in list:
            # 美女名字
            girlName = elements_dict["girlName"]
            if not os.path.exists((pictureDir+"/"+girlName)):
                os.makedirs((pictureDir+"/"+girlName))
    print("文件夹创建成功")


def downloadPicture(girlAll_list):
    # 记录图片的张数
    i = 0
    for list in girlAll_list:
        for elements_dict in list:
            # 美女名字
            girlName = elements_dict["girlName"]
            # 获取美女图片链接
            girlImg_url = elements_dict["girlImg_url"]
            # 获取美女图片
            ImgContent = requests.get(girlImg_url,verify=False,headers=useragentutil.get_headers())
            # 打开文件夹
            filePath = "./GirlPicture"+"/"+girlName+"/1."+girlName+".jpg"
            file = open(filePath,"wb")
            file.write(ImgContent.content)
            # 关闭文件夹
            file.close()
            i = i+1
            print("第%d张图片已经下载成功"%i)


def main():
    filePath = "./file/girlInfor.json"
    # 读取数据
    girlAll_list = load_Json_to_data(filePath)
    # 创建文件夹
    createGirlDir(girlAll_list)
    # 下载图片
    downloadPicture(girlAll_list)


if __name__ == '__main__':
    main()
