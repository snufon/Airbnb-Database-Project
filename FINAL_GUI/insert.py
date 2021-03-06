import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

def createComboBox_key(cur, table, col, tableWidget, index, addNone=False):
	cur.execute("select a." + col + " from " + table + " a order by a." + col)
	ids = np.array(cur.fetchall())[:,0]
	comboBox = QtWidgets.QComboBox(tableWidget)

	if addNone:
		ids = np.hstack(([""],ids))
	comboBox.addItems(ids.astype('str'))
	tableWidget.setCellWidget(index, 0, comboBox)

def createComboBox(tableWidget, index, values):
	comboBox = QtWidgets.QComboBox(tableWidget)
	comboBox.addItems(values)
	tableWidget.setCellWidget(index, 0, comboBox)

def createDateBox(tableWidget, index):
	dateEdit = QtWidgets.QDateEdit(tableWidget)
	tableWidget.setCellWidget(index, 0, dateEdit)
