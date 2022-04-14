"""
POKE-GUESSER game.
Thanks to Alice Kokado and Joe Zhu for the idea.

I challenged myself to write this without using classes.
I will update this code with classes once we learn it in class.
TODO: pytest file
"""
import os
import sys
import requests
import random
from PyQt5.QtWidgets import (
    QApplication, 
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

def get_pokemon_name(pokedex_no):
    '''
    
    '''
    search = API_URL + str(pokedex_no)
    response = requests.get(search)
    return response.json()["name"]

def get_sprite_pixmap(pokedex_no):
    '''
    
    '''
    search = API_URL + str(pokedex_no)
    response = requests.get(search)
    sprite_url = response.json()["sprites"]["front_default"]
    sprite_image = QImage()
    sprite_image.loadFromData(requests.get(sprite_url).content)

    sprite_pixmap = QLabel()
    # Change pixmap size here.
    sprite_pixmap.setPixmap(QPixmap(sprite_image).scaled(256, 256))
    sprite_pixmap.show()

    return sprite_pixmap

def on_submit(answer):
    pokemon_name = get_pokemon_name(pokedex_no)
    if answer.lower() == pokemon_name:
        reply_box.setText('Correct!')
    else:
        reply_box.setText(f'Incorrect, it is {pokemon_name}')
    entry_box.setText('')
    new_game_button = QPushButton('Play again? (ctrl + p)')
    QShortcut("Ctrl+p", widget).activated.connect(new_game)
    new_game_button.clicked.connect(new_game)
    new_game_button.show()
    layout.addWidget(new_game_button)

def new_game():
    #pixmap_widget.clear()
    os.execl(sys.executable, sys.executable, *sys.argv)

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName('Pokemon Guesser')

    pokedex_no = random.randint(1, 151)
    pixmap_widget = get_sprite_pixmap(pokedex_no)

    reply_box = QLabel()
    reply_box.setText('Who\'s that pokemon?')
    reply_box.show()

    entry_box = QLineEdit()
    entry_box.returnPressed.connect(lambda: on_submit(entry_box.text()))
    entry_box.show()

    submit_button = QPushButton('Submit')
    # Lambda is an extra bit of complication because I didn't use classes.
    # Don't worry about this for now.
    submit_button.clicked.connect(lambda: on_submit(entry_box.text()))
    submit_button.show()

    layout = QVBoxLayout()
    layout.addWidget(pixmap_widget)
    layout.addWidget(reply_box)
    layout.addWidget(entry_box)
    layout.addWidget(submit_button)
    widget = QWidget()
    widget.setLayout(layout)
    widget.show()

    app.exec_()