
import unittest
import time


class Test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("start!")
        print("\n")

    @classmethod
    def tearDownClass(self):
        time.sleep(1)
        print("end!")

    @unittest.skip('no reason')
    def test03(self):
        u'''测试登录用例，账号：xx 密码xx'''
        print("执行测试用例03")

    @unittest.skipIf(1,u'为真时跳过')
    def test04(self):
        u'''测试登搜索用例，关键词：xxx'''
        print("执行测试用例04")

    @unittest.skipUnless(0,u'为false时跳过')
    def test05(self):
        u'''测试登搜索用例，关键词：xxx'''
        print("执行测试用例05")

    def test06(self):
        u'''测试登搜索用例，关键词：xxx'''
        print("执行测试用例06")