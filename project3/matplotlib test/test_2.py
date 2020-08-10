import sys
from pyecharts.charts import Pie   
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
from matplotlib.figure import Figure
import pyecharts.charts as cht
from pyecharts import options as opts

Ui_MainWindow, QMainWindow = uic.loadUiType('project3/matplotlib test/test_1.ui')


class Main(QMainWindow,Ui_MainWindow) :  
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initData()
        self.mainLayout()
        self.pushButton.clicked.connect(self.mainLayout)
 
    def initData(self):
        labels = ['수도권', '동남권', '충청권', '호남권', '대경권', '강원권', '제주']
        ratio = [50.10, 15.26, 10.67, 9.89, 9.81, 2.97, 1.29]

        pie = cht.Pie(opts.InitOpts(width='350px', height='350px'))
        pie.add("대한민국 인구비율", list(zip(labels, ratio)), radius=100)
        pie.set_global_opts(title_opts=opts.TitleOpts(),
        toolbox_opts=opts.ToolboxOpts(is_show=False), tooltip_opts = opts .TooltipOpts (is_show = False))
        pie.render()
 
    def mainLayout(self):
        self.we_view.close()
        self.we_view = QWebEngineView(self)
        self.we_view.load(QUrl("C:/Users/SMT049/Google Drive/프로젝트/개발/project/render.html")) 
        self.view_layout.addWidget(self.we_view)
        
        # self.setLayout(self.gridLayout)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())