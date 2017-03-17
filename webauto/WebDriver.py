#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2016/12/14 15:59
# *******

from selenium import webdriver
import threading,time,queue,os
from Testfile import MobileGettest
from  Action_choose import Choose
class web(threading.Thread):
    def __init__(self,text,content,rs,message):
        threading.Thread.__init__(self)

        self.text=text
        self.content=content
        self.rs=rs
        self.message=message
    def run (self):
        con=text.split("\\")[-1]
        driver=webdriver.Chrome()
        driver.get(" http://www.baidu.com/")
        Choose(driver,self.text).get_action()
        self.message+='%s执行%s内容运行成功\n'%(self.getName(),con)

        while self.content.qsize() !=0:
            # print (content.qsize())
            self.text=self.content.get()
            print (self.text)
            if not Choose(driver,self.text).get_action():
                self.rs.append(self.text)
            self.message+='%s执行%s内容运行成功\n'%(self.getName(),con)

        with open('d://123.txt','a')as f:
            f.write(self.message)
        driver.close()



if __name__=="__main__":
    path=os.getcwd()
    content=MobileGettest.get_testfile(path)
    f_rs=[]
    th=[]
    message='开始测试：'
    """
    修改线程数，可以启动多个浏览器并发执行
    """
    for i in range(2):
        text=content.get()
        # print (text)
        # web(text,content,f_rs).setDaemon(True)
        th.append(web(text,content,f_rs,message))
    for i in range(2)  :
       th[i].start()
    for i in range(2)  :
       th[i].join()
