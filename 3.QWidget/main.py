from PySide6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)

windows = QWidget()
windows.show()

app.exec()
