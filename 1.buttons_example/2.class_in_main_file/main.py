from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
import sys


class ButtonHolder(QMainWindow):
    def __init__(self):
        # setup the window
        super().__init__()
        self.setWindowTitle("Button Holder app")
        # setup the button
        button = QPushButton("Press Me")
        # connect button and window
        window.setCentralWidget(button)


app = QApplication(sys.argv)
window = ButtonHolder()
window.show()

app.exec()
