import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
from matplotlib.figure import Figure
# Canvas : 플롯과 상호작용하기 위함.
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
import random
import numpy as np
from matplotlib import rcParams
import matplotlib.pyplot as plt

# import pyecharts.charts as cht
# from pyecharts import options as opts

Ui_MainWindow, QMainWindow = uic.loadUiType('project3/matplotlib test/test_1.ui')


class Main(QMainWindow,Ui_MainWindow) : 
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    
    # plot된 figure를 컨테이너에 삽입하는 메소드
    def addmpl(self):
        
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        #플롯을 포함한 figurecanvas의 위젯을 만듬.
        #addWidget은 레이아웃에 위젯을 추가하는 것을 말함.
        self.mplwindow.addWidget(self.canvas) 
        
        #plot을 그려줌.
        self.canvas.draw()  # plot 렌더링
        # 툴바 노출
        # self.toolbar = NavigationToolbar(self.canvas, 
        #         self.mplwindow, coordinates=True)
        # self.mplvl.addWidget(self.toolbar) 

    # 새로운 fiure를 노출시킬때 필요함.
    def rmmpl(self,):
        # 기존의 위젯을 지우고 새로운 위젯형태를 노출시킴.
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        # 툴바를 노출
        # self.mplvl.removeWidget(self.toolbar)
        # self.toolbar.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    labels = ['수도권', '동남권', '충청권', '호남권', '대경권', '강원권', '제주']
    ratio = [50.10, 15.26, 10.67, 9.89, 9.81, 2.97, 1.29]

    pie = cht.Pie()
    pie.add("대한민국 인구비율", list(zip(labels, ratio)), radius=150)
    pie.set_global_opts(title_opts=opts.TitleOpts(title="7대 권역별 인구비율", 
    subtitle="2018-2019 기준"),toolbox_opts=opts.ToolboxOpts())

    
 
    
    main = Main()
    # main.addmpl(fig1)
    
    
    # input()
    # main.rmmpl()
    main.addmpl(centre_circle)
    main.show()
    
    sys.exit(app.exec_())

    