import requests
import json

best_path = r"C:\Users\cleme\Documents\Chess\txt\fen.txt" #change ** in your windows username

def get_best_move(fen_position, depth):
    API_URL = "https://chess-api.com/v1"

    options = {
        "fen": fen_position,
        "variants": 1,
        "depth": depth,
        "maxThinkingTime": 50,
    }

    response = requests.post(API_URL, json=options)
    data = response.json()

    move_text = data.get('text', '').split(':')[0]

    with open(best_path, 'w', encoding='utf-8') as fichier:
        fichier.write(move_text)