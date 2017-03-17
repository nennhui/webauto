#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2016/12/9 14:06
# *******
import Twice_element
import json,time
from selenium.webdriver.remote.webdriver import *
class Choose():
    def __init__(self,driver,files):
        self.driver=driver
        self.files=files
        self._two=Twice_element.Twice(self.driver)

    def get_action(self):
        with open(self.files,'r') as f :
            con=f.read()
        con=con.split(';')
        for test_flow in con :
            # print test_flow
            time.sleep(3)
            # print (test_flow)
            test_flow=json.loads(test_flow)
            #重启操作
            if test_flow["test_action"]=='get':
                self._two.get(test_flow["test_adr"])

            #点击操作
            elif test_flow["test_action"]=='click':
                test_type=test_flow['test_type']
                test_element=test_flow['test_element']
                self._two.click(test_type,test_element )

            #截图
            elif test_flow["test_action"]=='save_screenshot':
                test_adr=test_flow['test_adr']
                self._two.save_screenshot(test_adr)
            #输入
            elif test_flow["test_action"]=='send_keys':
                test_type=test_flow['test_type']
                test_element=test_flow['test_element']
                test_content=test_flow['test_content']
                self._two.send_keys(test_type,test_element,test_content )
            #重启
            elif  test_flow["test_action"]=='reset':
                return self._two.reset(self.files)
            elif test_flow["test_action"]=="window_handles":
                return self.driver.window_handles()
            else:
                return  False



