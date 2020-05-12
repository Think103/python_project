if __name__ == '__main__':
    """
    filePath = "../file/test.txt"
    # file = open(filePath,"w",encoding="utf-8")
    for i in range(0,3):
        file = open(filePath, "a", encoding="utf-8")
        file.write(str(i))
        file.close()
    # file.close()
    print("完成")
    """

    """
    content = ["aaa","bbb","ccc","eee","dfjkjf","dj"]
    filePath = "../file/test.txt"
    file = open(filePath,"w",encoding="utf-8")
    for str in content:
        file.writelines(str+"\n")
    file.close()
    print("测试结束")
    """
    i = 1
    try:
        j = i/0
    except Exception as e:
        print(e)
    print("helloword")

