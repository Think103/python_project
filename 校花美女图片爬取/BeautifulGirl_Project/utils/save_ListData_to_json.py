import os
import json


"""说明：将python列表数据保存为json格式"""
def save_Data_to_json(filePath,ListDat,mode):
    """
    :param filePath:  调用该函数，需要传入绝对路径
    :param ListDat:  python列表类型
    :param mode:    是否是追加模式
    :return:
    """

    # 切割绝对路径的父路径，以及文件名
    parentDir,fileName = os.path.split(filePath)
    if not os.path.exists(parentDir):
        os.makedirs(parentDir)
    # 打开文件
    file = open(filePath, mode,encoding="utf-8")
    # 将列表数据转为json数据
    json.dump(ListDat,file,ensure_ascii=False,indent=2)
    # 关闭文件
    file.close()
    # print("数据保存成功")