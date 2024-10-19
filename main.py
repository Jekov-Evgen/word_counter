from draw import MainWindow
from PyQt6.QtWidgets import QApplication

start = QApplication([])

window = MainWindow()
window.show()

start.exec()
