# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'karaoke.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 470)
        MainWindow.setMinimumSize(QtCore.QSize(510, 470))
        MainWindow.setMaximumSize(QtCore.QSize(510, 470))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.slider_Years = QtWidgets.QSlider(self.centralwidget)
        self.slider_Years.setGeometry(QtCore.QRect(39, 210, 421, 20))
        self.slider_Years.setMaximum(5)
        self.slider_Years.setPageStep(1)
        self.slider_Years.setSliderPosition(0)
        self.slider_Years.setTracking(False)
        self.slider_Years.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Years.setObjectName("slider_Years")
        self.label_Years = QtWidgets.QLabel(self.centralwidget)
        self.label_Years.setGeometry(QtCore.QRect(20, 190, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(13)
        self.label_Years.setFont(font)
        self.label_Years.setTextFormat(QtCore.Qt.AutoText)
        self.label_Years.setObjectName("label_Years")
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        self.label_Title.setGeometry(QtCore.QRect(140, 9, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(18)
        self.label_Title.setFont(font)
        self.label_Title.setScaledContents(False)
        self.label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Title.setObjectName("label_Title")
        self.pushButton_Random = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Random.setGeometry(QtCore.QRect(160, 60, 181, 17))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        self.pushButton_Random.setFont(font)
        self.pushButton_Random.setObjectName("pushButton_Random")
        self.label_Random = QtWidgets.QLabel(self.centralwidget)
        self.label_Random.setGeometry(QtCore.QRect(140, 40, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(8)
        self.label_Random.setFont(font)
        self.label_Random.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Random.setObjectName("label_Random")
        self.label_Instructions = QtWidgets.QLabel(self.centralwidget)
        self.label_Instructions.setGeometry(QtCore.QRect(60, 150, 361, 20))
        font = QtGui.QFont()
        font.setFamily("Eras Medium ITC")
        font.setPointSize(8)
        self.label_Instructions.setFont(font)
        self.label_Instructions.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Instructions.setObjectName("label_Instructions")
        self.label_Song = QtWidgets.QLabel(self.centralwidget)
        self.label_Song.setGeometry(QtCore.QRect(60, 80, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(12)
        self.label_Song.setFont(font)
        self.label_Song.setAutoFillBackground(False)
        self.label_Song.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Song.setText("")
        self.label_Song.setObjectName("label_Song")
        self.slider_Range = QtWidgets.QSlider(self.centralwidget)
        self.slider_Range.setGeometry(QtCore.QRect(40, 270, 421, 20))
        self.slider_Range.setMaximum(5)
        self.slider_Range.setPageStep(1)
        self.slider_Range.setSliderPosition(0)
        self.slider_Range.setTracking(False)
        self.slider_Range.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Range.setObjectName("slider_Range")
        self.label_Range = QtWidgets.QLabel(self.centralwidget)
        self.label_Range.setGeometry(QtCore.QRect(20, 250, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(13)
        self.label_Range.setFont(font)
        self.label_Range.setTextFormat(QtCore.Qt.AutoText)
        self.label_Range.setObjectName("label_Range")
        self.label_RangeQ = QtWidgets.QLabel(self.centralwidget)
        self.label_RangeQ.setGeometry(QtCore.QRect(20, 230, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(8)
        self.label_RangeQ.setFont(font)
        self.label_RangeQ.setAlignment(QtCore.Qt.AlignCenter)
        self.label_RangeQ.setObjectName("label_RangeQ")
        self.label_YearsQ = QtWidgets.QLabel(self.centralwidget)
        self.label_YearsQ.setGeometry(QtCore.QRect(60, 170, 361, 20))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(8)
        self.label_YearsQ.setFont(font)
        self.label_YearsQ.setAlignment(QtCore.Qt.AlignCenter)
        self.label_YearsQ.setObjectName("label_YearsQ")
        self.label_MoodQ = QtWidgets.QLabel(self.centralwidget)
        self.label_MoodQ.setGeometry(QtCore.QRect(30, 290, 421, 20))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(8)
        self.label_MoodQ.setFont(font)
        self.label_MoodQ.setAlignment(QtCore.Qt.AlignCenter)
        self.label_MoodQ.setObjectName("label_MoodQ")
        self.slider_Mood = QtWidgets.QSlider(self.centralwidget)
        self.slider_Mood.setGeometry(QtCore.QRect(40, 330, 421, 20))
        self.slider_Mood.setMaximum(5)
        self.slider_Mood.setPageStep(1)
        self.slider_Mood.setSliderPosition(0)
        self.slider_Mood.setTracking(False)
        self.slider_Mood.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Mood.setObjectName("slider_Mood")
        self.label_Mood = QtWidgets.QLabel(self.centralwidget)
        self.label_Mood.setGeometry(QtCore.QRect(20, 310, 471, 20))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(13)
        self.label_Mood.setFont(font)
        self.label_Mood.setTextFormat(QtCore.Qt.AutoText)
        self.label_Mood.setObjectName("label_Mood")
        self.checkBox_Duet = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Duet.setGeometry(QtCore.QRect(290, 350, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        self.checkBox_Duet.setFont(font)
        self.checkBox_Duet.setObjectName("checkBox_Duet")
        self.slider_Difficulty = QtWidgets.QSlider(self.centralwidget)
        self.slider_Difficulty.setGeometry(QtCore.QRect(40, 390, 171, 20))
        self.slider_Difficulty.setMaximum(2)
        self.slider_Difficulty.setPageStep(1)
        self.slider_Difficulty.setSliderPosition(0)
        self.slider_Difficulty.setTracking(False)
        self.slider_Difficulty.setOrientation(QtCore.Qt.Horizontal)
        self.slider_Difficulty.setObjectName("slider_Difficulty")
        self.label_DifficultyQ = QtWidgets.QLabel(self.centralwidget)
        self.label_DifficultyQ.setGeometry(QtCore.QRect(20, 350, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Eras Bold ITC")
        font.setPointSize(8)
        self.label_DifficultyQ.setFont(font)
        self.label_DifficultyQ.setAlignment(QtCore.Qt.AlignCenter)
        self.label_DifficultyQ.setObjectName("label_DifficultyQ")
        self.label_Difficulty = QtWidgets.QLabel(self.centralwidget)
        self.label_Difficulty.setGeometry(QtCore.QRect(30, 370, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(13)
        self.label_Difficulty.setFont(font)
        self.label_Difficulty.setTextFormat(QtCore.Qt.AutoText)
        self.label_Difficulty.setObjectName("label_Difficulty")
        self.pushButton_Song = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Song.setGeometry(QtCore.QRect(270, 376, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Eras Demi ITC")
        font.setPointSize(10)
        self.pushButton_Song.setFont(font)
        self.pushButton_Song.setObjectName("pushButton_Song")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_Years.setText(_translate("MainWindow", "...1960\'s    1970\'s       1980\'s       1990\'s       2000\'s       2010\'s..."))
        self.label_Title.setText(_translate("MainWindow", "Karaoke Roulette"))
        self.pushButton_Random.setText(_translate("MainWindow", "RANDOMIZER"))
        self.label_Random.setText(_translate("MainWindow", "Feeling lucky? Sing a totally random song!"))
        self.label_Instructions.setText(_translate("MainWindow", "...or you can help narrow it down by choosing from the following options:"))
        self.label_Range.setText(_translate("MainWindow", " Bass        Baritone        Tenor       Alto        Mezzo       Soprano"))
        self.label_RangeQ.setText(_translate("MainWindow", "How would you describe your vocal range? (Bass = Lowest, Soprano = Highest)"))
        self.label_YearsQ.setText(_translate("MainWindow", "What time period resonates with you the most?"))
        self.label_MoodQ.setText(_translate("MainWindow", "What\'s your mood?"))
        self.label_Mood.setText(_translate("MainWindow", "Deep      Confident      Happy     Hyper       Gritty        Unsure"))
        self.checkBox_Duet.setText(_translate("MainWindow", " Singing with others?"))
        self.label_DifficultyQ.setText(_translate("MainWindow", "Preferred song difficulty?"))
        self.label_Difficulty.setText(_translate("MainWindow", "Easy      Medium      Hard"))
        self.pushButton_Song.setText(_translate("MainWindow", "FIND MY SONG!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
