from PyQt6.QtWidgets import QApplication, QMainWindow

from retail_project.ui.LoginMainWindowExt import LoginMainWindowExt

app = QApplication([])
login_ui=LoginMainWindowExt()
login_ui.setupUi(QMainWindow())
login_ui.showWindow()
app.exec()