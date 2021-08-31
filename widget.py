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

            # create window layout
            self.QFrameObj = QFrame(self)
            self.QFrameObj.resize(width, height)
            self.QFrameObj.setStyleSheet("background-color: rgba(0, 0, 0, 60)")




# main process
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create an object of class myApp
    appWindow = App()
    # show the window
    App.show(appWindow)
    sys.exit(app.exec_()) 