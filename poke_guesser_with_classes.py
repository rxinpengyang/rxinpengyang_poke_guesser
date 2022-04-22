"""

"""
import os
import sys
import requests
import random
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow,
    QLabel, 
    QPushButton, 
    QLineEdit,
    QVBoxLayout,
    QWidget,
    QShortcut
)
from PyQt5.QtGui import (
    QImage, 
    QPixmap
)

API_URL = "https://pokeapi.co/api/v2/pokemon/"

class MainWindow(QMainWindow):
    pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Poke Guesser v2')

    window = MainWindow()

    app.exec_()
