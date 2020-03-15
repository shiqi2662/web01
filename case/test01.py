import json
import logging
import time
import unittest

from parameterized import parameterized

from config import BARE_OS
from page.kt import PageBugBrowse
from page.page_bug_browse import PageBugCreate
from page.page_my import PageMY
from page.page_qa import PageQa
from page.page_user_login import PageUserLogin
from tool.utils import Utils, exists_text

def get_json():
    list = []
    with open(BARE_OS+"/data/create_bug.json","r",encoding="utf-8")as f:
        data=json.load(f)
        for d in data:
            bug_title = d.get("bug_title")
            expect = d.get("expect")
            list.append((bug_title,expect))
        return list



class Testlogin(unittest.TestCase):
    driver = None
    @classmethod
    def setUpClass(cls):
        # 打开浏览器
        cls.driver = Utils.get_driver()
        # 打开登录页面
        cls.driver.get("http://demo.zentao.net/user-login.html")

        # 测试登录
        cls.ulp = PageUserLogin(cls.driver)

        cls.kt = PageMY(cls.driver)
        cls.bug = PageQa(cls.driver)

        cls.ti_bug = PageBugBrowse(cls.driver)

        cls.skt = PageBugCreate(cls.driver)
        cls.ulp.page_user_yewu()


    @classmethod
    def tearDownClass(cls):
        Utils.quit_driver()

    def setUp(self):
        time.sleep(2)

    def tearDown(self):
        pass

    @parameterized.expand(get_json())
    def test01_login(self,tit,exc):

        logging.info("添加用例的标题是: {}".format(tit))
        self.kt.page_my()
        time.sleep(2)
        self.bug.page_bug()
        time.sleep(2)
        self.ti_bug.page_bug_browse()
        time.sleep(2)
        self.skt.page_bug_zj(tit)

        msg =exists_text(exc)
        self.assertTrue(msg)
