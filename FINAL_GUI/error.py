# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_Error(object):

	def __init__(self, label):
		self._label = label

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(400, 192)
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(10, 20, 381, 161))
		self.label.setText("")
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "Message"))

	def setLabel(self):
		_translate = QtCore.QCoreApplication.translate
		self.label.setText(_translate("Dialog", self._label))
