from pyecharts import options as opts
from pyecharts.charts import PictorialBar
from pyecharts.globals import SymbolType
import csv

"""象型柱图"""

# location = ["山西", "四川", "西藏", "北京", "上海", "内蒙古", "云南", "黑龙江", "广东", "福建"]
# values = [13, 42, 67, 81, 86, 94, 166, 220, 249, 262]

csv_f = open("C:/Users/跌入你的温柔/Desktop/国内疫情.csv", newline='')
csvReader = csv.reader(csv_f)

state_list = []     # 省
dangqian_list = []  # 当前确诊
leiji_list = []     # 累计确诊

for content in csvReader:
    state_list.append(content[0])
    dangqian_list.append(content[1])
    leiji_list.append(content[2])

csv_f.close()

c = (
    PictorialBar()
    .add_xaxis(state_list[1:15])
    .add_yaxis(
        "当前确诊",
        dangqian_list[1:15],
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=18,
        symbol_repeat="fixed",
        symbol_offset=[0, 0],
        is_symbol_clip=True,
        symbol=SymbolType.ROUND_RECT,
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="PictorialBar-大陆当前确诊病例"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
    .render("PictorialBar-大陆当前确诊病例.html")
)
