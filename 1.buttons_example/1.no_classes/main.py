from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
import sys

app = QApplication(sys.argv)

# setup the window
window = QMainWindow()
window.setWindowTitle("Our first MainWindow App!")

# setup the button
button = QPushButton()
button.setText("Press Me")

# connect button and window
window.setCentralWidget(button)
window.show()

app.exec()
