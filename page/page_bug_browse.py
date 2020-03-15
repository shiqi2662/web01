import time

import page
from base.base_page import Base

# 点击提bug
from page.kt import PageBugBrowse
from page.page_my import PageMY
from page.page_qa import PageQa
from page.page_user_login import PageUserLogin
from tool.utils import Utils




class PageBugCreate(Base):

    def page_bug01(self):
        self.click_base(page.page_bug_create001)

    def page_bug02(self):
        self.click_base(page.page_bug_create002)

    def page_bug03(self,value):
        self.input_base(page.page_title,value)
    def page_bug04(self):
        self.click_base(page.page_bug_create003)



    def page_bug_zj(self,value):
        self.page_bug01()
        self.page_bug02()
        self.page_bug03(value)
        self.driver.execute_script("window.scrollTo(0,5000)")
        time.sleep(2)
        self.page_bug04()



if __name__ == '__main__':
    # 打开浏览器
    driver = Utils.get_driver()
    # 打开登录页面
    driver.get("http://demo.zentao.net/user-login.html")

    # 测试登录

    ulp = PageUserLogin(driver)
    ulp.page_user_yewu()
    kt =  PageMY(driver)
    kt.page_my()
    bug = PageQa(driver)
    bug.page_bug()
    time.sleep(2)

    ti_bug=PageBugBrowse(driver)
    ti_bug.page_bug_browse()

    skt =PageBugCreate(driver)
    skt.page_bug_zj("haha")


    # 退出浏览器
    time.sleep(2)
    Utils.quit_driver()