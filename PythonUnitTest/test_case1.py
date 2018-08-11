import unittest


class Test1(unittest.TestCase):
    def setUp(self):
        print("test_case1---Test1")

    def tearDown(self):
        print("test_case1---Test1")

    def test_demo(self):
        print("test_case1---Test1---test_demo")

if __name__ == '__main__':
    unittest.main()