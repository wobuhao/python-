from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar_data = [["a", 33], ["b", 55], ["c", 11]]
bar_data.sort(key=lambda i: i[1], reverse=True)
print(f"{bar_data}")
bar1 = Bar(init_opts=InitOpts())
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GPD", [30, 20, 10], label_opts=LabelOpts(position='right'))
bar1.reversal_axis()


bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GPD", [500, 220, 110], label_opts=LabelOpts(position='right'))
bar2.reversal_axis()

timeline = Timeline(
    {"theme": ThemeType.LIGHT}
)
timeline.add(bar1, "2023年GPD")
timeline.add(bar2, "2024年GPD")

timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True
)

timeline.render("基础柱状图.html")
