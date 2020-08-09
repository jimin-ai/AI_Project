
import pyecharts.charts as cht
from pyecharts import options as opts

labels = ['수도권', '동남권', '충청권', '호남권', '대경권', '강원권', '제주']
ratio = [50.10, 15.26, 10.67, 9.89, 9.81, 2.97, 1.29]

pie = cht.Pie()
pie.add("대한민국 인구비율", list(zip(labels, ratio)), radius=150)
pie.set_global_opts(title_opts=opts.TitleOpts
(title="7대 권역별 인구비율", subtitle="2018-2019 기준"),toolbox_opts=opts.ToolboxOpts())
pie.render()