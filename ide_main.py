# -----------------------------------------------------------------------------
# ide_main
# -----------------------------------------------------------------------------
# Main file. This file contains all the logic of the program.
# -----------------------------------------------------------------------------

import sys
import inspect
import os.path
from ide_window import Ui_MainWindow
from cnf_window import Ui_CnfWindow
from PyQt5.QtCore import QProcess
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class CnfWindow(QtWidgets.QMainWindow, Ui_CnfWindow):
    def __init__(self, MainWindow):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CnfWindow")

        self.path = None
        self.MainWindow = MainWindow

        self.button_create_new_file.clicked.connect(self.create_new_file)

    def create_new_file(self):
        filename = inspect.getframeinfo(inspect.currentframe()).filename
        path = os.path.dirname(os.path.abspath(filename))
        open(f"{path}\\{self.field_entering_name_new_file.text()}.py", "a").close()

        self.MainWindow.field_path_current_file.setText(
            f"{path}\\{self.field_entering_name_new_file.text()}.py")
        self.MainWindow.field_code_input.setDisabled(False)
        self.MainWindow.field_code_input.clear()
        self.hide()

# -----------------------------------------------------------------------------

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("IDE")

        self.field_result_output.hide()

        self.process = None

        self.new_window = None
        self.cnf_window = CnfWindow(self)

        self.field_code_input.setDisabled(True)

        self.timer = QtCore.QTime()

        self.button_new_file.triggered.connect(self.new_file)
        self.button_open_file.triggered.connect(self.open_file)
        self.button_save_as.triggered.connect(self.save_as_file)
        self.button_run.triggered.connect(self.run_code)
        self.button_stop.triggered.connect(self.stop_code)
        self.button_save.triggered.connect(self.save_file)
        self.button_new_window.triggered.connect(self.create_new_window)
        self.button_close_window.triggered.connect(self.close_new_window)
        self.button_exit.triggered.connect(self.exit_the_program)
        self.button_hide_result_field.triggered.connect(self.hide_result_field)

    # -------------------------- BEGIN MENU <FILE> ----------------------------
    def new_file(self):
        self.cnf_window.field_entering_name_new_file.clear()
        self.cnf_window.show()


    def open_file(self):
        path = QFileDialog.getOpenFileName(self, "Save file", "",
                                           "All files (*.*)")[0]
        if path:
            try:
                with open(path, "r") as file:
                    self.field_code_input.setDisabled(False)
                    self.field_path_current_file.setText(path)
                    self.field_code_input.setPlainText(file.read())
            except IOError as error:
                warning = QMessageBox()
                warning.setWindowTitle("Error")
                warning.setText(f"{error}")
                warning.setIcon(QMessageBox.Warning)
                x = warning.exec_()


    def save_file(self):
        try:
            with open(f"{self.field_path_current_file.text()}", "w") as file:
                file.write(self.field_code_input.toPlainText())
        except IOError:
            pass


    def save_as_file(self):
        path = QFileDialog.getSaveFileName(self, "Open file", "",
                                           "All files (*.*)")[0]
        if path:
            try:
                with open(path, "w") as file:
                    self.field_path_current_file.setText(path)
                    file.write(self.field_code_input.toPlainText())
            except IOError as error:
                warning = QMessageBox()
                warning.setWindowTitle("Error")
                warning.setText(f"{error}")
                warning.setIcon(QMessageBox.Warning)
                x = warning.exec_()


    def create_new_window(self):
        if self.new_window is None:
            self.new_window = MainWindow()
            self.new_window.show()
        else:
            self.new_window.close()
            self.new_window = None


    def close_new_window(self):
        self.new_window.close()
        self.new_window = None


    def exit_the_program(self):
        self.close()
    # -------------------------- END MENU <FILE> ------------------------------

    # -------------------------- BEGIN MENU <VIEW> ----------------------------
    def hide_result_field(self):
        self.field_result_output.hide()
    # ---------------------------- END MENU <VIEW> ----------------------------

    # --------------------------- BEGIN MENU <RUN> ----------------------------
    def run_code(self):
        self.save_file()
        self.field_result_output.show()
        self.field_result_output.clear()
        if self.process is None:  # No process running.
            self.field_result_output.append("[Started]\n")
            self.process = QProcess()
            self.process.readyReadStandardOutput.connect(self.handle_stdout)
            self.process.readyReadStandardError.connect(self.handle_stderr)
            self.process.started.connect(self.timer.start)
            self.process.finished.connect(self.finished_code)
            try:
                self.process.start("python", [f"{self.field_path_current_file.text()}"])
            except Exception as error:
                warning = QMessageBox()
                warning.setWindowTitle("Error")
                warning.setText(f"{error}")
                warning.setIcon(QMessageBox.Warning)
                x = warning.exec_()


    def handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        self.field_result_output.append(stderr)


    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.field_result_output.append(stdout)


    def finished_code(self):
        process_execution_time = self.timer.elapsed()
        self.field_result_output.append(f"[Finished in {process_execution_time / 1000}s]")
        self.process = None


    def stop_code(self):
        try:
            self.process.kill()
        except Exception as error:
            warning = QMessageBox()
            warning.setWindowTitle("Error")
            warning.setText(f"{error}")
            warning.setIcon(QMessageBox.Warning)
            x = warning.exec_()
    # -------------------------- END MENU <RUN> -------------------------------

    # Program closure processing
    def closeEvent(self, event):
        self.save_file()
        reply = QMessageBox.question(self, 'Exit',
                                     'Are you sure you want to close the window?',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    application = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(application.exec_())