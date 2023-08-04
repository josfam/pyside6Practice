from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")

        button1 = QPushButton("Button1")
        button2 = QPushButton("Button2")

        # a horizontal layout for placing components
        button_layout = QHBoxLayout()  # use QVBoxLayout for vertical layouts
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)

        # use the layout to lay out various components
        self.setLayout(button_layout)
