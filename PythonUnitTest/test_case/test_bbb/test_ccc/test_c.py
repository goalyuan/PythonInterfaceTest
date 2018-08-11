import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("测试开始准备工作")

    def test_c(self):
        print("测试用例c")

    def tearDown(self):
        print("测试结束结束工作")


if __name__ == '__main__':
    unittest.main()
