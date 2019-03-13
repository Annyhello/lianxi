# coding:utf-8
import unittest
import os
import report.HTMLTestRunner

# python2.7要是报编码问题，就加这三行，python3不用加
# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

# 用例路径
case_path = os.path.join(os.getcwd(), "testcase")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")


def all_case():
    #pattern:匹配的测试文件的格式；top_level_dir：项目的顶级目录
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    print(discover)
    return discover


if __name__ == "__main__":
    # html报告文件路径
    report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_abspath, "wb")
    runner = report.HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()