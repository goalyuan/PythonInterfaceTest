import unittest


class Test(unittest.TestCase):
    def setUp(self):
        print("测试开始")

    def tearDown(self):
        print("测试结束")

    def test_case(self):
        print("测试用例")
        # self.assertEqual(1,2) #断言1，2是否相等
        # self.assertNotEqual(1,1)#断言1，1是否相等
        # self.assertTrue(1==2)#断言条件1==2是否为True
        # self.assertFalse(1==1)#断言条件1==1是否为True
        # self.assertIn(1,[2,3])#断言1在没有在[2,3]中

    def test_demo(self):
        print("测试用例demo")

class Test1(unittest.TestCase):
    def setUp(self):
        print("Test1测试开始")

    def tearDown(self):
        print("Test1测试结束")

    def test_case(self):
        print("Test1测试用例")


if __name__ == '__main__':
    # 构造测试集，run方法执行的顺序就是addTest添加的顺序
    suite = unittest.TestSuite()
    suite.addTest(Test("test_demo"))#为什么传参字符串是test_case，执行结果却有"测试用例demo",pycharm执行的问题。
    suite.addTest(Test1("test_case"))

    # 执行测试
    run = unittest.TextTestRunner()
    run.run(suite)
