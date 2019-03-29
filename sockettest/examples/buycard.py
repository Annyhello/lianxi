#coding=utf-8

import unittest
import requests

class testStore(unittest.TestCase):
    def testbuycard(self):
        try:
            params = {"d": '{"type":1,"id":"Huangma"}',"t": 'f8dc3e3fff822b86c6d320b7c77dbe50', "seq": 13, "rseq": 13}
            headers = {"Content-type": "application/x-www-form-urlencoded", "Accept-Encoding": "gzip"}
            r = requests.post('http://192.168.5.111:8590/store/gacha', data=params,headers=headers)
            print(r.text)
            self.assertEqual(int(r.json()['d']['cost']['num']),200)
            self.assertEqual(int(r.json()['d']['cost']['curr_num']), 4080)
        except Exception as e:
            print(e)


if __name__ =='__main__':
    unittest.main()