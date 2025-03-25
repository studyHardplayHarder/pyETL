# coding:utf8
"""
整个ETL案例中的所有的配置项，都设置在这个Python文件中
"""
import os
import time

# ################## --程序运行日志的配置项 start-- ###################
# 配置日志输出的根目录
log_root_path = "E:/03_scripts_dest/logs"
p_path = os.path.abspath(os.path.dirname('project_config.py'))
# log_root_path = p_path+"/logs/"

# 配置日志输出的文件名
log_name = f'pyetl-{time.strftime("%Y%m%d-%H", time.localtime(time.time()))}.log'
"""
常见的时间格式化的格式：
%Y:4位数字的年份：2022
%m:2位数字的月份：05
%d:2位数字的日期：15
%H：24小时制的小时
%M：2位数字的分钟
%S：2位数字的秒
如果要格式化为：2022-05-15 10:05:55
%Y-%m-%d %H:%M:%S
"""
# ################## --程序运行日志的配置项 end-- ###################

# ################## --JSON订单数据采集的相关配置项 start-- ###################
# 被采集的JSON数据，在哪个文件夹
json_data_root_path = "E:/02 python大数据学习文件/4-ELT/4-ETL/Day03/测试数据/"

# 写出CSV的根目录配置
retail_output_csv_root_path = "E:/02 python大数据学习文件/4-ELT/4-ETL/Day03/"
# 写出订单模型，CSV的文件名字配置
retail_orders_output_csv_file_name = f'orders-{time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))}.csv'
# 写出订单详情（带商品信息）模型，CSV的文件名字配置
retail_orders_detail_output_csv_file_name = f'orders-detail-{time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))}.csv'

# ################## --JSON订单数据采集的相关配置项 end-- ###################

# ################## --MySQL相关配置项 start-- ###################
mysql_charset = "utf8"
# 元数据管理库的配置
metadata_host = "localhost"
metadata_user = "root"
metadata_password = "root"
metadata_port = 3306
metadata_db_name = "metadata"
# 文件监控表名称，存储哪些文件被处理过
metadata_file_monitor_table_name = "file_monitor"
# 文件监控表，建表语句的列信息
metadata_file_monitor_table_create_cols = """
    id INT PRIMARY KEY AUTO_INCREMENT, 
    file_name VARCHAR(255) UNIQUE NOT NULL COMMENT '被处理的文件名称', 
    process_lines INT COMMENT '本文件中有多少条数据被处理', 
    process_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '处理时间'
"""

# 目标数据库的相关配置
target_host = metadata_host
target_user = metadata_user
target_password = metadata_password
target_port = metadata_port
target_db_name = "retail"

# JSON数据采集后，写入MySQL，存储订单相关的表，表名是：
target_orders_table_name = "orders"
# orders表的建表语句的列信息
target_orders_table_create_cols = \
    f"order_id VARCHAR(255) PRIMARY KEY, " \
    f"store_id INT COMMENT '店铺ID', " \
    f"store_name VARCHAR(30) COMMENT '店铺名称', " \
    f"store_status VARCHAR(10) COMMENT '店铺状态(open,close)', " \
    f"store_own_user_id INT COMMENT '店主id', " \
    f"store_own_user_name VARCHAR(50) COMMENT '店主名称', " \
    f"store_own_user_tel VARCHAR(15) COMMENT '店主手机号', " \
    f"store_category VARCHAR(10) COMMENT '店铺类型(normal,test)', " \
    f"store_address VARCHAR(255) COMMENT '店铺地址', " \
    f"store_shop_no VARCHAR(255) COMMENT '店铺第三方支付id号', " \
    f"store_province VARCHAR(10) COMMENT '店铺所在省', " \
    f"store_city VARCHAR(10) COMMENT '店铺所在市', " \
    f"store_district VARCHAR(10) COMMENT '店铺所在行政区', " \
    f"store_gps_name VARCHAR(255) COMMENT '店铺gps名称', " \
    f"store_gps_address VARCHAR(255) COMMENT '店铺gps地址', " \
    f"store_gps_longitude VARCHAR(255) COMMENT '店铺gps经度', " \
    f"store_gps_latitude VARCHAR(255) COMMENT '店铺gps纬度', " \
    f"is_signed TINYINT COMMENT '是否第三方支付签约(0,1)', " \
    f"operator VARCHAR(10) COMMENT '操作员', " \
    f"operator_name VARCHAR(50) COMMENT '操作员名称', " \
    f"face_id VARCHAR(255) COMMENT '顾客面部识别ID', " \
    f"member_id VARCHAR(255) COMMENT '顾客会员ID', " \
    f"store_create_date_ts TIMESTAMP COMMENT '店铺创建时间', " \
    f"origin VARCHAR(255) COMMENT '原始信息(无用)', " \
    f"day_order_seq INT COMMENT '本订单是当日第几单', " \
    f"discount_rate DECIMAL(10, 5) COMMENT '折扣率', " \
    f"discount_type TINYINT COMMENT '折扣类型', " \
    f"discount DECIMAL(10, 5) COMMENT '折扣金额', " \
    f"money_before_whole_discount DECIMAL(10, 5) COMMENT '折扣前总金额', " \
    f"receivable DECIMAL(10, 5) COMMENT '应收金额', " \
    f"erase DECIMAL(10, 5) COMMENT '抹零金额', " \
    f"small_change DECIMAL(10, 5) COMMENT '找零金额', " \
    f"total_no_discount DECIMAL(10, 5) COMMENT '总价格(无折扣)', " \
    f"pay_total DECIMAL(10, 5) COMMENT '付款金额', " \
    f"pay_type VARCHAR(10) COMMENT '付款类型', " \
    f"payment_channel TINYINT COMMENT '付款通道', " \
    f"payment_scenarios VARCHAR(15) COMMENT '付款描述(无用)', " \
    f"product_count INT COMMENT '本单卖出多少商品', " \
    f"date_ts TIMESTAMP COMMENT '订单时间', " \
    f"INDEX (receivable), INDEX (date_ts)"

# JSON数据采集后，写入MySQL，存储订单详情（带商品信息的）相关的表，表名是：
target_orders_detail_table_name = "orders_detail"
# orders_detail表的建表语句的列信息
target_orders_detail_table_create_cols = \
    f"order_id VARCHAR(255) COMMENT '订单ID', " \
    f"barcode VARCHAR(255) COMMENT '商品条码', " \
    f"name VARCHAR(255) COMMENT '商品名称', " \
    f"count INT COMMENT '本单此商品卖出数量', " \
    f"price_per DECIMAL(10, 5) COMMENT '实际售卖单价', " \
    f"retail_price DECIMAL(10, 5) COMMENT '零售建议价', " \
    f"trade_price DECIMAL(10, 5) COMMENT '贸易价格(进货价)', " \
    f"category_id INT COMMENT '商品类别ID', " \
    f"unit_id INT COMMENT '商品单位ID(包、袋、箱、等)', " \
    f"PRIMARY KEY (order_id, barcode)"


# 数据源数据库的配置


# ################## --MySQL相关配置项 end-- ###################








