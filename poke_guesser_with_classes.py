"""
TODO: Add a pokeball icon top left for Eden.
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
    QShortcut,
)
from PyQt5.QtGui import (
    QImage, 
    QPixmap,
    QIcon
)

# API_URL = "https://pokeapi.co/api/v2/pokemon/"
API_URL = "https://pokeapi.co/api/v2/"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Poke Guesser v2')
        # self.setFixedSize(800, 600)
        self.layout = QVBoxLayout()

        # 1
        self.add_window_icon()

        # Initialize pixmap.
        self.pokemon_pixmap = QLabel(self)
        self.pokemon_pixmap.show()

        # Initialize message box.
        self.message_box = QLabel(self)
        self.message_box.setText('Who\'s that pokemon?')
        self.message_box.show()

        # Initialize entry box.
        self.entry_box = QLineEdit(self)
        self.entry_box.show()

        self.entry_box.returnPressed.connect(self.on_submit)

        # Initialize submit button.
        self.submit_button = QPushButton('Submit')
        self.submit_button.show()

        # Initialize new game button.
        self.new_game_button = QPushButton('Next Pokemon')
        self.new_game_button.hide()

        self.layout.addWidget(self.pokemon_pixmap)
        self.layout.addWidget(self.message_box)
        self.layout.addWidget(self.entry_box)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.new_game_button)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)

    def add_window_icon(self):
        response = requests.get(f'{API_URL}/item/poke-ball')
        window_icon_url = response.json()['sprites']['default']
        window_icon_pixmap = QPixmap()
        window_icon_pixmap.loadFromData(requests.get(window_icon_url).content)
        self.setWindowIcon(QIcon(window_icon_pixmap))

    def on_submit(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
