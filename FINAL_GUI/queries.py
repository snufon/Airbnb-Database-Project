# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query1.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_1(object):

	def __init__(self, main_table, query):
		self._main_table = main_table
		self._query = query

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(400, 300)
		self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(50, 70, 201, 21))
		self.label.setObjectName("label")
		self.spinBox = QtWidgets.QSpinBox(Dialog)
		self.spinBox.setGeometry(QtCore.QRect(240, 70, 47, 24))
		self.spinBox.setObjectName("spinBox")
		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(50, 100, 201, 21))
		self.label_2.setObjectName("label_2")

		self.retranslateUi(Dialog)
		self.buttonBox.accepted.connect(Dialog.accept)
		self.buttonBox.rejected.connect(Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Query 1"))
		self.label.setText(_translate("Dialog", "Average price for listings with"))
		self.label_2.setText(_translate("Dialog", "bedrooms."))

	def setupFunc(self):
		self.buttonBox.accepted.connect(self.execute)

	def execute(self):
		self._query = self._query.replace("x1", self.spinBox.text())
		self._main_table.exec_query(self._query)

class Ui_Dialog_2(object):

	def __init__(self, main_table, query, values):
		self._main_table = main_table
		self._query = query
		self._values = values

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(400, 300)
		self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(80, 70, 241, 31))
		self.label.setObjectName("label")
		self.comboBox = QtWidgets.QComboBox(Dialog)
		self.comboBox.setGeometry(QtCore.QRect(80, 100, 241, 23))
		self.comboBox.setObjectName("comboBox")

		self.retranslateUi(Dialog)
		self.buttonBox.accepted.connect(Dialog.accept)
		self.buttonBox.rejected.connect(Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Query 2"))
		self.label.setText(_translate("Dialog", "Average cleaning score for listings with"))

	def setupFunc(self):
		self.comboBox.addItems(self._values)
		self.buttonBox.accepted.connect(self.execute)

	def execute(self):
		self._query = self._query.replace("x1", str(self.comboBox.currentText()))
		self._main_table.exec_query(self._query)

class Ui_Dialog_6(object):

	def __init__(self, main_table, query):
		self._main_table = main_table
		self._query = query

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(400, 300)
		self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
		self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(50, 70, 201, 21))
		self.label.setObjectName("label")
		self.spinBox = QtWidgets.QSpinBox(Dialog)
		self.spinBox.setGeometry(QtCore.QRect(240, 70, 47, 24))
		self.spinBox.setObjectName("spinBox1")
		self.spinBox.setValue(1)
		self.spinBox.setMaximum(99)

		self.label_2 = QtWidgets.QLabel(Dialog)
		self.label_2.setGeometry(QtCore.QRect(50, 100, 201, 21))
		self.label_2.setObjectName("label_2")

		self.retranslateUi(Dialog)
		self.buttonBox.accepted.connect(Dialog.accept)
		self.buttonBox.rejected.connect(Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Query 6"))
		self.label.setText(_translate("Dialog", "Hosts that have "))
		self.label_2.setText(_translate("Dialog", "listings."))

	def setupFunc(self):
		self.buttonBox.accepted.connect(self.execute)

	def execute(self):
		self._query = self._query.replace("x1", self.spinBox.text())
		self._main_table.exec_query(self._query)
