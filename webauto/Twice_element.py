#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2016/12/7 16:33
# *******
from selenium.webdriver.remote.webdriver import *
from appium.webdriver.webdriver import *
from Testfile.MobileGettest import *
class Twice:

    def __init__(self,driver):
        self.driver=driver

    def get_search(self,by,value):
        if by == 'id':
            by = By.CSS_SELECTOR
            value = '[id="%s"]' % value
        elif by == 'tag_name':
            by = By.CSS_SELECTOR
        elif by == "class_name":
            by = By.CSS_SELECTOR
            value = ".%s" % value
        elif by == "name":
            by = By.CSS_SELECTOR
            value = '[name="%s"]' % value
        return by,value
    def save_screenshot(self,file_adr):
        """
        二次封装保存图片
        """
        return self.driver.save_screenshot(file_adr)

    def click(self,by,value):
        """
        二次封装点击方法
        """

        rs=self.get_search(by,value)
        return self.driver.find_element( by=rs[0] ,value=rs[1]).click()

    def send_keys(self,by,value,content):
        """
        二次封装输入方法
        """
        rs=self.get_search(by,value)

        return self.driver.find_element(by=rs[0] ,value=rs[1]).send_keys(content)

    def reset(self,files):
        """
        二次封装重启方法
        """
        return self.driver.reset()
        return False
    def get(self,url):
        """
        再封装访问网站地址的方法
        """
        return self.driver.get(url)
if __name__=="__main__":
    Twice.reset()