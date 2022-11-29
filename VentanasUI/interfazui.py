# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 632)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(532, 632))
        MainWindow.setMaximumSize(QtCore.QSize(532, 632))
        MainWindow.setStyleSheet("QWidget{\n"
"    background-color: #f4f3ee;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    font: 18px tw-cent-mt #434343;\n"
"    border:  0.5px solid gray;\n"
"    border-radius: 4px;\n"
"    background-color: white;\n"
"    color: #434343;\n"
"    \n"
"}\n"
"\n"
"QLabel{\n"
"     color: #434343;\n"
"    font: bold 16px tw-cent-mt  #434343;\n"
"}\n"
"\n"
"QPushButton{\n"
"    font: bold 16px tw-cent-mt #434343;\n"
"    border:  0.5px solid #f4f3ee;\n"
"    border-radius: 5px;\n"
"    color:white;\n"
"}\n"
"\n"
"QTextEdit{\n"
"    background-color: white;\n"
"}\n"
"\n"
"QComboBox{\n"
"    background-color: white\n"
"}\n"
"\n"
"QSpinBox{\n"
"        background-color: white\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.txtID = QtWidgets.QLineEdit(self.centralwidget)
        self.txtID.setGeometry(QtCore.QRect(70, 40, 131, 31))
        #self.txtID.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txtID.setText("")
        self.txtID.setObjectName("txtID")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 40, 31, 31))
        self.label.setObjectName("label")
        self.cbNames = QtWidgets.QComboBox(self.centralwidget)
        self.cbNames.setGeometry(QtCore.QRect(30, 90, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbNames.setFont(font)
        self.cbNames.setObjectName("cbNames")
        self.spCant = QtWidgets.QSpinBox(self.centralwidget)
        self.spCant.setGeometry(QtCore.QRect(380, 40, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.spCant.setFont(font)
        self.spCant.setMinimum(1)
        self.spCant.setMaximum(20)
        self.spCant.setObjectName("spCant")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 40, 91, 31))
        self.label_2.setObjectName("label_2")
        self.btnAdmin = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdmin.setGeometry(QtCore.QRect(30, 592, 31, 31))
        self.btnAdmin.setStyleSheet("background-color: #32bea6;\n"
"border-radius: 15px;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdmin.setIcon(icon)
        self.btnAdmin.setIconSize(QtCore.QSize(26, 26))
        self.btnAdmin.setObjectName("btnAdmin")
        self.btnPaid = QtWidgets.QPushButton(self.centralwidget)
        self.btnPaid.setGeometry(QtCore.QRect(410, 590, 91, 31))
        self.btnPaid.setStyleSheet("background-color: #06d6a0;")
        self.btnPaid.setObjectName("btnPaid")
        self.btnOff = QtWidgets.QPushButton(self.centralwidget)
        self.btnOff.setGeometry(QtCore.QRect(490, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("tw-cent-mt #434343")
        font.setPointSize(1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnOff.setFont(font)
        self.btnOff.setStyleSheet("background-color: #ff4764;\n"
"border-radius: 15px")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnOff.setIcon(icon1)
        self.btnOff.setIconSize(QtCore.QSize(25, 25))
        self.btnOff.setObjectName("btnOff")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(280, 95, 71, 21))
        self.label_6.setObjectName("label_6")
        self.lbPrice = QtWidgets.QLabel(self.centralwidget)
        self.lbPrice.setGeometry(QtCore.QRect(360, 95, 101, 21))
        self.lbPrice.setText("")
        self.lbPrice.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbPrice.setObjectName("lbPrice")
        self.btnSearch = QtWidgets.QPushButton(self.centralwidget)
        self.btnSearch.setGeometry(QtCore.QRect(210, 40, 31, 31))
        self.btnSearch.setStyleSheet("background-color: #70d6ff;\n"
"border-radius: 15px")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSearch.setIcon(icon2)
        self.btnSearch.setObjectName("btnSearch")
        self.table = QtWidgets.QTableView(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(10, 170, 511, 411))
        self.table.setStyleSheet("background-color: white;")
        self.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table.setSortingEnabled(True)
        self.table.setObjectName("table")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(210, 600, 71, 21))
        self.label_7.setObjectName("label_7")
        self.lbTotal = QtWidgets.QLabel(self.centralwidget)
        self.lbTotal.setGeometry(QtCore.QRect(290, 600, 101, 21))
        self.lbTotal.setText("")
        self.lbTotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbTotal.setObjectName("lbTotal")
        self.btnAdd = QtWidgets.QPushButton(self.centralwidget)
        self.btnAdd.setGeometry(QtCore.QRect(480, 130, 31, 31))
        self.btnAdd.setStyleSheet("background-color: #2196f3;\n"
"border-radius: 15px")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnAdd.setIcon(icon3)
        self.btnAdd.setIconSize(QtCore.QSize(28, 28))
        self.btnAdd.setObjectName("btnAdd")
        self.btnDel = QtWidgets.QPushButton(self.centralwidget)
        self.btnDel.setGeometry(QtCore.QRect(430, 130, 31, 31))
        self.btnDel.setStyleSheet("background-color: #ec1c24;\n"
"border-radius: 15px")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDel.setIcon(icon4)
        self.btnDel.setIconSize(QtCore.QSize(28, 28))
        self.btnDel.setObjectName("btnDel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.cbNames.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Punto de Venta"))
        self.txtID.setPlaceholderText(_translate("MainWindow", "ID"))
        self.label.setText(_translate("MainWindow", "ID:"))
        self.label_2.setText(_translate("MainWindow", "Cantidad:"))
        self.btnAdmin.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.btnPaid.setText(_translate("MainWindow", "Pagar"))
        self.btnPaid.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.btnOff.setShortcut(_translate("MainWindow", "Esc"))
        self.label_6.setText(_translate("MainWindow", "Precio: $"))
        self.btnSearch.setShortcut(_translate("MainWindow", "Return"))
        self.label_7.setText(_translate("MainWindow", "Total: $"))
        self.btnAdd.setShortcut(_translate("MainWindow", "Return"))
        self.btnDel.setShortcut(_translate("MainWindow", "Return"))
