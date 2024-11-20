import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot

app = QApplication([])

@pyqtSlot()
def on_click():
    print("Hellor World")

window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(750, 300, 500, 500)
helloMsg = QLabel("<h1>Todo App</h1>", parent=window)
helloMsg.move(60, 15)
button = QPushButton(text="button", parent=window)


window.show()

sys.exit(app.exec())