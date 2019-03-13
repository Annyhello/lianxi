import unittest
import requests
import json

URL = 'http://xxx:9000'


# 针对登录模块的测试类
class Login_Module(unittest.TestCase):
    # 获取sessionID
    def get_session(self):
        # 这段代码post代表post方法，post函数的第一个参数代表接口URL地址，第二个参数代表数据信息
        r = requests.post(URL + '/login',
                          data={'realPhone': '18890000000', 'password': '123456'})
        # 这段代码loads代表将返回的相应字符串转化为python字典数据类型，然后['data']就可以取出属性为data的数据
        return json.loads(r.text)['data']

    # 登录接口测试
    def test_login(self):
        r = requests.post(URL + '/login',
                          data={'realPhone': '18890000000', 'password': '123456'})
        obj = json.loads(r.text)
        self.assertEqual(obj['code'], 0)  # 判断返回结果码是否为0

    # 身边用户接口测试
    def test_near_user(self):
        r = requests.get(URL + '/nearuser',
                         params={'sessionID': self.get_session()})
        obj = json.loads(r.text)
        self.assertEqual(len(obj['data']), 10)  # 判断返回列表中用户是否只有十个


if __name__ == '__main__':
    unittest.main()