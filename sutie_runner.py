# 组织运行测试用例
import time
import unittest


from case.test01 import Testlogin
from config import BARE_OS

suite =  unittest.TestSuite()


suite.addTest(unittest.makeSuite(Testlogin))

file = BARE_OS + "/report/report_{}.txt".format(time.strftime("%Y%m%d%H%M%S"))

with open(file,"w")as f:
    runner = unittest.TextTestRunner(stream=f,verbosity=2)

    runner.run(suite)

