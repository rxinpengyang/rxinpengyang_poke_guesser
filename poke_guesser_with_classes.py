'''

'''
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
        self.pokedex_no = None
        self.pokemon_name = None

        self.setWindowTitle('Poke Guesser v2')
        # self.setFixedSize(800, 600)
        self.layout = QVBoxLayout()

        # 1
        self.add_window_icon()

        # Initialize pixmap.
        self.pokemon_sprite_pixmap = QLabel(self)
        self.pokemon_sprite_pixmap.show()

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

        self.layout.addWidget(self.pokemon_sprite_pixmap)
        self.layout.addWidget(self.message_box)
        self.layout.addWidget(self.entry_box)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.new_game_button)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)

        self.new_game()

    def add_window_icon(self):
        response = requests.get(f'{API_URL}/item/poke-ball')
        window_icon_url = response.json()['sprites']['default']
        window_icon_pixmap = QPixmap()
        window_icon_pixmap.loadFromData(requests.get(window_icon_url).content)
        self.setWindowIcon(QIcon(window_icon_pixmap))

    def get_pokemon_name(self):
        search = f'{API_URL}/pokemon/{self.pokedex_no}'
        response = requests.get(search)
        return response.json()["name"]

    def set_pokemon_sprite_pixmap(self):
        search = f'{API_URL}/pokemon/{self.pokedex_no}'
        response = requests.get(search)
        pokemon_sprite_url = response.json()["sprites"]["front_default"]
        pokemon_sprite_image = QImage()
        pokemon_sprite_image\
            .loadFromData(requests.get(pokemon_sprite_url).content)
        self.pokemon_sprite_pixmap\
            .setPixmap(QPixmap(pokemon_sprite_image).scaled(256, 256))

    def on_submit(self):
        pass

    def new_game(self):
        '''
        TODO: Generate non-repeating pokedex numbers.
        '''
        self.pokedex_no = random.randint(1, 151)
        self.pokemon_name = self.get_pokemon_name()
        self.pokemon_sprite_pixmap.clear()
        self.set_pokemon_sprite_pixmap()
        self.message_box.setText('Who\'s that pokemon?')
        self.entry_box.setText('')
        self.new_game_button.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
