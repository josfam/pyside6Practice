from PySide6.QtWidgets import QApplication, QPushButton


# the slot that responds when something happens
def button_clicked(data):
    print("You clicked the button, didn't you! checked : ", data)


app = QApplication()
button = QPushButton("Press Me")

# make the button checkable such that it toggles between checked and unchecked
button.setCheckable(True)

# Use the emitted `clicked` signal of the QPushButton to wire the slot
button.clicked.connect(button_clicked)

button.show()
app.exec()
