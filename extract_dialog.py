# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\python\extract\extract_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1317, 824)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_dir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dir.setGeometry(QtCore.QRect(30, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_dir.setFont(font)
        self.pushButton_dir.setObjectName("pushButton_dir")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 600, 1281, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 60, 1271, 501))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setColumnCount(67)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(32, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(33, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(34, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(35, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(36, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(37, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(38, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(39, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(40, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(41, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(42, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(43, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(44, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(45, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(46, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(47, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(48, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(49, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(50, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(51, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(52, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(53, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(54, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(55, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(56, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(57, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(58, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(59, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(60, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(61, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(62, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(63, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(64, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(65, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(66, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(95)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(36)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 650, 1271, 121))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 570, 1271, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 630, 161, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(190, 4, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 191, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton_extr = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_extr.setFont(font)
        self.radioButton_extr.setChecked(True)
        self.radioButton_extr.setObjectName("radioButton_extr")
        self.horizontalLayout.addWidget(self.radioButton_extr)
        self.radioButton_kern = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.radioButton_kern.setChecked(False)
        self.radioButton_kern.setObjectName("radioButton_kern")
        self.horizontalLayout.addWidget(self.radioButton_kern)
        self.spinBox_round = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_round.setGeometry(QtCore.QRect(510, 20, 42, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_round.setFont(font)
        self.spinBox_round.setMaximum(15)
        self.spinBox_round.setProperty("value", 5)
        self.spinBox_round.setObjectName("spinBox_round")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_instr = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_instr.setGeometry(QtCore.QRect(1160, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_instr.setFont(font)
        self.pushButton_instr.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_instr.setObjectName("pushButton_instr")
        self.pushButton_fm = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_fm.setGeometry(QtCore.QRect(1020, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_fm.setFont(font)
        self.pushButton_fm.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_fm.setObjectName("pushButton_fm")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1317, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EXTRACT"))
        self.pushButton_dir.setText(_translate("MainWindow", "Выбрать директорию"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "номер образца"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "номер пробы"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Heptane (C7)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Octane (C8)"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Nonane (C9)"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Decane (C10) "))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Undecane (C11)"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Dodecane (C12)"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Tridecane (C13) "))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Tetradecane (C14)"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Pentadecane (C15) "))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Hexadecane (C16) "))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Heptadecane (C17)"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Pristane"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Octadecane (C18)  "))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Phytane"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Nonadecane (C19)"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Eicosane (C20)  "))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "Heneicosane (C21)  "))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "Docosane (C22) "))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "Tricosane (C23) "))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "Tetracosane (C24)   "))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "Pentacosane (C25) "))
        item = self.tableWidget.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "Hexacosane (C26)"))
        item = self.tableWidget.horizontalHeaderItem(24)
        item.setText(_translate("MainWindow", "Heptacosane (C27)"))
        item = self.tableWidget.horizontalHeaderItem(25)
        item.setText(_translate("MainWindow", "Octacosane (C28)  "))
        item = self.tableWidget.horizontalHeaderItem(26)
        item.setText(_translate("MainWindow", "Nonacosane (C29)"))
        item = self.tableWidget.horizontalHeaderItem(27)
        item.setText(_translate("MainWindow", "Triacontane (C30) "))
        item = self.tableWidget.horizontalHeaderItem(28)
        item.setText(_translate("MainWindow", "Hentriacontane (C31)"))
        item = self.tableWidget.horizontalHeaderItem(29)
        item.setText(_translate("MainWindow", "Dotriacontane (C32)"))
        item = self.tableWidget.horizontalHeaderItem(30)
        item.setText(_translate("MainWindow", "Tritriacontane (C33) "))
        item = self.tableWidget.horizontalHeaderItem(31)
        item.setText(_translate("MainWindow", "Tetratriacontane (C34)"))
        item = self.tableWidget.horizontalHeaderItem(32)
        item.setText(_translate("MainWindow", "Pentatriacontane (C35) "))
        item = self.tableWidget.horizontalHeaderItem(33)
        item.setText(_translate("MainWindow", "Hexatriacontane (C36) "))
        item = self.tableWidget.horizontalHeaderItem(34)
        item.setText(_translate("MainWindow", "Heptatriacontane (C37)"))
        item = self.tableWidget.horizontalHeaderItem(35)
        item.setText(_translate("MainWindow", "Octatriacontane (C38)"))
        item = self.tableWidget.horizontalHeaderItem(36)
        item.setText(_translate("MainWindow", "Nonatriacontane (C39)"))
        item = self.tableWidget.horizontalHeaderItem(37)
        item.setText(_translate("MainWindow", "Tetracontane (C40)"))
        item = self.tableWidget.horizontalHeaderItem(38)
        item.setText(_translate("MainWindow", "Pr/Ph"))
        item = self.tableWidget.horizontalHeaderItem(39)
        item.setText(_translate("MainWindow", "Pr/n-C17"))
        item = self.tableWidget.horizontalHeaderItem(40)
        item.setText(_translate("MainWindow", "Ph/n-C18"))
        item = self.tableWidget.horizontalHeaderItem(41)
        item.setText(_translate("MainWindow", "Ki"))
        item = self.tableWidget.horizontalHeaderItem(42)
        item.setText(_translate("MainWindow", "C27/C17"))
        item = self.tableWidget.horizontalHeaderItem(43)
        item.setText(_translate("MainWindow", "CPI nC19-nC23"))
        item = self.tableWidget.horizontalHeaderItem(44)
        item.setText(_translate("MainWindow", "CPI  nC17-nC21"))
        item = self.tableWidget.horizontalHeaderItem(45)
        item.setText(_translate("MainWindow", "CPI  nC19-nC25"))
        item = self.tableWidget.horizontalHeaderItem(46)
        item.setText(_translate("MainWindow", "CPI nC23-nC29"))
        item = self.tableWidget.horizontalHeaderItem(47)
        item.setText(_translate("MainWindow", "CPI nC23-nC33"))
        item = self.tableWidget.horizontalHeaderItem(48)
        item.setText(_translate("MainWindow", "OEP при nС19"))
        item = self.tableWidget.horizontalHeaderItem(49)
        item.setText(_translate("MainWindow", "OEP при nС21"))
        item = self.tableWidget.horizontalHeaderItem(50)
        item.setText(_translate("MainWindow", "OEP при nС23"))
        item = self.tableWidget.horizontalHeaderItem(51)
        item.setText(_translate("MainWindow", "OEP при nС25"))
        item = self.tableWidget.horizontalHeaderItem(52)
        item.setText(_translate("MainWindow", "OEP при nС27"))
        item = self.tableWidget.horizontalHeaderItem(53)
        item.setText(_translate("MainWindow", "OEP при nС29"))
        item = self.tableWidget.horizontalHeaderItem(54)
        item.setText(_translate("MainWindow", "CPI nC25-nC33"))
        item = self.tableWidget.horizontalHeaderItem(55)
        item.setText(_translate("MainWindow", "nC17/nC25 "))
        item = self.tableWidget.horizontalHeaderItem(56)
        item.setText(_translate("MainWindow", "nC16- nC22/nC23- nC29"))
        item = self.tableWidget.horizontalHeaderItem(57)
        item.setText(_translate("MainWindow", "nC35/nC34"))
        item = self.tableWidget.horizontalHeaderItem(58)
        item.setText(_translate("MainWindow", "nC15-nC20"))
        item = self.tableWidget.horizontalHeaderItem(59)
        item.setText(_translate("MainWindow", "nC21-nC30"))
        item = self.tableWidget.horizontalHeaderItem(60)
        item.setText(_translate("MainWindow", "nC15- nC20/nC21- nC30"))
        item = self.tableWidget.horizontalHeaderItem(61)
        item.setText(_translate("MainWindow", "nC16-nC22"))
        item = self.tableWidget.horizontalHeaderItem(62)
        item.setText(_translate("MainWindow", "nC23-nC29"))
        item = self.tableWidget.horizontalHeaderItem(63)
        item.setText(_translate("MainWindow", "nC15- nC17/nC22- nC24"))
        item = self.tableWidget.horizontalHeaderItem(64)
        item.setText(_translate("MainWindow", "nC25- nC33/nC26- nC34"))
        item = self.tableWidget.horizontalHeaderItem(65)
        item.setText(_translate("MainWindow", "nC11-nC18"))
        item = self.tableWidget.horizontalHeaderItem(66)
        item.setText(_translate("MainWindow", "nC15- nC19/nC25- nC29"))
        self.label.setText(_translate("MainWindow", "INFO"))
        self.label_2.setText(_translate("MainWindow", "Список ошибок:"))
        self.groupBox.setTitle(_translate("MainWindow", "Тип исследования"))
        self.radioButton_extr.setText(_translate("MainWindow", "экстракция"))
        self.radioButton_kern.setText(_translate("MainWindow", "керн"))
        self.label_3.setText(_translate("MainWindow", "знаков после\n"
"запятой:"))
        self.pushButton_instr.setText(_translate("MainWindow", "Инструкция"))
        self.pushButton_fm.setText(_translate("MainWindow", "Формулы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
