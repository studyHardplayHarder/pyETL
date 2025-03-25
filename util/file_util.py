# coding:utf8
"""
和文件处理相关的工具方法，都定义到这个Python文件中
"""
import os


def get_dir_files_list(path="./", recursion=False):
    """
    判断文件夹下面，有哪些文件
    :param path: 被判断的文件夹的路径，默认当前路径
    :param recursion: 是否递归读取，默认不递归
    :return: list对象，list里面存储的是文件的路径
    """
    # os.listdir 这个API 返回的是 你给定的path下面有哪些```文件和文件夹```
    dir_names = os.listdir(path)
    files = []
    for dir_name in dir_names:
        abs_path = f'{path}/{dir_name}'
        if os.path.isfile(abs_path):
            files.append(abs_path)
        else:
            if recursion:
                recursion_files_list = get_dir_files_list(abs_path, recursion=recursion)
                files += recursion_files_list

    return files





