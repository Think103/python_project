""""该.py是爬取每个美女的生活照"""
from BeautifulGirl_Project import downloadGirl_picture
import requests
from BeautifulGirl_Project.utils import useragentutil
import lxml.html
from BeautifulGirl_Project.utils import save_ListData_to_json as save



"""用于获取美女生活照的链接，并返回列表"""
def getGirl_life_picture_url_list(girlDetail_list):
    # 定义一个大列表，用于存放美女生活照信息 格式如[{"name":[……]},{"name2":[……]}……]
    Allgirl_life_picture_url_list = []
    for dict in girlDetail_list:
        # 定义一个字典，用于封装美女生活照信息
        girLif_picture_link_dict = {}
        # 获取美女名称
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
        girl_life_picture_url_list = parse.xpath("//div[@class='p-tmb']/img/@src")
        girLif_picture_link_dict["girlName"] = girlName
        girLif_picture_link_dict["life_picture_link"] = girl_life_picture_url_list
        # 将这个大字典添加到大列表中
        Allgirl_life_picture_url_list.append(girLif_picture_link_dict)
    return Allgirl_life_picture_url_list

"""函数：用于下载美女生活照，并且保存到相应的文件夹中"""
def download_life_picture(girlLife_link_list):
    k = 0
    for dict in girlLife_link_list:
        # 用于标记图片序号
        i = 2
        # 获取美女名字
        girlName = dict["girlName"]
        # 获取美女生活照链接列表
        life_picture_link_list = dict["life_picture_link"]
        # 遍历链接，下载图片
        for link in life_picture_link_list:
            # 拼接好图片网址
            url = "http://www.xueshengmai.com"+link
            # 获取图片内容
            try:
                ImgContent = requests.get(url,verify=False,headers=useragentutil.get_headers()).content
            except Exception as e:
                # 打印报错信息
                print(e)
                print(girlName)
                print(url)
            # 打开文件
            filePath = "./GirlPicture/"+girlName+"/"+str(i)+"."+girlName+".jpg"
            file = open(filePath,"wb")
            file.write(ImgContent)
            # 关闭文件
            file.close()
            i = i + 1
        k = k + 1
        print("第%d个美女的生活照下载完毕"%k)

def main():
    # 加载json数据
    filePath = "./file/girlDetail_url.json"
    girlDetail_list = downloadGirl_picture.load_Json_to_data(filePath)
    # 获取每个美女生活照的地址
    girl_life_picture_url_list = getGirl_life_picture_url_list(girlDetail_list)
    # 将它保存为json格式的数据
    girl_life_picturePath = "D:/python练习/校花美女图片爬取/BeautifulGirl_Project/file/girlLif_picture.json"
    save.save_Data_to_json(girl_life_picturePath,girl_life_picture_url_list,"w")
    # 加载美女生活图片链接数据
    girlLife_linkPath = "./file/girlLif_picture.json"
    girlLife_link_list = downloadGirl_picture.load_Json_to_data(girlLife_linkPath)
    # 下载美女生活照
    download_life_picture(girlLife_link_list)
    print("程序已经走完")


if __name__ == '__main__':
    main()