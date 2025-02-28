from utils.demand import *
from utils.img_fen import *

fen_path = r"C:\Users\**\Documents\Chess\txt\fen.txt" #change ** in your windows username or path if error

player = str(input("enter your player : "))

def get_fen():
    def last():
        demand()
        fen(player=player)
        with open(fen_path, 'r') as fichier:
            contenu = fichier.read().strip().replace('_', ' ')
    last()
