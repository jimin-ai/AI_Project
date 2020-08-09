
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
 
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
    
Ui_MainWindow, QMainWindow = uic.loadUiType("plot_test.ui")

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
 
if __name__ == '__main__':
    import sys
    from PyQt5 import QtGui
 
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())