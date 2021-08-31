import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class App(QMainWindow):

        # class constructor
        def __init__(self) -> None:
            super().__init__()
            # window settings
            self.width = 600
            self.height = 250
            self.setWindowTitle("WidgetApp")
            self.setFixedSize(self.width, self.height)
            # change window starting pos to btm left
            qtRectangle = self.frameGeometry()
            centerPoint = QDesktopWidget().availableGeometry().bottomRight()
            qtRectangle.moveBottomRight(centerPoint)
            self.move(qtRectangle.topLeft())
            # force window to be abover any other objects (even taskbar or other windows being moved "above" this)
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

# main process
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create an object of class myApp
    appWindow = App()
    # show the window
    App.show(appWindow)
    sys.exit(app.exec_()) 