from PySide6.QtWidgets import QApplication, QWidget

# responsible for processing commandline arguments
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

# start the event loop
app.exec()
