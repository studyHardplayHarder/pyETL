# coding:utf8
"""
这个python文件的功能，是构建日志输出的模块
方便我们后续快速的在程序中输入日志信息

Python中最常用的日志库，是一个叫做logging的模块
"""
import logging
from config import project_config as conf

class Logging:
    def __init__(self, level=20):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)

def init_logger():
    logger = Logging().logger

    if logger.handlers:
        return logger

    # 设置logger属性
    file_handler = logging.FileHandler(
        filename=conf.log_root_path+conf.log_name
        , mode='a', encoding='UTF-8'
    )
    # 设置一个format输出格式
    fmt = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s")
    file_handler.setFormatter(fmt)

    logger.addHandler(file_handler)
    return logger






