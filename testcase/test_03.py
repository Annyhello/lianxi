
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
        self.assertEqual(3, 1 + 1)
        print("执行测试用例03")

    @unittest.skipIf(1,u'为真时跳过')
    def test04(self):
        u'''测试登录用例，账号：xx 密码xx'''
        self.assertEqual(3, 1 + 2)
        print("执行测试用例03")


