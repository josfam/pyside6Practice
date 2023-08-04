from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# responsible for processing commandline arguments
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first MainWindow App!")

# create a button
button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()

# start the event loop
app.exec()
