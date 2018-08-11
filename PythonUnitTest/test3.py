import unittest

"""
run执行多级目录的testcase，每一级目录都是带有__init__.py文件
"""
test_dir = './test_case'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
