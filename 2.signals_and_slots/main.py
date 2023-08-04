from PySide6.QtWidgets import QApplication, QPushButton


# the slot that responds when something happens
def button_clicked():
    print("You clicked the button, didn't you!")


app = QApplication()
button = QPushButton("Press Me")

# Use the emitted `clicked` signal of the QPushButton to wire the slot
button.clicked.connect(button_clicked)

button.show()
app.exec()
