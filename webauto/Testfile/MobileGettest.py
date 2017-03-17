#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2016/12/12 11:55
# *******
# from  Testfile.quque import Stack as stack
import os
import queue

def get_testfile(adr):
    """
    获取用例文件
    return 用例文件的地址的数组
    """
    all =os.listdir(adr)
    testfile=[]
    for  i in all:
        pp=i.split('.')
        if len(pp)>1:
            if pp[1]=='json':
                text=adr+"\\"+i
                testfile.append(text)
                # print (testfile)
    return insert_queue(testfile)

def  insert_queue(fileadrs):
    """
    添加测试到队列中
    return 队列
    """
    content=queue.Queue()
    for i in  fileadrs:
        content.put(i)
    return content

if __name__=="__main__":
    a=get_testfile('D:\python_project\mobileauto')




