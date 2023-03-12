from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys
from classes import MainWindow

#


def main():
    app = QApplication([])
    window = MainWindow()

    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
