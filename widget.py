import sys
import os
# custom weatherfile
import weather as w

# import neccesary Qt componenets
from PyQt5 import QtGui
from PyQt5.Qt import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QGridLayout, QFrame, QLabel, QHBoxLayout, QWidget, QVBoxLayout, QApplication

DEBUG_FLAG = w.DEBUG_FLAG

# 60000 ms = 1s,,, ease of readability to multiply
# you can't mess up the zeros here
EVENT_TIME_MS = 15 * 60000

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
            self.setWindowFlags( self.windowFlags() | Qt.WindowStaysOnBottomHint | Qt.FramelessWindowHint)

            # make window semi transparent so we can see under it still
            # but has bg for ease of text readability
            self.setAttribute(Qt.WA_TranslucentBackground, True)

            # main window layout
            self._layout = QGridLayout()

            # create QFrame "container" for translucent effect
            QFObj = QFrame(self)
            QFObj.resize(width, height)
            QFObj.setStyleSheet("background-color: rgba(0, 0, 0, 0.2);") # set transparency
            # create a sublayout to apply to qframe
            QFLayout = QHBoxLayout()
            # create central widget for sublayout
            QFWidget = QWidget()
            QFWidget.setStyleSheet("background: transparent; color: white;")   # add transparent rule so that we don't get overlapping sub-backgrounds
            QFWidget.setLayout(self._layout)    # appy main layout to central widget which then applies to QFLayout sublayout which applies to qframe container
            
            # add the central widget to the sublayout
            QFLayout.addWidget(QFWidget)    
            # set the sublayout to the qframe layout
            QFObj.setLayout(QFLayout)

            # call initalization functions
            self.initLayout()
            self.loadPixmaps()
            self.initScheduler()

            # intial call of weather function so it actually shows when the program loads vs waiting 30 seconds for the timer
            self.updateWeather()
        
        def initLayout(self) -> None:
            # create some label objects
            self.location = QLabel("Location")
            self.weatherIcon = QLabel()
            self.sky = QLabel("Sky Status")
            self.temp = QLabel("24")
            self.humidity = QLabel("Humidity")

            # create main layouts
            self._vBox1 = QVBoxLayout()
            self._vBox2 = QVBoxLayout()

            # set custom font
            QtGui.QFontDatabase.addApplicationFont("./assets/IBMPlexSans-Regular.ttf")

            _font = "IBM Plex Sans"

            # apply fonts to all objects
            self.location.setFont(QFont(_font, 20))
            self.sky.setFont(QFont(_font, 20))
            self.temp.setFont(QFont(_font, 30))
            self.humidity.setFont(QFont(_font, 20))
            self.weatherIcon.setFont(QFont(_font, 15))

            # align the widgets into correct positions via sublayouts
            self._vBox1.addWidget(self.location, alignment=Qt.AlignTop)
            self._vBox1.addWidget(self.weatherIcon, alignment=Qt.AlignVCenter)
            self._vBox2.addWidget(self.sky, alignment=Qt.AlignTop)
            self._vBox2.addWidget(self.temp, alignment=Qt.AlignVCenter)
            self._vBox2.addWidget(self.humidity, alignment=Qt.AlignBottom)

            # add sublayouts to main layout
            self._layout.addLayout(self._vBox1, 1, 1)
            self._layout.addLayout(self._vBox2, 1, 2)
        
        # setter function, as name says update the weather labels
        def updateLabels(self, location, sky, temp, humidity, iconCode) -> None:
            self.location.setText(location)
            self.sky.setText(sky)
            self.temp.setText(str(temp) + "C")
            self.humidity.setText(str(humidity) + "%")
            self.selectPixmap(iconCode)
        
        # load the pixmaps/icons from the local directory
        def loadPixmaps(self) -> None:
            self.pixmaps = {}
            for image in os.listdir("./assets/icons"):
                if image.endswith(".png"):
                    self.pixmaps[image] = QPixmap("./assets/icons/{file}".format(file=image)).scaledToHeight(150)
        
        # select the pixmap based on iconcode, if corresponding pixmap not found then show now icon available
        def selectPixmap(self, iconCode) -> None:
            pixmap = self.pixmaps.get(iconCode  + ".png", None)

            if DEBUG_FLAG: print(self.pixmaps)

            if pixmap is not None:
                self.weatherIcon.setPixmap(pixmap)
            elif iconCode.startswith("03"):
                self.weatherIcon.setPixmap(self.pixmaps["03"])
            elif iconCode.startswith("50"):
                self.weatherIcon.setPixmap(self.pixmaps["50"])
            else:
                self.weatherIcon.setText("No icon available")
        
        # setup the QTimer for timed event calling ( in this case updateWeather())
        def initScheduler(self):
            timer = QTimer(self)
            timer.timeout.connect(self.updateWeather)
            timer.start(EVENT_TIME_MS)

        # call weather function from external file
        def updateWeather(self):
            weather = w.getWeather()

            if DEBUG_FLAG: print("updating")

            if weather is not None:
                self.updateLabels(weather[0], weather[1].capitalize(), weather[2], weather[3], weather[4])

        def hideEvent(self, a0: QtGui.QHideEvent) -> None:
            if self.isMinimized():
                self.showNormal()
            else:
                pass
            return super().hideEvent(a0)
# main process
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # create an object of class myApp
    appWindow = App()
    # show the window
    App.show(appWindow)

    sys.exit(app.exec_()) 
