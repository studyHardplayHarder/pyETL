# coding:utf8
"""
针对file_util.py内的方法做单元测试
"""
import os.path
from unittest import TestCase
from util import file_util

class TestFileUtil(TestCase):
    def setUp(self) -> None:
        self.project_root_path = os.path.dirname(os.getcwd())

    def test_get_dir_files_list(self):
        '''
        用test_dir检验 不递归结果应该是1和2
        递归结果应该是1, 2, 3, 4, 5
        '''
        test_path = f"{self.project_root_path}/test/test_dir"
        # 先测试不递归
        result = file_util.get_dir_files_list(test_path, recursion=False)
        files = []
        for file in result:
            # file_name = file.rsplit('/', 1)[-1]
            file_name = os.path.basename(file)
            files.append(file_name)
        files.sort()
        self.assertEqual(['1', '2'], files)

        # 递归
        result = file_util.get_dir_files_list(test_path, recursion=True)
        files = []
        for file in result:
            file_name = os.path.basename(file)
            files.append(file_name)
        files.sort()
        self.assertEqual(["1", "2", "3", "4", "5"], files)

