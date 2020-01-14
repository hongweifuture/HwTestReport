#!/usr/bin/env python3 
# coding=utf-8
__author__ = "zhaohongwei"
__email__ = "hongweifuture@163.com"
__contact__ = "https://blog.csdn.net/z_johnny"
__version__ = "0.1"
__date__ = "2019/9/9 16:22"
__maintainer__ = "zhaohongwei,"
__description__ = ""

"""
History:
2020/1/13 11:47 : python使用geckodriver驱动Firefox https://github.com/mozilla/geckodriver/releases
2019/9/9 16:22 : Created by zhaohongwei 
"""

import unittest
# from HwTestReport import HTMLTestReport
# from HwTestReport import HTMLTestReportEN
from HwTestReport_local import HTMLTestReport

class Case_assert_1(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_ok(self):
        self.assertEqual(1,1)

    def test_faile(self):
        self.assertEqual(1,2)

    def test_error(self):
        raise Exception

class Case_assert_2(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_ok(self):
        self.assertTrue(True)

class Case_assert_3(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_error(self):
        raise Exception

class Case_assert_4(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_faile(self):
        self.assertEqual(1,3)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Case_assert_1('test_ok'))
    suite.addTest(Case_assert_1('test_faile'))
    suite.addTest(Case_assert_1('test_error'))
    suite.addTest(Case_assert_2('test_ok'))
    suite.addTest(Case_assert_3('test_error'))
    suite.addTest(Case_assert_4('test_faile'))

    with open('./HwTestReport.html', 'wb') as report:
        runner = HTMLTestReport(stream=report,
                                verbosity=2,
                                title='HwTestReport 测试',
                                description='带截图，带饼图，带详情',
                                tester='Johnny')
        runner.run(suite)
