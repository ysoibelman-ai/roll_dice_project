import json
from pathlib import Path

def get_input(msg):
    return input(msg)

def update_json_file(game_results):
    my_file = Path(__file__).parent.parent / "data/game_history.json"
    try:
        with open(my_file, "w", encoding="utf-8") as file:
            json.dump(game_results, file, indent=2, ensure_ascii=False)
    except json.decoder.JSONDecodeError:
        print ("unable to update file")

def load_from_json():
    my_file = Path(__file__).parent.parent / "data/game_history.json"
    try:
        with open(my_file, "r", encoding="utf-8") as file:
            json_file = json.load(file)
            return json_file
    except json.decoder.JSONDecodeError:
        return None

def check_json():
    json_content = load_from_json()
    if json_content == None:
        update_json_file([])