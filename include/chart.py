# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'charts.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtChart
import include.icon_rc

class Ui_WaveFormView(object):
    def setupW(self, WaveFormView):
        WaveFormView.setObjectName("WaveFormView")
        WaveFormView.resize(1015, 652)
        icon = QtGui.QIcon.fromTheme("oxygen")
        WaveFormView.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(WaveFormView)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.browserB = QtWidgets.QPushButton(self.centralwidget)
        self.browserB.setObjectName("browserB")
        self.gridLayout.addWidget(self.browserB, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        self.ChartViewLayout = QtWidgets.QVBoxLayout()
        self.ChartViewLayout.setObjectName("ChartViewLayout")
        self.chartview = QtChart.QChartView(self.centralwidget)
        self.chartview.setObjectName("chartview")
        self.ChartViewLayout.addWidget(self.chartview)
        self.gridLayout.addLayout(self.ChartViewLayout, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        WaveFormView.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WaveFormView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1015, 22))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        WaveFormView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WaveFormView)
        self.statusbar.setObjectName("statusbar")
        WaveFormView.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(WaveFormView)
        self.toolBar.setObjectName("toolBar")
        WaveFormView.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_Open = QtWidgets.QAction(WaveFormView)
        self.action_Open.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Humanity/actions/16/document-new.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open.setIcon(icon)
        self.action_Open.setObjectName("action_Open")
        self.action_Exit = QtWidgets.QAction(WaveFormView)
        self.action_Exit.setCheckable(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Humanity/actions/16/application-exit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon1)
        self.action_Exit.setObjectName("action_Exit")
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addAction(self.action_Exit)
        self.menu_Help.addSeparator()
        self.menu_Help.addSeparator()
        self.menu_Help.addSeparator()
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.action_Open)
        self.toolBar.addAction(self.action_Exit)

        self.retranslateUiW( WaveFormView )
        QtCore.QMetaObject.connectSlotsByName(WaveFormView)

    def retranslateUiW(self, WaveFormView):
        _translate = QtCore.QCoreApplication.translate
        WaveFormView.setWindowTitle(_translate("WaveFormView", "MainWindow"))
        self.browserB.setText(_translate("WaveFormView", "Open Folder"))
        self.menu_File.setTitle(_translate("WaveFormView", "&File"))
        self.menu_Help.setTitle(_translate("WaveFormView", "&Help"))
        self.toolBar.setWindowTitle(_translate("WaveFormView", "toolBar"))
        self.action_Open.setText(_translate("WaveFormView", "&Open"))
        self.action_Exit.setText(_translate("WaveFormView", "&Exit"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WaveFormView = QtWidgets.QMainWindow()
    ui = Ui_WaveFormView()
    ui.setupW( WaveFormView )
    WaveFormView.show()
    sys.exit(app.exec_())

