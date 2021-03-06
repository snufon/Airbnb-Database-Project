# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Query_without_parameters.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):

	def __init__(self, main_table, label, query):
		self._main_table = main_table
		self._text = label
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
		self.label.setGeometry(QtCore.QRect(20, 30, 361, 171))
		self.label.setText("")
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")

		self.retranslateUi(Dialog)
		self.buttonBox.accepted.connect(Dialog.accept)
		self.buttonBox.rejected.connect(Dialog.reject)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Non parametrizable"))

	def setLabel(self):
		_translate = QtCore.QCoreApplication.translate
		self.label.setText(_translate("Dialog", self._text))

	def setupFunc(self):
		self.buttonBox.accepted.connect(self.execute)

	def execute(self):
		self._main_table.exec_query(self._query)
