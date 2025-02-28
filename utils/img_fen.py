import requests
import base64
import os

def fen(player):
    global result
    url = "http://app.chessvision.ai/predict"

    with open(r"C:\Users\cleme\Documents\Chess\img\chess.png", "rb") as image_file: #change ** in your windows username
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    data = {
        "board_orientation": "predict",
        "cropped": False,
        "current_player": player,
        "image": f"data:image/jpeg;base64,{encoded_image}",
        "predict_turn": True
    }

    response = requests.post(url, json=data)

    folder = "txt"
    filename = os.path.join(folder, "fen.txt")

    if response.status_code == 200:
        response_json = response.json()
        result = response_json.get('result', None)
        with open(filename, 'w') as fichier:
            fichier.write(result)
    else:
        print(response.status_code)
        result = None