import time

import page
from base.base_page import Base
from page.page_my import PageMY
from page.page_user_login import PageUserLogin
from tool.utils import Utils


class PageQa(Base):

    def page_bug(self):

        self.click_base(page.page_bug)

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


    # 退出浏览器
    time.sleep(2)
    Utils.quit_driver()

