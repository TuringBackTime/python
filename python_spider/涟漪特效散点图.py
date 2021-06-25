from pyecharts import options as opts
from pyecharts.charts import EffectScatter
from pyecharts.globals import SymbolType
import csv

"""涟漪特效散点图"""

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
    EffectScatter()
    .add_xaxis(state_list[1:15])
    .add_yaxis("当前确诊", dangqian_list[1:15], symbol=SymbolType.ARROW)
    .set_global_opts(title_opts=opts.TitleOpts(title="EffectScatter-不同Symbol"))
    .render("effectscatter_symbol.html")
)
