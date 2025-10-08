from PyQt6.QtWidgets import QMessageBox

from retail_project.connectors.employee_connector import EmployeeConnector
from retail_project.ui.MainWindow import Ui_MainWindow


class LoginMainWindowExt(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonLogin.clicked.connect(self.process_login)
    def process_login(self):
        email=self.lineEditEmail.text()
        password=self.lineEditPassword.text()
        ec = EmployeeConnector()
        em = ec.login(email, password)
        if em == None:
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Login Failed! Please check your account again.")
            msg.setWindowTitle("Login Failed!")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText("Login Successful!")
            msg.setWindowTitle("Login Successful!")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

