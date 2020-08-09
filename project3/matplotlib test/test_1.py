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
from pyecharts.charts import Pie



Ui_MainWindow, QMainWindow = uic.loadUiType('project3/matplotlib test/test_1.ui')


class Main(QMainWindow,Ui_MainWindow) : 
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

    
    # plot된 figure를 컨테이너에 삽입하는 메소드
    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
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

    
    attr = ['A','B','C','D','E','F']
    v1 = [10, 20, 30, 40, 50, 60]
    v2 = [38, 28, 58, 48, 78, 68]
    pie = Pie("name", title_pos = 'center', width = '900')
    pie.add("A", attr, v1, center=[25, 50], is_random=True, radius=[30, 75], rosetype='radius')
    pie.add("B", attr, v2, center=[75, 50], is_randome=True, radius=[30, 75], rosetype='area', is_legend_show=False,
        is_label_show=True)

    # fig1 = Figure()
    # ax1f1 = fig1.add_subplot(111)
    # ax1f1.plot(np.random.rand(5))

    # fig2 = Figure()
    # #add_subplot >> 행x열x순서 (211)의 경우 아래로 2행 1열의 첫번째 요소라는 뜻.
    # ax1f2 = fig2.add_subplot(211)
    # ax1f2.plot(np.random.rand(5), ls='--')
    # ax2f2 = fig2.add_subplot(212)
    # ax2f2.plot(np.random.rand(10))
 
    
    main = Main()
    # main.addmpl(fig1)
    
    
    # input()
    # main.rmmpl()
    main.addmpl(pie)
    main.show()
    
    sys.exit(app.exec_())

    