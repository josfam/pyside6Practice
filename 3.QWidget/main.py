from PySide6.QtWidgets import QApplication, QWidget
from rockwidget import RockWidget
import sys

app = QApplication(sys.argv)

windows = RockWidget()
windows.show()

app.exec()
