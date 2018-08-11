import unittest

"""
跳过测试和预期失败
"""


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test_skip")

    @unittest.skipIf(3 > 2, "当条件为真，跳过这个测试用例")
    def test_skip_if(self):
        print("test_skip_if")

    @unittest.skipUnless(3 < 2, "当条件为假，跳过这个测试用例")
    def test_skip_unless(self):
        print("test_skip_unless")

    @unittest.expectedFailure#标记这个测试用例执行失败
    def test_expected_failure(self):
        self.assertEqual(1,1)
        print("test_expected_failure")


if __name__ == '__main__':
    unittest.main()
