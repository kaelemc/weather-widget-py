import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class App(QMainWindow):

        # class constructor
        # basically just initialzing the main window
        def __init__(self) -> None:
            super().__init__()
            # window settings
            width = 600
            height = 250
            self.setFixedSize(width, height)
            # change window starting pos to btm left
            qtRectangle = self.frameGeometry()
            centerPoint = QDesktopWidget().availableGeometry().bottomRight()
            qtRectangle.moveBottomRight(centerPoint)
            self.move(qtRectangle.topLeft())
            # set window flags (there are multiple)
            #   1. init the window flags
            #   2. keep window at very top of any other windows always (even above taskbar)
            #   3. make window frameless so can't be moved
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)

            # make window semi transparent so we can see under it still
            # but has bg for ease of text readability
            self.setAttribute(Qt.WA_TranslucentBackground, True)

            # main window layout
            self._layout = QHBoxLayout()

            # create QFrame "container" for translucent effect
            QFObj = QFrame(self)
            QFObj.resize(width, height)
            QFObj.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);") # set transparency
            # create a sublayout to apply to qframe
            QFLayout = QHBoxLayout()
            # create central widget for sublayout
            QFWidget = QWidget()
            QFWidget.setStyleSheet("background: transparent")   # add transparent rule so that we don't get overlapping sub-backgrounds
            QFWidget.setLayout(self._layout)    # appy main layout to central widget which then applies to QFLayout sublayout which applies to qframe container
            
            # add the central widget to the sublayout
            QFLayout.addWidget(QFWidget)    

            # set the sublayout to the qframe layout
            QFObj.setLayout(QFLayout)   





# main process
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create an object of class myApp
    appWindow = App()
    # show the window
    App.show(appWindow)
    sys.exit(app.exec_()) 