# 一.登录禅道
import time

import page
from base.base_page import Base
from tool.utils import Utils


class PageUserLogin(Base):



    def page_jia(self):
        self.click_base(page.page_ceshi_jia)

    def page_login(self):
        self.click_base(page.page_login)

    def page_user_yewu(self):
        self.page_jia()
        self.page_login()


if __name__ == '__main__':
    # 打开浏览器
    driver = Utils.get_driver()
    # 打开登录页面
    driver.get("http://demo.zentao.net/user-login.html")

    # 测试登录

    ulp = PageUserLogin(driver)
    ulp.page_user_yewu()

    # 退出浏览器
    time.sleep(2)
    Utils.quit_driver()
