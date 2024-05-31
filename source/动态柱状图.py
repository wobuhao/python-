from pyecharts.charts import Bar, Timeline
from pyecharts.globals import ThemeType
from pyecharts.options import *

f = open("F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", 'r', encoding="GB2312")
f_data = f.readlines()
f.close()

f_data.pop(0)
data_list = {}
timeline = Timeline({"theme": ThemeType.LIGHT})
# 2017,巴巴多斯,4978000000
for x in f_data:
    year = int(x.split(",")[0])
    country = x.split(",")[1]
    gdp = float(x.split(",")[2])
    try:
        data_list[year].append((country, gdp))
    except KeyError:
        data_list[year] = []
        data_list[year].append((country, gdp))

year_list = sorted(data_list.keys())
for year in year_list:
    # print(f"{data_list[year]}")
    data_list[year].sort(key=lambda i: i[1], reverse=True)
    year_data = data_list[year][0:8]
    country_names = []
    gdps = []
    for z in year_data:
        country_names.append(z[0])
        gdps.append(int(z[1] / 100000000))
    bar = Bar()
    country_names.reverse()
    gdps.reverse()
    bar.set_global_opts(title_opts=TitleOpts(title=f"{year}年全球GDP前8国家"))
    bar.add_xaxis(country_names)
    bar.add_yaxis("GDP亿", gdps, label_opts=LabelOpts(position='right'))
    bar.reversal_axis()
    timeline.add(bar, str(year))

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
timeline.render("1960-2019全球GDP前8国家.html")

