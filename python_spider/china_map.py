from pyecharts.charts import Map
from pyecharts import options as opts
import csv

china_dic = {}
csv_f = open("C:/Users/跌入你的温柔/Desktop/国内疫情.csv", newline='')
csvReader = csv.reader(csv_f)

for content in csvReader:
    china_dic[content[0][:2]] = content[1]
map1 = Map()
# print(list(china_dic.items()))
map1.set_global_opts(   # 全局配置
    title_opts=opts.TitleOpts(title="国内现在疫情地图"),
    visualmap_opts=opts.VisualMapOpts(max_=150, is_piecewise=True,  # is_piecewise参数表示是否分段
                                      pieces=[                                          # 定义每个字段的范围以及每个字段的样式
                                        {"max": 150, "min": 101, "label": ">100", "color": "#8A0808"},
                                        {"max": 100, "min": 51, "label": "51-100", "color": "#B40404"},
                                        {"max": 50, "min": 31, "label": "31-50", "color": "#DF0101"},
                                        {"max": 30, "min": 11, "label": "11-30", "color": "#F78181"},
                                        {"max": 10, "min": 6, "label": "6-10", "color": "#F5A9A9"},
                                        {"max": 5, "min": 0, "label": "0-5", "color": "#F5A9A9"}, ], )
    )
map1.add("国内现在疫情地图", data_pair=list(china_dic.items()), maptype="china", is_roam=True)
map1.render('D:/pychar/pycharm_code/国内新冠病毒确诊地图.html')
