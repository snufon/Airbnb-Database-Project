# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_onglet.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from query_no_param import Ui_Dialog as Form
from queries import Ui_Dialog_1 as Query1
from queries import Ui_Dialog_2 as Query2
from queries import Ui_Dialog_6 as Query6
from error import Ui_Dialog_Error as Error
from insert import *
import numpy as np
import sys
import cx_Oracle

dateMap = {'01' : "JAN", '02' : "FEB", '03' : "MAR", '04' : "APR", '05' : "MAY", '06' : "JUN", '07' : "JUL", '08' : "AUG", '09' : "SEP", '10' : "OCT", '11' : "NOV", '12' : "DEC"}

class Ui_TabWidget(object):
	def __init__(self, con, cur):
		self._con = con
		self._cur = cur

		# QUERY PART #
		self._query_data = np.array([])
	
		# SEARCH PART #
		self._search_data = np.array([])

	def setupUi(self, TabWidget):
		TabWidget.setObjectName("TabWidget")
		TabWidget.setEnabled(True)
		TabWidget.resize(1054, 731)
		self.tab = QtWidgets.QWidget()
		self.tab.setObjectName("tab")
		self.table_search = QtWidgets.QTableWidget(self.tab)
		self.table_search.setGeometry(QtCore.QRect(10, 340, 1021, 351))
		self.table_search.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.table_search.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.table_search.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.table_search.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.table_search.setAlternatingRowColors(True)
		self.table_search.setRowCount(0)
		self.table_search.setColumnCount(0)
		self.table_search.setObjectName("table_search")
		self.dockWidget_4 = QtWidgets.QDockWidget(self.tab)
		self.dockWidget_4.setGeometry(QtCore.QRect(10, 10, 1031, 271))
		self.dockWidget_4.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
		self.dockWidget_4.setObjectName("dockWidget_4")
		self.dockWidgetContents_6 = QtWidgets.QWidget()
		self.dockWidgetContents_6.setObjectName("dockWidgetContents_6")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_6)
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.gridLayout_2 = QtWidgets.QGridLayout()
		self.gridLayout_2.setObjectName("gridLayout_2")
		self.radioButton_50 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_50.setObjectName("radioButton_50")
		self.gridLayout_2.addWidget(self.radioButton_50, 1, 1, 1, 1)
		self.radioButton_51 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_51.setObjectName("radioButton_51")
		self.gridLayout_2.addWidget(self.radioButton_51, 3, 2, 1, 1)
		self.radioButton_64 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_64.setObjectName("radioButton_64")
		self.gridLayout_2.addWidget(self.radioButton_64, 5, 2, 1, 1)
		self.radioButton_52 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_52.setObjectName("radioButton_52")
		self.gridLayout_2.addWidget(self.radioButton_52, 2, 1, 1, 1)
		self.radioButton_59 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_59.setObjectName("radioButton_59")
		self.gridLayout_2.addWidget(self.radioButton_59, 4, 1, 1, 1)
		self.radioButton_58 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_58.setObjectName("radioButton_58")
		self.gridLayout_2.addWidget(self.radioButton_58, 3, 1, 1, 1)
		self.radioButton_49 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_49.setObjectName("radioButton_49")
		self.gridLayout_2.addWidget(self.radioButton_49, 3, 0, 1, 1)
		self.radioButton_54 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_54.setObjectName("radioButton_54")
		self.gridLayout_2.addWidget(self.radioButton_54, 2, 2, 1, 1)
		self.radioButton_63 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_63.setObjectName("radioButton_63")
		self.gridLayout_2.addWidget(self.radioButton_63, 4, 2, 1, 1)
		self.radioButton_61 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_61.setObjectName("radioButton_61")
		self.gridLayout_2.addWidget(self.radioButton_61, 0, 1, 1, 1)
		self.radioButton_62 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_62.setObjectName("radioButton_62")
		self.gridLayout_2.addWidget(self.radioButton_62, 2, 0, 1, 1)
		self.radioButton_56 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_56.setObjectName("radioButton_56")
		self.gridLayout_2.addWidget(self.radioButton_56, 1, 0, 1, 1)
		self.radioButton_55 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_55.setChecked(True)
		self.radioButton_55.setObjectName("radioButton_55")
		self.gridLayout_2.addWidget(self.radioButton_55, 0, 0, 1, 1)
		self.radioButton_53 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_53.setObjectName("radioButton_53")
		self.gridLayout_2.addWidget(self.radioButton_53, 1, 2, 1, 1)
		self.radioButton_60 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_60.setObjectName("radioButton_60")
		self.gridLayout_2.addWidget(self.radioButton_60, 4, 0, 1, 1)
		self.label_6 = QtWidgets.QLabel(self.dockWidgetContents_6)
		self.label_6.setObjectName("label_6")
		self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)
		self.lineEdit_4 = QtWidgets.QLineEdit(self.dockWidgetContents_6)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.gridLayout_2.addWidget(self.lineEdit_4, 1, 3, 1, 1)
		self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(self.dockWidgetContents_6)
		self.commandLinkButton_2.setObjectName("commandLinkButton_2")
		self.gridLayout_2.addWidget(self.commandLinkButton_2, 2, 3, 1, 1)
		self.radioButton_57 = QtWidgets.QRadioButton(self.dockWidgetContents_6)
		self.radioButton_57.setObjectName("radioButton_57")
		self.gridLayout_2.addWidget(self.radioButton_57, 0, 2, 1, 1)
		self.verticalLayout_2.addLayout(self.gridLayout_2)
		self.dockWidget_4.setWidget(self.dockWidgetContents_6)
		self.label_8 = QtWidgets.QLabel(self.tab)
		self.label_8.setGeometry(QtCore.QRect(20, 320, 241, 16))
		self.label_8.setObjectName("label_8")
		self.spinBox_2 = QtWidgets.QSpinBox(self.tab)
		self.spinBox_2.setGeometry(QtCore.QRect(170, 290, 51, 24))
		self.spinBox_2.setMinimum(1)
		self.spinBox_2.setObjectName("spinBox_2")
		self.label_18 = QtWidgets.QLabel(self.tab)
		self.label_18.setGeometry(QtCore.QRect(230, 290, 61, 21))
		self.label_18.setObjectName("label_18")
		self.label_19 = QtWidgets.QLabel(self.tab)
		self.label_19.setGeometry(QtCore.QRect(20, 290, 151, 21))
		self.label_19.setObjectName("label_19")
		self.pushButton_26 = QtWidgets.QPushButton(self.tab)
		self.pushButton_26.setEnabled(False)
		self.pushButton_26.setGeometry(QtCore.QRect(530, 290, 80, 23))
		self.pushButton_26.setObjectName("pushButton_26")
		self.label_nb_result_search = QtWidgets.QLabel(self.tab)
		self.label_nb_result_search.setGeometry(QtCore.QRect(780, 320, 241, 16))
		self.label_nb_result_search.setObjectName("label_nb_result_search")
		self.label_21 = QtWidgets.QLabel(self.tab)
		self.label_21.setGeometry(QtCore.QRect(300, 290, 151, 21))
		self.label_21.setObjectName("label_21")
		self.spinBox_nb_rows_search = QtWidgets.QSpinBox(self.tab)
		self.spinBox_nb_rows_search.setGeometry(QtCore.QRect(460, 290, 51, 24))
		self.spinBox_nb_rows_search.setMinimum(10)
		self.spinBox_nb_rows_search.setValue(30)
		self.spinBox_nb_rows_search.setMaximum(50)
		self.spinBox_nb_rows_search.setSingleStep(20)
		self.spinBox_nb_rows_search.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
		self.spinBox_nb_rows_search.setObjectName("spinBox_nb_rows_search")
		TabWidget.addTab(self.tab, "")
		self.tab_3 = QtWidgets.QWidget()
		self.tab_3.setObjectName("tab_3")
		self.gridLayoutWidget = QtWidgets.QWidget(self.tab_3)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1021, 205))
		self.gridLayoutWidget.setObjectName("gridLayoutWidget")
		self.PredefinedQueries = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.PredefinedQueries.setContentsMargins(0, 0, 0, 0)
		self.PredefinedQueries.setObjectName("PredefinedQueries")
		self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_4.setObjectName("pushButton_4")
		self.PredefinedQueries.addWidget(self.pushButton_4, 3, 0, 1, 1)
		self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_7.setObjectName("pushButton_7")
		self.PredefinedQueries.addWidget(self.pushButton_7, 1, 1, 1, 1)
		self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_5.setObjectName("pushButton_5")
		self.PredefinedQueries.addWidget(self.pushButton_5, 2, 0, 1, 1)
		self.pushButton_11 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_11.setObjectName("pushButton_11")
		self.PredefinedQueries.addWidget(self.pushButton_11, 5, 1, 1, 1)
		self.pushButton_14 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_14.setObjectName("pushButton_14")
		self.PredefinedQueries.addWidget(self.pushButton_14, 2, 2, 1, 1)
		self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_9.setObjectName("pushButton_9")
		self.PredefinedQueries.addWidget(self.pushButton_9, 3, 1, 1, 1)
		self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_8.setObjectName("pushButton_8")
		self.PredefinedQueries.addWidget(self.pushButton_8, 2, 1, 1, 1)
		self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_6.setObjectName("pushButton_6")
		self.PredefinedQueries.addWidget(self.pushButton_6, 1, 0, 1, 1)
		self.pushButton_12 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_12.setObjectName("pushButton_12")
		self.PredefinedQueries.addWidget(self.pushButton_12, 1, 2, 1, 1)
		self.pushButton_17 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_17.setObjectName("pushButton_17")
		self.PredefinedQueries.addWidget(self.pushButton_17, 5, 2, 1, 1)
		self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_2.setObjectName("pushButton_2")
		self.PredefinedQueries.addWidget(self.pushButton_2, 5, 0, 1, 1)
		self.pushButton_13 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_13.setObjectName("pushButton_13")
		self.PredefinedQueries.addWidget(self.pushButton_13, 1, 3, 1, 1)
		self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_3.setObjectName("pushButton_3")
		self.PredefinedQueries.addWidget(self.pushButton_3, 4, 0, 1, 1)
		self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_10.setObjectName("pushButton_10")
		self.PredefinedQueries.addWidget(self.pushButton_10, 4, 1, 1, 1)
		self.pushButton_15 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_15.setObjectName("pushButton_15")
		self.PredefinedQueries.addWidget(self.pushButton_15, 3, 2, 1, 1)
		self.pushButton_16 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_16.setObjectName("pushButton_16")
		self.PredefinedQueries.addWidget(self.pushButton_16, 4, 2, 1, 1)
		self.pushButton_18 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_18.setObjectName("pushButton_18")
		self.PredefinedQueries.addWidget(self.pushButton_18, 6, 2, 1, 1)
		self.pushButton_19 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_19.setObjectName("pushButton_19")
		self.PredefinedQueries.addWidget(self.pushButton_19, 2, 3, 1, 1)
		self.pushButton_20 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_20.setObjectName("pushButton_20")
		self.PredefinedQueries.addWidget(self.pushButton_20, 3, 3, 1, 1)
		self.pushButton_21 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_21.setObjectName("pushButton_21")
		self.PredefinedQueries.addWidget(self.pushButton_21, 4, 3, 1, 1)
		self.pushButton_22 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_22.setObjectName("pushButton_22")
		self.PredefinedQueries.addWidget(self.pushButton_22, 5, 3, 1, 1)
		self.pushButton_23 = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.pushButton_23.setObjectName("pushButton_23")
		self.PredefinedQueries.addWidget(self.pushButton_23, 6, 3, 1, 1)
		self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
		self.label_3.setObjectName("label_3")
		self.PredefinedQueries.addWidget(self.label_3, 0, 0, 1, 2)
		self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
		self.label_4.setObjectName("label_4")
		self.PredefinedQueries.addWidget(self.label_4, 0, 2, 1, 2)
		self.table_predefined_queries = QtWidgets.QTableWidget(self.tab_3)
		self.table_predefined_queries.setGeometry(QtCore.QRect(10, 280, 1031, 411))
		self.table_predefined_queries.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.table_predefined_queries.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.table_predefined_queries.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.table_predefined_queries.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.table_predefined_queries.setAlternatingRowColors(True)
		self.table_predefined_queries.setObjectName("table_predefined_queries")
		self.table_predefined_queries.setColumnCount(0)
		self.table_predefined_queries.setRowCount(0)
		self.label_15 = QtWidgets.QLabel(self.tab_3)
		self.label_15.setGeometry(QtCore.QRect(10, 240, 151, 21))
		self.label_15.setObjectName("label_15")
		self.spinBox = QtWidgets.QSpinBox(self.tab_3)
		self.spinBox.setGeometry(QtCore.QRect(170, 240, 51, 24))
		self.spinBox.setMinimum(1)
		self.spinBox.setObjectName("spinBox")
		self.label_17 = QtWidgets.QLabel(self.tab_3)
		self.label_17.setGeometry(QtCore.QRect(230, 240, 61, 21))
		self.label_17.setObjectName("label_17")
		self.pushButton_25 = QtWidgets.QPushButton(self.tab_3)
		self.pushButton_25.setEnabled(False)
		self.pushButton_25.setGeometry(QtCore.QRect(530, 240, 80, 23))
		self.pushButton_25.setObjectName("pushButton_25")
		self.label_nb_result_query = QtWidgets.QLabel(self.tab_3)
		self.label_nb_result_query.setGeometry(QtCore.QRect(800, 260, 241, 16))
		self.label_nb_result_query.setObjectName("label_nb_result_qurey")
		self.spinBox_nb_rows_query = QtWidgets.QSpinBox(self.tab_3)
		self.spinBox_nb_rows_query.setGeometry(QtCore.QRect(470, 240, 51, 24))
		self.spinBox_nb_rows_query.setMinimum(10)
		self.spinBox_nb_rows_query.setMaximum(50)
		self.spinBox_nb_rows_query.setValue(30)
		self.spinBox_nb_rows_query.setSingleStep(20)
		self.spinBox_nb_rows_query.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
		self.spinBox_nb_rows_query.setObjectName("spinBox_nb_rows_query")
		self.label_20 = QtWidgets.QLabel(self.tab_3)
		self.label_20.setGeometry(QtCore.QRect(310, 240, 151, 21))
		self.label_20.setObjectName("label_20")
		TabWidget.addTab(self.tab_3, "")
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
		self.tableWidget.setGeometry(QtCore.QRect(330, 90, 701, 281))
		self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
		self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
		self.tableWidget.setObjectName("tableWidget")
		self.tableWidget.setColumnCount(0)
		self.tableWidget.setRowCount(0)
		self.pushButton = QtWidgets.QPushButton(self.tab_2)
		self.pushButton.setEnabled(False)
		self.pushButton.setGeometry(QtCore.QRect(330, 390, 701, 21))
		self.pushButton.setObjectName("pushButton")
		self.label = QtWidgets.QLabel(self.tab_2)
		self.label.setGeometry(QtCore.QRect(650, 40, 211, 31))
		self.label.setObjectName("label")
		self.dockWidget_6 = QtWidgets.QDockWidget(self.tab_2)
		self.dockWidget_6.setGeometry(QtCore.QRect(10, 70, 311, 601))
		self.dockWidget_6.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
		self.dockWidget_6.setObjectName("dockWidget_6")
		self.dockWidgetContents_8 = QtWidgets.QWidget()
		self.dockWidgetContents_8.setObjectName("dockWidgetContents_8")
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContents_8)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		self.radioButton_33 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_33.setChecked(True)
		self.radioButton_33.setObjectName("radioButton_33")
		self.verticalLayout_4.addWidget(self.radioButton_33)
		self.radioButton_34 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_34.setChecked(False)
		self.radioButton_34.setObjectName("radioButton_34")
		self.verticalLayout_4.addWidget(self.radioButton_34)
		self.radioButton_35 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_35.setCheckable(True)
		self.radioButton_35.setChecked(False)
		self.radioButton_35.setAutoRepeat(False)
		self.radioButton_35.setObjectName("radioButton_35")
		self.verticalLayout_4.addWidget(self.radioButton_35)
		self.radioButton_36 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_36.setChecked(False)
		self.radioButton_36.setObjectName("radioButton_36")
		self.verticalLayout_4.addWidget(self.radioButton_36)
		self.radioButton_37 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_37.setObjectName("radioButton_37")
		self.verticalLayout_4.addWidget(self.radioButton_37)
		self.radioButton_38 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_38.setObjectName("radioButton_38")
		self.verticalLayout_4.addWidget(self.radioButton_38)
		self.radioButton_39 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_39.setObjectName("radioButton_39")
		self.verticalLayout_4.addWidget(self.radioButton_39)
		self.radioButton_40 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_40.setObjectName("radioButton_40")
		self.verticalLayout_4.addWidget(self.radioButton_40)
		self.radioButton_41 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_41.setObjectName("radioButton_41")
		self.verticalLayout_4.addWidget(self.radioButton_41)
		self.radioButton_42 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_42.setObjectName("radioButton_42")
		self.verticalLayout_4.addWidget(self.radioButton_42)
		self.radioButton_43 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_43.setObjectName("radioButton_43")
		self.verticalLayout_4.addWidget(self.radioButton_43)
		self.radioButton_44 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_44.setObjectName("radioButton_44")
		self.verticalLayout_4.addWidget(self.radioButton_44)
		self.radioButton_45 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_45.setObjectName("radioButton_45")
		self.verticalLayout_4.addWidget(self.radioButton_45)
		self.radioButton_46 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_46.setObjectName("radioButton_46")
		self.verticalLayout_4.addWidget(self.radioButton_46)
		self.radioButton_47 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_47.setObjectName("radioButton_47")
		self.verticalLayout_4.addWidget(self.radioButton_47)
		self.radioButton_48 = QtWidgets.QRadioButton(self.dockWidgetContents_8)
		self.radioButton_48.setObjectName("radioButton_48")
		self.verticalLayout_4.addWidget(self.radioButton_48)
		self.btn_submit_insert_delete_3 = QtWidgets.QPushButton(self.dockWidgetContents_8)
		self.btn_submit_insert_delete_3.setObjectName("btn_submit_insert_delete_3")
		self.verticalLayout_4.addWidget(self.btn_submit_insert_delete_3)
		self.dockWidget_6.setWidget(self.dockWidgetContents_8)
		self.label_16 = QtWidgets.QLabel(self.tab_2)
		self.label_16.setGeometry(QtCore.QRect(60, 40, 161, 31))
		self.label_16.setObjectName("label_16")
		self.label_9 = QtWidgets.QLabel(self.tab_2)
		self.label_9.setGeometry(QtCore.QRect(590, 480, 211, 31))
		self.label_9.setObjectName("label_9")
		self.comboBox = QtWidgets.QComboBox(self.tab_2)
		self.comboBox.setGeometry(QtCore.QRect(330, 520, 701, 23))
		self.comboBox.setObjectName("comboBox")
		self.label_7 = QtWidgets.QLabel(self.tab_2)
		self.label_7.setGeometry(QtCore.QRect(650, 450, 59, 15))
		self.label_7.setObjectName("label_7")
		self.label_10 = QtWidgets.QLabel(self.tab_2)
		self.label_10.setGeometry(QtCore.QRect(660, 550, 59, 16))
		font = QtGui.QFont()
		font.setPointSize(30)
		self.label_10.setFont(font)
		self.label_10.setObjectName("label_10")
		self.lineEdit = QtWidgets.QLineEdit(self.tab_2)
		self.lineEdit.setGeometry(QtCore.QRect(330, 580, 701, 31))
		self.lineEdit.setObjectName("lineEdit")
		self.pushButton_24 = QtWidgets.QPushButton(self.tab_2)
		self.pushButton_24.setEnabled(False)
		self.pushButton_24.setGeometry(QtCore.QRect(330, 630, 701, 21))
		self.pushButton_24.setObjectName("pushButton_24")
		TabWidget.addTab(self.tab_2, "")

		self.retranslateUi(TabWidget)
		TabWidget.setCurrentIndex(0)
		QtCore.QMetaObject.connectSlotsByName(TabWidget)

	def retranslateUi(self, TabWidget):
		_translate = QtCore.QCoreApplication.translate
		TabWidget.setWindowTitle(_translate("TabWidget", "Database G06 Interface"))
		self.table_search.setSortingEnabled(True)
		self.radioButton_50.setText(_translate("TabWidget", "BedType"))
		self.radioButton_51.setText(_translate("TabWidget", "Calendars"))
		self.radioButton_64.setText(_translate("TabWidget", "ListingsHasAmenities"))
		self.radioButton_52.setText(_translate("TabWidget", "CancellationPolicy"))
		self.radioButton_59.setText(_translate("TabWidget", "ResponseTime"))
		self.radioButton_58.setText(_translate("TabWidget", "PropertyType"))
		self.radioButton_49.setText(_translate("TabWidget", "Amenities"))
		self.radioButton_54.setText(_translate("TabWidget", "Country"))
		self.radioButton_63.setText(_translate("TabWidget", "HostsHasVerifications"))
		self.radioButton_61.setText(_translate("TabWidget", "RoomType"))
		self.radioButton_62.setText(_translate("TabWidget", "Verifications"))
		self.radioButton_56.setText(_translate("TabWidget", "Listings"))
		self.radioButton_55.setText(_translate("TabWidget", "Hosts"))
		self.radioButton_53.setText(_translate("TabWidget", "City"))
		self.radioButton_60.setText(_translate("TabWidget", "Reviews"))
		self.label_6.setText(_translate("TabWidget", "Type to search..."))
		self.commandLinkButton_2.setText(_translate("TabWidget", "SEARCH"))
		self.radioButton_57.setText(_translate("TabWidget", "Neighborhoods"))
		self.label_8.setText(_translate("TabWidget", "SELECT A RESULT IN THE TAB BELOW:"))
		self.label_18.setText(_translate("TabWidget", "/"))
		self.label_19.setText(_translate("TabWidget", "SELECT PAGE NUMBER : "))
		self.pushButton_26.setText(_translate("TabWidget", "Go"))
		self.label_nb_result_search.setText(_translate("TabWidget", ""))
		self.label_21.setText(_translate("TabWidget", "NB ROWS PER PAGES :"))
		TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Search"))
		self.pushButton_4.setText(_translate("TabWidget", "Q3"))
		self.pushButton_7.setText(_translate("TabWidget", "Q6"))
		self.pushButton_5.setText(_translate("TabWidget", "Q2"))
		self.pushButton_11.setText(_translate("TabWidget", "Q10"))
		self.pushButton_14.setText(_translate("TabWidget", "Q12"))
		self.pushButton_9.setText(_translate("TabWidget", "Q8"))
		self.pushButton_8.setText(_translate("TabWidget", "Q7"))
		self.pushButton_6.setText(_translate("TabWidget", "Q1"))
		self.pushButton_12.setText(_translate("TabWidget", "Q11"))
		self.pushButton_17.setText(_translate("TabWidget", "Q15"))
		self.pushButton_2.setText(_translate("TabWidget", "Q5"))
		self.pushButton_13.setText(_translate("TabWidget", "Q17"))
		self.pushButton_3.setText(_translate("TabWidget", "Q4"))
		self.pushButton_10.setText(_translate("TabWidget", "Q9"))
		self.pushButton_15.setText(_translate("TabWidget", "Q13"))
		self.pushButton_16.setText(_translate("TabWidget", "Q14"))
		self.pushButton_18.setText(_translate("TabWidget", "Q16"))
		self.pushButton_19.setText(_translate("TabWidget", "Q18"))
		self.pushButton_20.setText(_translate("TabWidget", "Q19"))
		self.pushButton_21.setText(_translate("TabWidget", "Q20"))
		self.pushButton_22.setText(_translate("TabWidget", "Q21"))
		self.pushButton_23.setText(_translate("TabWidget", "Q22"))
		self.label_3.setText(_translate("TabWidget", "Simple queries"))
		self.label_4.setText(_translate("TabWidget", "Complex queries"))
		self.table_predefined_queries.setSortingEnabled(True)
		self.label_15.setText(_translate("TabWidget", "SELECT PAGE NUMBER : "))
		self.label_17.setText(_translate("TabWidget", "/"))
		self.pushButton_25.setText(_translate("TabWidget", "Go"))
		self.label_nb_result_query.setText(_translate("TabWidget", ""))
		self.label_20.setText(_translate("TabWidget", "NB ROWS PER PAGES :"))
		TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "Queries"))
		self.pushButton.setText(_translate("TabWidget", "Insert"))
		self.label.setText(_translate("TabWidget", "INSERTION"))
		self.radioButton_33.setText(_translate("TabWidget", "Hosts"))
		self.radioButton_34.setText(_translate("TabWidget", "Listings"))
		self.radioButton_35.setText(_translate("TabWidget", "Verifications"))
		self.radioButton_36.setText(_translate("TabWidget", "Amenities"))
		self.radioButton_37.setText(_translate("TabWidget", "Reviews"))
		self.radioButton_38.setText(_translate("TabWidget", "RoomType"))
		self.radioButton_39.setText(_translate("TabWidget", "BedType"))
		self.radioButton_40.setText(_translate("TabWidget", "CancellationPolicy"))
		self.radioButton_41.setText(_translate("TabWidget", "PropertyType"))
		self.radioButton_42.setText(_translate("TabWidget", "ResponseTime"))
		self.radioButton_43.setText(_translate("TabWidget", "Neighborhoods"))
		self.radioButton_44.setText(_translate("TabWidget", "City"))
		self.radioButton_45.setText(_translate("TabWidget", "Country"))
		self.radioButton_46.setText(_translate("TabWidget", "Calendars"))
		self.radioButton_47.setText(_translate("TabWidget", "HostsHasVerifications"))
		self.radioButton_48.setText(_translate("TabWidget", "ListingsHasAmenities"))
		self.btn_submit_insert_delete_3.setText(_translate("TabWidget", "Select"))
		self.label_16.setText(_translate("TabWidget", "SELECT TABLE TO UPDATE"))
		self.label_9.setText(_translate("TabWidget", "In choosen table, delete rows with"))
		self.label_7.setText(_translate("TabWidget", "DELETION"))
		self.label_10.setText(_translate("TabWidget", "="))
		self.pushButton_24.setText(_translate("TabWidget", "Delete"))
		TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "Insert/Delete"))

	def q1(self):
		query = "SELECT AVG(L.price) FROM Listings L WHERE L.bedrooms = x1"
		dialog = QtWidgets.QDialog()
		dialog.ui = Query1(self, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()

	def q2(self):
		query = "SELECT AVG(L.rs_cleanliness)\
			FROM Listings L, ListingsHasAmenities LA, Amenities A\
			WHERE L.lid = LA.lid AND LA.aid = A.aid AND A.ANAME = 'x1'"
		dialog = QtWidgets.QDialog()
		values = np.array(self._cur.execute("select a.aname from amenities a order by a.aname").fetchall())[:,0]
		dialog.ui = Query2(self, query, values)
		dialog.ui.setupUi(dialog)
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()

	def q3(self):
		query = "SELECT DISTINCT L.host_id\
			FROM Listings L\
			WHERE  L.lid IN (\
			SELECT Cal.lid\
			FROM Calendars Cal\
			WHERE Cal.available = 't' AND Cal.cdate BETWEEN TO_DATE('2019-03-01', 'YYYY-MM-DD') AND TO_DATE('2019-09-30', 'YYYY-MM-DD'))"
		label = "Hosts with available property\n between date 03.2019 and 09.2019."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()

	def q4(self):
		query = "SELECT COUNT(L.lid)\
			FROM  Listings L\
			WHERE L.host_id IN (\
		  	SELECT DISTINCT H1.hid\
		  	FROM Hosts H1, Hosts H2\
		  	WHERE H1.hid != H2.hid AND H1.name = H2.name)"
		label = "Number of listing items posted by two different hosts\n which have the same name."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()

	def q5(self):
		query = "SELECT DISTINCT Cal.cdate\
			FROM Calendars Cal\
			WHERE Cal.available = 't' AND Cal.lid IN (SELECT L.lid\
			FROM Listings L , Hosts H\
			WHERE L.host_id=H.hid AND H.name='Viajes Eco')"
		label = "Dates Host 'Viajes Eco' has available accommodations\n for rent."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()

	def q6(self):
		query = "SELECT H.hid, H.name\
			FROM Hosts H\
			WHERE H.hid IN (\
			  SELECT L.host_id\
			  FROM Listings L\
			  GROUP BY L.host_id\
			  HAVING COUNT(*) = x1\
			)"
		dialog = QtWidgets.QDialog()
		dialog.ui = Query6(self, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()

	def q7(self):
		query = "SELECT Wifi.PRICE - noWifi.PRICE\
			FROM(\
			SELECT AVG(L.price) AS PRICE\
			FROM Listings L, ListingsHasAmenities LHA, Amenities A\
			WHERE L.lid = LHA.lid AND LHA.aid = A.aid AND A.aname = 'Wifi') Wifi,\
			\
			(SELECT AVG(L.price) AS PRICE\
			FROM Listings L\
			WHERE L.lid NOT IN (\
			  SELECT LHA.lid\
			  FROM ListingsHasAmenities LHA, Amenities A\
			  WHERE LHA.aid = A.aid AND A.aname = 'Wifi'\
			)) noWifi"
		label = "Difference in the average price of listings with and\n without Wifi."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q8(self):
		query = "SELECT BERLIN.PRICE - MADRID.PRICE\
			FROM(\
			SELECT AVG(L.price) AS PRICE\
			FROM Listings L, Neighborhoods N, City C\
			WHERE L.bedrooms = 8  AND L.neighborhood_id = N.nid AND N.city_id = C.city_id AND C.city_name = 'berlin' ) BERLIN,\
			\
			(\
			SELECT AVG(L.price) AS PRICE\
			FROM Listings L, Neighborhoods N, City C\
			WHERE L.bedrooms = 8  AND L.neighborhood_id = N.nid AND N.city_id = C.city_id AND C.city_name = 'madrid' ) MADRID"
		label = "Difference to rent a room with 8 beds\n between Berlin and Madrid."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q9(self):
		query = "SELECT * FROM (\
			\
			SELECT H.hid, H.name\
			FROM Hosts H\
			LEFT JOIN Listings L ON L.host_id = H.hid\
			WHERE H.neighborhood_id IN (\
				SELECT N.nid\
				FROM Neighborhoods N, City C, Country Co\
				WHERE N.city_id=C.city_id AND C.country_id=Co.country_id AND Co.country_code = 'ES'\
			)\
			GROUP BY H.hid, H.name\
			ORDER BY COUNT(*) DESC\
			)\
			WHERE ROWNUM <= 10"
		label = "Top 10 hosts in Spain."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q10(self):
		query = "SELECT * FROM (\
		  SELECT L.lid, L.listing_name\
		  FROM Listings L, Neighborhoods N, City C, PropertyType P\
		  WHERE L.neighborhood_id = N.nid AND N.city_id = C.city_id AND C.city_name = 'barcelona' AND L.rs_rating >= 0\
		  AND L.property_type_id = P.prop_id AND P.property_type = 'Apartment'\
		  ORDER BY L.rs_rating DESC\
		)\
		WHERE ROWNUM <= 10"
		label = "Top 10 rated apartments in Barcelona."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q11(self):
		query = "SELECT C.city_name, COUNT(*)\
			FROM City C, Neighborhoods N, Hosts H\
			WHERE H.neighborhood_id = N.nid AND N.city_id = C.city_id\
			AND H.hid IN (\
			  SELECT DISTINCT L.host_id\
			  FROM Listings L\
			  WHERE L.square_feet > 0\
			)\
			GROUP BY C.city_name\
			ORDER BY C.city_name"
		label = "Number of listing which declared the area of their\n property"
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q12(self):
		query = "SELECT * FROM (\
			  SELECT N.nid, N.neighborhood_name\
			  FROM Neighborhoods N, (\
			    SELECT Neighb_ratings.nid as Nid, Neighb_ratings.rating as median\
			    FROM (\
			      SELECT L.neighborhood_id as nid, COUNT(*) as nbr\
			      FROM Listings L, Neighborhoods N, City C\
			      WHERE L.rs_rating >= 0 AND L.neighborhood_id = N.nid AND N.city_id=C.city_id AND C.CITY_NAME = 'madrid'\
			      GROUP BY L.neighborhood_id\
			    ) Neighb_nbrListings,\
			    (\
			      SELECT L.neighborhood_id as nid, L.rs_rating as rating, row_number() over (partition by N.nid order by L.rs_rating DESC)\
				as rownbr\
			      FROM Listings L, Neighborhoods N, City C\
			      WHERE L.rs_rating >= 0 AND L.neighborhood_id = N.nid AND N.city_id=C.city_id AND C.CITY_NAME = 'madrid'\
			    ) Neighb_ratings\
			    WHERE Neighb_nbrListings.nid = Neighb_ratings.nid AND Neighb_ratings.rownbr = Neighb_nbrListings.nbr/2\
			  ) Neighb_medians\
			  WHERE N.nid = Neighb_medians.Nid\
			  ORDER BY Neighb_medians.median DESC\
			) WHERE ROWNUM <= 5"
		label = "Top 5 neighborhoods of listings in Madrid."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q13(self):
		query = "SELECT M.hid, M.name\
			FROM (\
			SELECT H.hid AS hid, H.name AS name, COUNT(*) as nbr_listings\
			FROM Hosts H, Listings L\
			WHERE H.hid = L.host_id\
			GROUP BY H.hid, H.name\
			ORDER BY COUNT(*) DESC\
			\
			) M\
			WHERE( M.nbr_listings IN (SELECT * FROM (SELECT COUNT(*) as nbr_listings\
			FROM Hosts H, Listings L\
			WHERE H.hid = L.host_id\
			GROUP BY H.hid, H.name\
			ORDER BY COUNT(*) DESC\
			\
			) M2 WHERE ROWNUM = 1))"
		label = "Hosts with the highest number of listings."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q14(self):
		query = "SELECT * FROM(\
			SELECT selected.LID, selected.NAME\
			FROM CALENDARS Cal\
			LEFT OUTER JOIN(\
			SELECT L.LID AS LID, L.LISTING_NAME AS NAME\
			FROM Listings L\
			LEFT OUTER JOIN propertytype P ON P.prop_id = L.PROPERTY_TYPE_ID\
			LEFT OUTER JOIN NEIGHBORHOODS N ON L.NEIGHBORHOOD_ID = N.NID\
			LEFT OUTER JOIN City C ON N.city_id = C.city_id\
			LEFT OUTER JOIN CANCELLATIONPOLICY CP ON L.CANCELLATION_POLICY_ID = CP.CP_ID\
			WHERE P.PROPERTY_TYPE = 'Apartment' AND C.CITY_NAME = 'berlin'\
			AND L.BEDS >= 2 AND L.RS_RLOCATION >= 8 AND CP.CANCELLATION_POLICY = 'flexible'\
			AND L.HOST_ID IN (SELECT HHV.HID\
					  FROM HOSTSHASVERIFICATIONS HHV, VERIFICATIONS V\
					  WHERE HHV.VID = V.VID AND V.VNAME = 'government_id')\
			) selected ON selected.LID = Cal.LID\
			WHERE Cal.AVAILABLE = 't' AND Cal.cdate BETWEEN TO_DATE('2019-03-01', 'YYYY-MM-DD') AND TO_DATE('2019-04-30', 'YYYY-MM-DD')\
			GROUP BY selected.LID, selected.NAME\
			ORDER BY AVG (Cal.PRICE) DESC\
			) WHERE ROWNUM <= 5"
		label = "5 most cheapest Apartments in Berlin available\nbetween 01-03-2019 and 30-04-2019 having\nat least 2 beds, a location review score\nof at leat 8, flexible cancellation\nand listed by a host with a verifiable government id."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q15(self):
		query = "SELECT rs.ACCOMMODATES, rs.LID, rs.LISTING_NAME, rs.RS_RATING\
			  FROM(\
			    SELECT L.ACCOMMODATES, L.LID, L.LISTING_NAME, L.RS_RATING, ROW_NUMBER () over (Partition BY L.ACCOMMODATES ORDER BY L.RS_RATING DESC NULLS LAST) AS rownumber\
			      FROM(\
				SELECT list_with_amenities.LID\
				  FROM(\
				    SELECT LHA.LID AS LID, COUNT(*) AS nbr_facilities\
				      FROM LISTINGSHASAMENITIES LHA LEFT OUTER JOIN AMENITIES A ON LHA.AID = A.AID\
				      WHERE A.ANAME = 'Wifi' OR A.ANAME = 'Internet' OR A.ANAME = 'TV' OR A.ANAME = 'Free street parking'\
				      GROUP BY LHA.LID\
				  ) list_with_amenities\
				  WHERE list_with_amenities.nbr_facilities >= 2\
			      ) selected INNER JOIN LISTINGS L ON selected.LID = L.LID\
			  ) rs WHERE rs.rownumber <= 5"
		label = "Top 5 rated listings for each accomodate\ncategory (number of people) with a least\ntwo of these facilities: Widi, Internet, TV,\nFree street parking."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q16(self):
		query = "SELECT rs.HOST_ID, rs.total_reviews, rs.LID, rs.LISTING_NAME\
			  FROM(\
			    SELECT reduced_listings.HOST_ID, reduced_listings.LID, reduced_listings.LISTING_NAME, reduced_reviews.total_reviews,\
				    ROW_NUMBER () OVER (PARTITION BY reduced_listings.HOST_ID ORDER BY reduced_reviews.total_reviews DESC) AS row_number\
			      FROM\
				(SELECT L.LID, L.HOST_ID, L.LISTING_NAME\
				FROM LISTINGS L) reduced_listings\
				INNER JOIN\
				(SELECT R.LID, COUNT(*) AS total_reviews\
				FROM REVIEWS R\
				GROUP BY R.LID) reduced_reviews\
				ON reduced_listings.LID = reduced_reviews.LID\
			      ORDER BY reduced_listings.HOST_ID) rs\
			  WHERE row_number <= 3"
		label = "Three busiest listings per host"
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q17(self):
		query = "SELECT rs.NID, rs.NEIGHBORHOOD_NAME, rs.AID, rs.ANAME\
			  FROM(\
			    SELECT count.AID, count.ANAME, count.NID, count.NEIGHBORHOOD_NAME,\
			    ROW_NUMBER() over (PARTITION BY count.NID ORDER BY count.total DESC) AS row_number\
			      FROM(\
				SELECT inner_ln.NID, inner_ln.NEIGHBORHOOD_NAME, LHM.AID, A.ANAME, COUNT(*) AS total\
				FROM(\
				  SELECT L.LID, N.NID, N.NEIGHBORHOOD_NAME\
				  FROM LISTINGS L INNER JOIN NEIGHBORHOODS N on L.NEIGHBORHOOD_ID = N.NID\
						  INNER JOIN CITY C ON N.CITY_ID = C.CITY_ID\
						  INNER JOIN ROOMTYPE RT ON RT.ROOM_ID = L.ROOM_TYPE_ID\
				  WHERE RT.ROOM_TYPE = 'Private room' AND C.CITY_NAME = 'berlin') inner_ln\
				INNER JOIN\
				LISTINGSHASAMENITIES LHM ON inner_ln.LID = LHM.LID\
				INNER JOIN\
				AMENITIES A ON LHM.AID = A.AID\
				GROUP BY inner_ln.NID, LHM.AID, A.ANAME, inner_ln.NEIGHBORHOOD_NAME) count\
			      ORDER BY count.NID) rs\
			  WHERE rs.row_number <= 3"
		label = "Three most frequently used amenities at each \nneighborhood in Berlin for the listings with 'Private Room'."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q18(self):
		query = "SELECT most_diverse_scores.avrg - least_diverse_scores.avrg\
			FROM (\
			  SELECT AVG(L.rs_communication) as avrg\
			  FROM Listings L, (\
			    SELECT diverse_hosts.hid as hid\
			    FROM (\
			      SELECT HHV.hid as hid\
			      FROM HostsHasVerifications HHV\
			      WHERE HHV.hid IN (\
				SELECT DISTINCT L.host_id\
				FROM Listings L\
				WHERE L.rs_communication >= 0\
				GROUP BY L.host_id\
				HAVING COUNT(*) > 10\
			      )\
			      GROUP BY HHV.HID\
			      ORDER BY COUNT(*) DESC\
			    ) diverse_hosts\
			    WHERE ROWNUM = 1\
			  ) most_diverse_host\
			  WHERE L.host_id = most_diverse_host.hid\
			) most_diverse_scores,\
			(\
			  SELECT AVG(L.rs_communication) as avrg\
			  FROM Listings L, (\
			    SELECT not_diverse_hosts.hid as hid\
			    FROM (\
			      SELECT DISTINCT L.host_id as hid\
			      FROM Listings L\
			      WHERE L.rs_communication >= 0\
			      AND L.host_id NOT IN (\
				SELECT DISTINCT HHV.hid\
				FROM HostsHasVerifications HHV\
			      )\
			    ) not_diverse_hosts\
			    WHERE ROWNUM = 1\
			  ) least_diverse_host\
			  WHERE L.host_id = least_diverse_host.hid\
			) least_diverse_scores"
		label = "Difference in the average communication review score\nof the host who has the most diverse way of verifications\nand of the host who has the least diverse way\nof verifications."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q19(self):
		query = "SELECT *\
			FROM (\
			  SELECT C.city_name\
			  FROM City C\
			  LEFT JOIN Neighborhoods N ON C.city_id = N.city_id\
			  LEFT JOIN Listings L ON N.nid = L.neighborhood_id\
			  LEFT JOIN REVIEWS R ON L.lid = R.lid\
			  WHERE L.room_type_id IN (\
			    SELECT rtype_accomodates.id\
			    FROM (\
			      SELECT L.room_type_id AS id, AVG(L.accommodates) AS avrg\
			      FROM Listings L\
			      GROUP BY L.room_type_id\
			    ) rtype_accomodates\
			    WHERE rtype_accomodates.avrg > 3\
			  )\
			  GROUP BY C.city_name\
			  ORDER BY COUNT(*) DESC\
			)\
			WHERE ROWNUM = 1"
		label = "City with the highest number of reviews for listings\nwhose average number of accommodates are greater\nthan 3."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q20(self):
		query = "SELECT N.nid, N.neighborhood_name\
			FROM Neighborhoods N, (\
			  SELECT L.neighborhood_id as nid, COUNT(*) as nbr\
			  FROM Listings L, Hosts H, Neighborhoods N, City C\
			  WHERE L.lid IN (\
			    SELECT DISTINCT Cal.lid\
			    FROM CALENDARS Cal\
			    WHERE Cal.cdate >= TO_DATE('2019-01-01', 'YYYY-MM-DD') AND Cal.available = 'f'\
			  ) AND L.host_id = H.hid AND H.since < TO_DATE('2017-06-01', 'YYYY-MM-DD') AND L.neighborhood_id = N.nid\
			  AND N.city_id = C.city_id AND C.city_name = 'madrid'\
			  GROUP BY L.neighborhood_id\
			) neighb_available, (\
			  SELECT L.neighborhood_id as nid, COUNT(*) as nbr\
			  FROM Listings L\
			  GROUP BY L.neighborhood_id\
			) neighb_total\
			WHERE N.nid = neighb_available.nid AND N.nid = neighb_total.nid AND 2*neighb_available.nbr >= neighb_total.nbr"
		label = "Neighborhoods in Madrid which have at least\n50 percent of their listings occupied at some date in year\n2019 and their host has joined airbnb before 01.06.2017."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q21(self):
		query = "SELECT C.country_name\
			FROM Country C, (\
			  SELECT C.country_id AS cid, COUNT(*) AS nbr\
			  FROM City C\
			  LEFT JOIN Neighborhoods N ON N.city_id = C.city_id\
			  LEFT JOIN Listings L ON N.nid = L.neighborhood_id\
			  WHERE L.lid IN (\
			    SELECT DISTINCT Cal.lid\
			    FROM Calendars Cal\
			    WHERE Cal.available = 't' AND Cal.cdate BETWEEN TO_DATE('2018-01-01', 'YYYY-MM-DD') AND TO_DATE('2018-12-31', 'YYYY-MM-DD')\
			  )\
			  GROUP BY C.country_id\
			) ctry_available, (\
			  SELECT C.country_id AS cid, COUNT(*) AS nbr\
			  FROM City C\
			  LEFT JOIN Neighborhoods N ON N.city_id = C.city_id\
			  LEFT JOIN Listings L ON N.nid = L.neighborhood_id\
			  GROUP BY C.country_id\
			) ctry_total\
			WHERE C.country_id = ctry_available.cid AND C.country_id = ctry_total.cid AND 5*ctry_available.nbr >= ctry_total.nbr"
		label = "Countries that had at least 20% of their listings\navailable in 2018."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def q22(self):
		query = "SELECT N.nid, N.neighborhood_name\
			FROM Neighborhoods N, (\
			  SELECT L.neighborhood_id AS nid, COUNT(*) as nbr\
			  FROM Listings L, Neighborhoods N, City C, CancellationPolicy CP\
			  WHERE L.neighborhood_id = N.nid AND N.city_id = C.city_id AND C.city_name = 'barcelona'\
			  AND L.cancellation_policy_id = CP.cp_id AND CP.cancellation_policy = 'strict_14_with_grace_period'\
			  GROUP BY L.neighborhood_id\
			) neighb_grace_period, (\
			  SELECT L.neighborhood_id AS nid, COUNT(*) as nbr\
			  FROM Listings L, Neighborhoods N, City C\
			  WHERE L.neighborhood_id = N.nid AND N.city_id = C.city_id AND C.city_name = 'barcelona'\
			  GROUP BY L.neighborhood_id\
			) neighb_total\
			WHERE N.nid = neighb_grace_period.nid AND N.nid = neighb_total.nid AND 20*neighb_grace_period.nbr >= neighb_total.nbr"
		label = "Neighborhoods in Barcelona where more than 5 percent\nof their accomodations's cancelation policy\nis strict with grace period."
		dialog = QtWidgets.QDialog()
		dialog.ui = Form(self, label, query)
		dialog.ui.setupUi(dialog)
		dialog.ui.setLabel()
		dialog.ui.setupFunc()
		dialog.exec_()
		dialog.show()


	def setup_func(self):
		"""
		Queries
		"""
		self.pushButton_6.clicked.connect(self.q1)
		self.pushButton_4.clicked.connect(self.q3)
		self.pushButton_7.clicked.connect(self.q6)
		self.pushButton_5.clicked.connect(self.q2)
		self.pushButton_11.clicked.connect(self.q10)
		self.pushButton_14.clicked.connect(self.q12)
		self.pushButton_9.clicked.connect(self.q8)
		self.pushButton_8.clicked.connect(self.q7)
		self.pushButton_12.clicked.connect(self.q11)
		self.pushButton_17.clicked.connect(self.q15)
		self.pushButton_2.clicked.connect(self.q5)
		self.pushButton_13.clicked.connect(self.q17)
		self.pushButton_3.clicked.connect(self.q4)
		self.pushButton_10.clicked.connect(self.q9)
		self.pushButton_15.clicked.connect(self.q13)
		self.pushButton_16.clicked.connect(self.q14)
		self.pushButton_18.clicked.connect(self.q16)
		self.pushButton_19.clicked.connect(self.q18)
		self.pushButton_20.clicked.connect(self.q19)
		self.pushButton_21.clicked.connect(self.q20)
		self.pushButton_22.clicked.connect(self.q21)
		self.pushButton_23.clicked.connect(self.q22)

		"""
		INSERT/DELETE
		"""
		self.btn_submit_insert_delete_3.clicked.connect(self.setup_insert_delete)
		self.pushButton.clicked.connect(self.insert)

		self._radio_buttons_insert_delete = [self.radioButton_33, self.radioButton_34, self.radioButton_35, self.radioButton_36, self.radioButton_37,	self.radioButton_38, self.radioButton_39, self.radioButton_40, self.radioButton_41, self.radioButton_42,self.radioButton_43, self.radioButton_44, self.radioButton_45, self.radioButton_46, self.radioButton_47,self.radioButton_48]

		self.pushButton_24.clicked.connect(self.delete)
		self.pushButton_25.clicked.connect(self.go_page)

		"""
		SEARCH
		"""
		self._radio_buttons_search = [self.radioButton_49, self.radioButton_50, self.radioButton_51, self.radioButton_52, self.radioButton_53,self.radioButton_54, self.radioButton_55, self.radioButton_56, self.radioButton_57, self.radioButton_58,self.radioButton_59, self.radioButton_60, self.radioButton_61, self.radioButton_62, self.radioButton_63,self.radioButton_64]

		self.commandLinkButton_2.clicked.connect(self.search)
		#self.table_search.cellClicked.connect(self.display_complete_row)

		self.pushButton_26.clicked.connect(self.go_page_2)

	"""
	SEARCH METHODS
	"""

	#TODO A EFFACER
	def display_complete_row(self, row, column):
		table = [x for x in self._radio_buttons_search if x.isChecked()][0].text()
		col_names = [row_x[0] for row_x in self._cur.description]
		idcol = col_names[0]
		myid = self.table_search.item(row, 0).text()
		query = "select * from " + table + " h where h." + idcol + " = " + myid
		self._cur.execute(query)
		res = np.array(self._cur.fetchall())
		self.display_table(self.table_search_2, res, 1)
	#FIN TODO

	def search(self):
		self.spinBox_2.setValue(1)
		self.spinBox_nb_rows_search.setValue(30)
		self.pushButton_26.setEnabled(True)
		_translate = QtCore.QCoreApplication.translate
		table = [x for x in self._radio_buttons_search if x.isChecked()][0].text()
		search_text = self.lineEdit_4.text().lower()
		self._cur.execute("select * from " + table + " where rownum = 1")
		col_names = [row[0] for row in self._cur.description]

		query_search = " OR ".join(["lower(h." + col +  ") like '%" + search_text + "%'" for col in col_names])
		query = "select * from " + table + " h where " + query_search
		self._cur.execute(query)
		self.search_data = np.array(self._cur.fetchall())
		plength = self.spinBox_nb_rows_search.value()
		nbr_pages = (self.search_data.shape[0] // plength) + 1
		self.spinBox_2.setMaximum(nbr_pages)
		self.label_nb_result_search.setText('Number of results : ' + str(self.search_data.shape[0]))
		self.label_18.setText(_translate("TabWidget", '/ ' + str(nbr_pages)))
		self.display_table(self.table_search, self.search_data, 1,plength)

	def go_page_2(self):
		_translate = QtCore.QCoreApplication.translate
		plength = self.spinBox_nb_rows_search.value()
		nbr_pages = (self.search_data.shape[0] // plength) + 1
		self.spinBox_2.setMaximum(nbr_pages)
		self.label_18.setText(_translate("TabWidget", '/ ' + str(nbr_pages)))
		self.display_table(self.table_search, self.search_data, self.spinBox_2.text(), self.spinBox_nb_rows_search.value())

	"""
	INSERT / DELETE METHODS
	"""
	def delete(self):
		try:
			table = [x for x in self._radio_buttons_insert_delete if x.isChecked()][0].text()
			text = "delete from " + table + " where " + str(self.comboBox.currentText()) + " = '" + self.lineEdit.text() + "'"
			self._cur.execute(text)
			self._con.commit()
			label = "OPERATION SUCCESSFULL !!"

		except cx_Oracle.IntegrityError as error:
				print("Caught an error : " + repr(error))
				label = "ERROR : OPERATION IMPOSSIBLE\nDUE TO INTEGRITY CONSTRAINT !\n\n"
				label += "TO DELETE THE DATA,\nREMOVE ALL ENTRIES IN OTHER TABLES\nUSING THIS TABLE DATA."

		except cx_Oracle.DatabaseError as error:
				print("Caught an error : " + repr(error))
				label = "ERROR : OPERATION IMPOSSIBLE\nDUE TO INVALID INPUT FORMAT !\n\n"
				label += "MAKE SURE TO ENTER A NUMBER IF WE EXPECT A NUMBER,\nA STRING IF WE EXPECT A STRING\nOR A DATE WITH FORMAT\nJJ-MMM-YYYY (MMM FOR 'JAN', 'FEB', ETC...)\nIF WE EXPECT A DATE."

		finally:
			dialog = QtWidgets.QDialog()
			dialog.ui = Error(label)
			dialog.ui.setupUi(dialog)
			dialog.ui.setLabel()
			dialog.exec_()
			dialog.show()		


	def insert(self):
		try:
			text = "insert into " + self.tableWidget.horizontalHeaderItem(0).text() + " values"
			headercount = self.tableWidget.rowCount()
			values = []
			for i in range(headercount):
				widget = self.tableWidget.cellWidget(i,0)
				type_name = widget.metaObject().className()
				if type_name == "QLineEdit":
					values.append(widget.text())
				if type_name == "QComboBox":
					values.append(str(widget.currentText()))
				if type_name == "QDateEdit":
					date = widget.date().toString("dd-MM-yy")
					date = date[:3] + dateMap[date[3:5]] + date[5:]
					values.append(date)
				if type_name == "QSpinBox":
					values.append(widget.text())				

			text += " ('" + "','".join(values) + "')"
			print(text)
			self._cur.execute(text)
			self._con.commit()
			label = "OPERATION SUCCESSFULL !!"

		except cx_Oracle.IntegrityError as error:
			print("Caught an error : " + repr(error))
			label = "ERROR : OPERATION IMPOSSIBLE\nDUE TO INTEGRITY CONSTRAINT\n\n"
			label += "MAKE SURE TO FILL EVERY ROW\nAND THE ID DOES NOT ALREADY EXIST."
	
		finally:
			dialog = QtWidgets.QDialog()
			dialog.ui = Error(label)
			dialog.ui.setupUi(dialog)
			dialog.ui.setLabel()
			dialog.exec_()
			dialog.show()	

	def setup_insert_delete(self):
		# INSERT SETUP #
		self.pushButton.setEnabled(True)
		self.tableWidget.setColumnCount(0)
		self.tableWidget.setRowCount(0)
		table = [x for x in self._radio_buttons_insert_delete if x.isChecked()][0].text()
		self._cur.execute("select * from " + table + " where rownum = 1")
		col_names = [row[0] for row in self._cur.description]
		col_names2 = [row[0] for row in self._cur.description if row[1] is not cx_Oracle.CLOB]
		self.tableWidget.setColumnCount(1)
		self.tableWidget.setRowCount(len(col_names))
		self.tableWidget.setVerticalHeaderLabels(col_names)
		self.tableWidget.setHorizontalHeaderLabels([table])
		self.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
		self.insert_user_friendly(table, col_names)

		# DELETE SETUP #
		self.pushButton_24.setEnabled(True)
		self.comboBox.clear()
		self.comboBox.addItems(col_names2)


	def insert_user_friendly(self, table, col_names):
		for i, col in enumerate(col_names):
				lineEdit = QtWidgets.QLineEdit(self.tableWidget)
				self.tableWidget.setCellWidget(i, 0, lineEdit)
		if table == 'Hosts':
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())
			createComboBox_key(self._cur, "neighborhoods", "nid", self.tableWidget, 1)
			createComboBox_key(self._cur, "responsetime", "resid", self.tableWidget, 2, addNone=True)
			createDateBox(self.tableWidget, 5)
			createComboBox(self.tableWidget, 6, np.hstack(([""], np.arange(0,101))).astype('str'))

		if table == "Listings":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())
			createComboBox_key(self._cur, "hosts", "hid", self.tableWidget, 1)
			createComboBox_key(self._cur, "neighborhoods", "nid", self.tableWidget, 2)
			createComboBox_key(self._cur, "cancellationpolicy", "cp_id", self.tableWidget, 3)
			createComboBox_key(self._cur, "bedtype", "bed_id", self.tableWidget, 4)
			createComboBox_key(self._cur, "roomtype", "room_id", self.tableWidget, 5)
			createComboBox_key(self._cur, "propertytype", "prop_id", self.tableWidget, 6)

			self.tableWidget.cellWidget(9,0).setValidator(QtGui.QDoubleValidator())
			self.tableWidget.cellWidget(10,0).setValidator(QtGui.QDoubleValidator())
			self.tableWidget.cellWidget(11,0).setValidator(QtGui.QDoubleValidator())
			self.tableWidget.cellWidget(12,0).setValidator(QtGui.QDoubleValidator())
			self.tableWidget.cellWidget(13,0).setValidator(QtGui.QDoubleValidator())
			self.tableWidget.cellWidget(14,0).setValidator(QtGui.QDoubleValidator())
			self.tableWidget.cellWidget(15,0).setValidator(QtGui.QDoubleValidator())
			self.tableWidget.cellWidget(16,0).setValidator(QtGui.QIntValidator())
			self.tableWidget.cellWidget(17,0).setValidator(QtGui.QDoubleValidator())
			self.tableWidget.cellWidget(18,0).setValidator(QtGui.QIntValidator())
			self.tableWidget.cellWidget(19,0).setValidator(QtGui.QIntValidator())
			self.tableWidget.cellWidget(20,0).setValidator(QtGui.QIntValidator())
			self.tableWidget.cellWidget(21,0).setValidator(QtGui.QDoubleValidator())
			self.tableWidget.cellWidget(22,0).setValidator(QtGui.QIntValidator())
			self.tableWidget.cellWidget(23,0).setValidator(QtGui.QIntValidator())
			self.tableWidget.cellWidget(24,0).setValidator(QtGui.QIntValidator())

			createComboBox(self.tableWidget, 25, np.hstack(([""], np.arange(0,101))).astype('str'))
			createComboBox(self.tableWidget, 26, np.hstack(([""], np.arange(0,11))).astype('str'))
			createComboBox(self.tableWidget, 27, np.hstack(([""], np.arange(0,11))).astype('str'))
			createComboBox(self.tableWidget, 28, np.hstack(([""], np.arange(0,11))).astype('str'))
			createComboBox(self.tableWidget, 29, np.hstack(([""], np.arange(0,11))).astype('str'))
			createComboBox(self.tableWidget, 30, np.hstack(([""], np.arange(0,11))).astype('str'))
			createComboBox(self.tableWidget, 31, np.hstack(([""], np.arange(0,11))).astype('str'))

			createComboBox(self.tableWidget, 32, np.array(["", "t", "f"]))
			createComboBox(self.tableWidget, 33, np.array(["", "t", "f"]))
			createComboBox(self.tableWidget, 34, np.array(["", "t", "f"]))

		if table == "Verifications":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())

		if table == "Amenities":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())

		if table == "Reviews":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())
			createComboBox_key(self._cur, "listings", "lid", self.tableWidget, 1)
			createDateBox(self.tableWidget, 2)
			self.tableWidget.cellWidget(3,0).setValidator(QtGui.QIntValidator())

		if table == "RoomType":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())

		if table == "BedType":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())

		if table == "CancellationPolicy":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())

		if table == "PropertyType":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())

		if table == "ResponseTime":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())

		if table == "Neighborhoods":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())
			createComboBox_key(self._cur, "city", "city_id", self.tableWidget, 1)

		if table == "City":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())
			createComboBox_key(self._cur, "country", "country_id", self.tableWidget, 1)

		if table == "Country":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())

		if table == "Calendars":
			self.tableWidget.cellWidget(0,0).setValidator(QtGui.QIntValidator())
			createComboBox_key(self._cur, "listings", "lid", self.tableWidget, 1)
			createDateBox(self.tableWidget, 2)
			createComboBox(self.tableWidget, 3, np.array(["t", "f"]))
			self.tableWidget.cellWidget(4,0).setValidator(QtGui.QIntValidator())

		if table == "HostsHasVerifications":
			createComboBox_key(self._cur, "hosts", "hid", self.tableWidget, 0)
			createComboBox_key(self._cur, "verifications", "vid", self.tableWidget, 1)

		if table == "ListingsHasAmenities":
			createComboBox_key(self._cur, "listings", "lid", self.tableWidget, 0)
			createComboBox_key(self._cur, "amenities", "aid", self.tableWidget, 1)
			

	"""
	QUERIES METHODS
	"""
	def exec_query(self, query):
		self.spinBox.setValue(1)
		self.pushButton_25.setEnabled(True)
		_translate = QtCore.QCoreApplication.translate
		self._cur.execute(query)
		self.query_data = np.array(self._cur.fetchall())
		plength = self.spinBox_nb_rows_search.value()
		nbr_pages = (self.query_data.shape[0] // plength) + 1
		self.spinBox.setMaximum(nbr_pages)
		self.label_nb_result_query.setText('Number of results : ' + str(self.query_data.shape[0]))
		self.label_17.setText(_translate("TabWidget", '/ ' + str(nbr_pages)))
		self.display_table(self.table_predefined_queries, self.query_data,1,self.spinBox_nb_rows_query.value())


	def go_page(self):
		_translate = QtCore.QCoreApplication.translate
		plength = self.spinBox_nb_rows_query.value()
		nbr_pages = (self.query_data.shape[0] // plength) + 1
		self.spinBox.setMaximum(nbr_pages)
		self.label_17.setText(_translate("TabWidget", '/ ' + str(nbr_pages)))
		self.display_table(self.table_predefined_queries, self.query_data, self.spinBox.text(),self.spinBox_nb_rows_query.value())

	def display_table(self, table, data, page, plength):
		columnCount = data.shape[1] if len(data.shape) > 1 else 0
		col_names = [row[0] for row in self._cur.description]
		table.setColumnCount(0)
		table.setRowCount(0)
		table.setColumnCount(columnCount)
		table.setHorizontalHeaderLabels(col_names)
		
		page = int(page)
		for row_number, row_data in enumerate(data[(page-1)*plength : min(plength*page, data.shape[0])]):
			table.insertRow(row_number)
			for column_number, _data in enumerate(row_data):
				table.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(_data)))

		table.setVerticalHeaderLabels(np.arange(1 + (page-1)*plength, min(plength*page, data.shape[0])+1).astype('str'))
		table.resizeColumnsToContents()

if __name__ == "__main__":
	
	try:
		con = cx_Oracle.connect('C##DB2019_G06/DB2019_G06@cs322-db.epfl.ch/ORCLCDB')
		cur = con.cursor()
		print("Connected to the database.")
		app = QtWidgets.QApplication(sys.argv)
		TabWidget = QtWidgets.QTabWidget()
		ui = Ui_TabWidget(con, cur)
		ui.setupUi(TabWidget)
		ui.setup_func()
		TabWidget.show()
		sys.exit(app.exec_())

	except Exception as error:
		print("Caught an error : " + repr(error))
		con.close()
		cur.close()
		sys.exit()
