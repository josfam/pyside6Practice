from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import Qt


# the slot to respond to the slider
def respond_to_slider(data):
    print("slider moved to : ", data)


app = QApplication()

# create the slider
slider = QSlider(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(100)
slider.setValue(25)

# use the `valueChanged` signal emitted from the slider to
# connect to the slot
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
