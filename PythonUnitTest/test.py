import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("测试开始准备工作")

    def test_look(self):
        print("测试用例")

    def tearDown(self):
        print("测试结束结束工作")


if __name__ == '__main__':
    unittest.main()  # unittest提供了全局的main()方法，方便直接运行测试脚本。
    # main()方法使用TestLoader类在这个类中搜索所有包含"test"
    # 开头的测试方法，自动执行它们，执行的顺序按照ASCII码顺序
