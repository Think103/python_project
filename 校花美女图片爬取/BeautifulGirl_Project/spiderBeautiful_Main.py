import requests
from BeautifulGirl_Project import spiderHtmlData
from BeautifulGirl_Project import spiderParseHtml
from BeautifulGirl_Project import downloadGirl_picture
from BeautifulGirl_Project import spiderGirl_introduce_infor
from BeautifulGirl_Project import spiderGirl_other_picture


"""主函数集群"""
def main():
    spiderHtmlData.main()
    spiderParseHtml.main()
    downloadGirl_picture.main()
    spiderGirl_introduce_infor.main()
    spiderGirl_other_picture.main()

if __name__ == '__main__':
    main()
