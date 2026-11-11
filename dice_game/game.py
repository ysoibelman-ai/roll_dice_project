from dice_game.validations import *
import random
from outputs import show_end_game,show_game_history,show_round,show_statistics
from helper_functions import get_input,load_from_json,update_json_file


def play_flow():
    game_results = []
    while True:
        name = get_input("Enter Name: ")
        if not check_not_empty(name):
            continue
        break
    while True:
        num_of_rounds = get_input("Enter Number of Rounds: ")
        if not check_valid_num(num_of_rounds,10):
            continue
        num_of_rounds = int(num_of_rounds)
        break

    for i in range (num_of_rounds):
        player,computer = roll_dice()
        round_ = create_round(name,player,computer,i)
        show_round(name,round_)
        game_results.append(round_)

    player_score, computer_score = calculate_points(game_results)
    show_end_game(name,player_score,computer_score)
    full_game_presentation = create_game_presentation(name,num_of_rounds,player_score,computer_score,(name if player_score > computer_score else "Computer" if computer_score > player_score else "Tie Game"),game_results)

    json_file = load_from_json()
    if json_file:
        json_file.append(full_game_presentation)
        update_json_file(json_file)
    else:
        json_file = load_from_json()
        json_file.append(full_game_presentation)
        update_json_file(json_file)

def review_game_history_flow():
    game_history = load_from_json()
    if game_history == []:
        print ("no games")
        return
    show_game_history(game_history)

def view_statistics_flow():
    game_history = load_from_json()
    game_count = len(game_history)
    player_wins,computer_wins,draws = calculate_wins(game_history)
    player_win_stats = player_wins / len(game_history)
    show_statistics(game_count,player_wins,computer_wins,draws,player_win_stats)

def calculate_wins(game_history):
    player_wins = 0
    computer_wins = 0
    draws = 0
    for game in game_history:
        if game["winner"] == "Computer":
            computer_wins +=1
        elif game["winner"] == "Draw":
            draws += 1
        else:
            player_wins +=1
    return player_wins,computer_wins,draws

def calculate_points(game_results):
    player_score =0
    computer_score = 0
    for round in game_results:
        if round["winner"] == "Computer":
            computer_score +=1
        elif round["winner"] == "Draw":
            continue
        else:
            player_score +=1
    return player_score,computer_score
        

def create_round (name,player_score,computer_socre,round_num):
    round_ = {
            "round": round_num+1,
            "player_dice": player_score,
            "computer_dice": computer_socre,
            "winner": name if player_score > computer_socre else "Computer" if computer_socre > player_score else "Draw"
        }
    return round_

def roll_dice():
    player_roll = random.randint(1,6)
    computer_roll = random.randint(1,6)
    return player_roll,computer_roll

def create_game_presentation(name,rounds,player_score,computer_score,winner,game_results):
    full_game ={
    "player_name": name,
    "rounds": rounds,
    "player_score": player_score,
    "computer_score": computer_score,
    "winner": winner,
    "results": game_results
    }
    return full_game