from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import csv

csv_f = open("C:/Users/跌入你的温柔/Desktop/国内疫情.csv", newline='')
csvReader = csv.reader(csv_f)

state_list = []     # 省
dangqian_list = []  # 当前确诊
leiji_list = []     # 累计确诊
zhiyu = []      # 治愈人数
siwang = []     # 死亡人数
for content in csvReader:
    state_list.append(content[0])
    dangqian_list.append(content[1])
    leiji_list.append(content[2])
    zhiyu.append(content[4])
    siwang.append(content[5])

csv_f.close()

bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(state_list[:15])
    .add_yaxis("当前确诊", dangqian_list[:15])
    .add_yaxis("累计确诊", leiji_list[:15])
    .set_global_opts(title_opts=opts.TitleOpts(title="国内新冠疫情确诊top15"))
)

bar.render('D:/pychar/pycharm_code/国内死亡治愈对比图.html')
