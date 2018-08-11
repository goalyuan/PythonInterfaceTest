import unittest

"""
fixtures,setUp&tearDown方法应用在测试类和测试模块中
"""


def setUpModule():
    print("setUpModule")


def tearDownModule():
    print("tearDownModule")


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("setUpClass")

    def setUp(self):
        print("setUp")

    def tearDown(self):
        print("tearDown")

    def test_demo(self):
        print("test_demo")


if __name__ == '__main__':
    unittest.main()
