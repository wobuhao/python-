
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts, InitOpts, AxisOpts, LegendOpts

# 美国数据
f_us = open("F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/折线图数据/美国.txt", 'r', encoding='UTF-8')
us_data = f_us.read()
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
us_dict = json.loads(us_data[:-2])
us_trend_data = us_dict['data'][0]['trend']
us_x_data = us_trend_data['updateDate'][:314]
us_y_data = us_trend_data['list'][0]['data'][:314]

# 日本数据
f_jp = open("F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/折线图数据/日本.txt", 'r', encoding='UTF-8')
jp_data = f_jp.read()
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
jp_dict = json.loads(jp_data[:-2])
jp_trend_data = jp_dict['data'][0]['trend']
jp_x_data = jp_trend_data['updateDate'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]

# 印度数据
f_in = open("F:/python/1、Python快速入门（8天零基础入门到精通）/资料/第1-12章资料/资料/可视化案例数据/折线图数据/印度.txt", 'r', encoding='UTF-8')
in_data = f_in.read()
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
in_dict = json.loads(in_data[:-2])
in_trend_data = in_dict['data'][0]['trend']
in_x_data = in_trend_data['updateDate'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

line = Line(init_opts=InitOpts(width='800px', height='800px'))
line.add_xaxis(xaxis_data=us_x_data)
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

line.set_global_opts(
    title_opts=TitleOpts(title="确诊人数对比图", pos_left='center', pos_bottom='1%'),
    yaxis_opts=AxisOpts(name="累计确诊人数"),
    xaxis_opts=AxisOpts(name="时间"),
    legend_opts=LegendOpts(pos_left='50%')
)

line.render()

f_us.close()
f_jp.close()
f_in.close()