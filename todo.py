import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])

window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(750, 300, 500, 500)
helloMsg = QLabel("Todo App", parent=window)
helloMsg.move(60, 15)

window.show()

sys.exit(app.exec())