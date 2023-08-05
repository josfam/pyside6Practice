from PySide6.QtWidgets import QApplication
from main_window import MainWindow
import sys

app = QApplication()

window = MainWindow(app)
window.show()

app.exec()
