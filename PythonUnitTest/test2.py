import unittest

test_dir = './'
# discover(start_dir,pattern='test*.py',top_level_dir=None)
# start_dir测试用例目录
# pattern='test*.py'表示用例文件名匹配规则，test*.py表示test开头，.py结尾的文件，*表示任意字符
# top_level_dir=None表示测试模块顶层目录，如果没有顶层目录，默认为None
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(discover)
