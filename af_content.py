from af_demand import *
from fen_move import *

fen_path = r"C:\Users\cleme\Documents\Chess\txt\fen.txt" #change ** in your windows username
best_path = r"C:\Users\cleme\Documents\Chess\txt\fen.txt" #change ** in your windows username

def final():
    while True:
        depth = 12

        get_fen()

        with open(fen_path, 'r') as fichier:
            fen_position = fichier.read().strip().replace('_', ' ')

        get_best_move(fen_position, depth)

        with open(best_path, 'r', encoding='utf-8') as fichier:
            best = fichier.read().strip()

        print(best)