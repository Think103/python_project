import lxml.html
from BeautifulGirl_Project.utils import save_ListData_to_json as save
from BeautifulGirl_Project import spiderHtmlData

"""该.py是用来解析网页，然后获取自己想要的数据信息"""


"""解析网页数据，返回美女姓名、图片地址、点赞数、详细地址四个列表"""
def get_BeautifulGirl_info(htmlContent):
    # 获取解析器
    metree = lxml.html.etree
    # 获取解析器对象
    parse = metree.HTML(htmlContent)
    # 开始解析
    # 美女姓名
    girlName_list = parse.xpath("//div[@class='img']/span/text()")
    # 美女图片地址  http://www.xueshengmai.com/d/file/20200116/smallf29ef026905f40d34814b251c0c85d761579167601.jpg
    girlImg_url_list = parse.xpath("//div[@class='img']/a/img/@src")
    # 美女点赞数
    girlZan_count_list = parse.xpath("//div[@class='items_likes fl']/em/text()")
    # 美女详细信息地址
    girlDetails_url_list = parse.xpath("//div[@class='img']/a/@href")
    return girlName_list, girlImg_url_list, girlZan_count_list, girlDetails_url_list



"""将每个美女数据拼接成一个小字典，最后用一个大列表包住，最后返回这个大列表"""
def splicing_data_to_dict(girlName_list, girlImg_url_list, girlZan_count_list, girlDetails_url_list):
    # 定义一个大列表
    girlList = []
    for index in range(0,len(girlName_list)):
        # 定义一个字典，用来封装美女信息
        girDict = {}
        girDict["girlName"] = girlName_list[index]
        girDict["girlImg_url"] = "http://www.xueshengmai.com"+girlImg_url_list[index]
        girDict["girlDetails_url"] = girlDetails_url_list[index]
        girDict["点赞数"] = girlZan_count_list[index]
        # 将每个美女字典添加到大列表中
        girlList.append(girDict)
    return girlList


"""爬取指定页数的数据"""
def spiderDataLimt(num):
    # 存放所有美女的信息列表
    girlAllInfo = []
    # 用于递增url的页数
    for i in range(0,num):
        url = "http://www.xueshengmai.com/list-1-" + str(i) + ".html"
        htmlContent = spiderHtmlData.getHtml(url)
        # 解析网页数据，并返回所需信息
        girlName_list, girlImg_url_list, girlZan_count_list, girlDetails_url_list = get_BeautifulGirl_info(htmlContent)
        # 将每个美女数据拼接成一个小字典，最后用一个大列表包住，最后返回这个大列表
        girlList = splicing_data_to_dict(girlName_list, girlImg_url_list, girlZan_count_list, girlDetails_url_list)
        girlAllInfo.append(girlList)
        # 将列表数据保存为json数据
        filePath = "D:/python练习/校花美女图片爬取/BeautifulGirl_Project/file/girlInfor.json"
        save.save_Data_to_json(filePath, girlAllInfo,"w")

def main():
    # 这里可以修改爬取页数
    spiderDataLimt(4)
    print("程序已经走完")


if __name__ == '__main__':
    main()
