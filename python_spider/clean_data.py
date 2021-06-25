# from openpyxl import *
import pandas as pd


"""
filename = r'D:\pychar\pycharm_code\国内疫情统计表3.xlsx'
wb = load_workbook(filename)
ws = wb.active
# for i in range(2):
#     ws.delete_cols(10) # 删除第 10 列数据*2
# for i in range(2):
#     ws.delete_cols(1)  # 删除第 1 列数据*2
# ws.delete_cols(2)  # 删除第 2 列数据
# ws.delete_rows(1)  # 删除第 1 行数据
ws.delete_rows(1)  # 删除第 1 行数据
wb.save(filename)
"""

data = pd.read_csv(r'D:\pychar\pycharm_code\国内疫情统计表3.xlsx')
# data.head()
# data = pd.read_csv(r'D:\pychar\pycharm_code\国内疫情统计表3.xlsx', dtype={'当前确诊': int})

data.drop(labels='统计数据区', axis=1)
data.drop(labels='地区代码', axis=1)
data.drop(labels='省区短名', axis=1)
data.drop(labels='评论', axis=1)

data.to_csv('国内疫情.csv', encoding='UTF-8')

