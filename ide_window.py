# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testUpdateMenu.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


# -----------------------------------------------------------------------------
# ide_window
# -----------------------------------------------------------------------------
# This window is the main window. All UI IDE is here.
#
# This window has a main menu (on top),
# a code entry field,
# a result output field (the result of running the code),
# a field for displaying the current path.
# -----------------------------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets
from syntax_highlighting import PythonHighlighter
from line_number import QCodeEditor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(605, 649)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #3c3f41;")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.field_code_input = QCodeEditor(self.centralwidget)
        self.field_code_input.setTabStopWidth(20)
        self.field_code_input.setStyleSheet(
            "background-color: #2b2b2b; color: rgb(204,204,204); border-width: 1px; border-style: solid; border-color: #555555 #555555 #555555 #555555;")
        self.field_code_input.setObjectName("field_code_input")
        self.field_code_input.setPlainText("Create a new file or open yours to get started")
        self.syntax_highlight = PythonHighlighter(self.field_code_input.document())
        self.verticalLayout.addWidget(self.field_code_input)

        self.field_result_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.field_result_output.setStyleSheet("background-color: #2b2b2b; color: #a4a3a3; border-width: 1px; border-style: solid; border-color: #555555 #555555 #555555 #555555;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.field_result_output.sizePolicy().hasHeightForWidth())
        self.field_result_output.setSizePolicy(sizePolicy)
        self.field_result_output.setObjectName("field_result_output")
        self.verticalLayout.addWidget(self.field_result_output)

        self.field_path_current_file = QtWidgets.QLabel(self.centralwidget)
        self.field_path_current_file.setObjectName("field_path_current_file")
        self.field_path_current_file.setStyleSheet("color: #a4a3a3;")
        self.verticalLayout.addWidget(self.field_path_current_file)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuRun = QtWidgets.QMenu(self.menubar)
        self.menuRun.setObjectName("menuRun")
        MainWindow.setMenuBar(self.menubar)

        self.button_new_file = QtWidgets.QAction(MainWindow)
        self.button_new_file.setObjectName("button_new_file")
        self.button_open_file = QtWidgets.QAction(MainWindow)
        self.button_open_file.setObjectName("button_open_file")
        self.button_save = QtWidgets.QAction(MainWindow)
        self.button_save.setObjectName("button_save")
        self.button_save_as = QtWidgets.QAction(MainWindow)
        self.button_save_as.setObjectName("button_save_as")
        self.actionNew_Window = QtWidgets.QAction(MainWindow)
        self.actionNew_Window.setObjectName("actionNew_Window")
        self.button_new_window = QtWidgets.QAction(MainWindow)
        self.button_new_window.setObjectName("button_new_window")
        self.button_close_window = QtWidgets.QAction(MainWindow)
        self.button_close_window.setObjectName("button_close_window")
        self.button_exit = QtWidgets.QAction(MainWindow)
        self.button_exit.setObjectName("button_exit")
        self.button_undo = QtWidgets.QAction(MainWindow)
        self.button_undo.setObjectName("button_undo")
        self.button_redo = QtWidgets.QAction(MainWindow)
        self.button_redo.setObjectName("button_redo")
        self.button_cut = QtWidgets.QAction(MainWindow)
        self.button_cut.setObjectName("button_cut")
        self.button_copy = QtWidgets.QAction(MainWindow)
        self.button_copy.setObjectName("button_copy")
        self.button_paste = QtWidgets.QAction(MainWindow)
        self.button_paste.setObjectName("button_paste")
        self.button_run = QtWidgets.QAction(MainWindow)
        self.button_run.setObjectName("button_run")
        self.button_stop = QtWidgets.QAction(MainWindow)
        self.button_stop.setObjectName("button_stop")
        self.button_hide_result_field = QtWidgets.QAction(MainWindow)
        self.button_hide_result_field.setObjectName("button_hide_result_field")

        self.menuFile.addAction(self.button_new_file)
        self.menuFile.addAction(self.button_open_file)
        self.menuFile.addAction(self.button_save)
        self.menuFile.addAction(self.button_save_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.button_new_window)
        self.menuFile.addAction(self.button_close_window)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.button_exit)
        self.menuEdit.addAction(self.button_undo)
        self.menuEdit.addAction(self.button_redo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.button_cut)
        self.menuEdit.addAction(self.button_copy)
        self.menuEdit.addAction(self.button_paste)
        self.menuView.addAction(self.button_hide_result_field)
        self.menuRun.addAction(self.button_run)
        self.menuRun.addAction(self.button_stop)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuRun.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.field_path_current_file.setText(_translate("MainWindow", "/current/path/file.py"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuRun.setTitle(_translate("MainWindow", "Run"))
        self.button_new_file.setText(_translate("MainWindow", "New File"))
        self.button_open_file.setText(_translate("MainWindow", "Open File"))
        self.button_save.setText(_translate("MainWindow", "Save"))
        self.button_save_as.setText(_translate("MainWindow", "Save As"))
        self.actionNew_Window.setText(_translate("MainWindow", "New Window"))
        self.button_new_window.setText(_translate("MainWindow", "New Window"))
        self.button_close_window.setText(_translate("MainWindow", "Close Window"))
        self.button_exit.setText(_translate("MainWindow", "Exit"))
        self.button_undo.setText(_translate("MainWindow", "Undo"))
        self.button_redo.setText(_translate("MainWindow", "Redo"))
        self.button_cut.setText(_translate("MainWindow", "Cut"))
        self.button_copy.setText(_translate("MainWindow", "Copy"))
        self.button_paste.setText(_translate("MainWindow", "Paste"))
        self.button_run.setText(_translate("MainWindow", "Run"))
        self.button_stop.setText(_translate("MainWindow", "Stop"))
        self.button_hide_result_field.setText(_translate("MainWindow", "Hide Result Window"))