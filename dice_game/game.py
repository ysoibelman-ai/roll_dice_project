from dice_game.validations import check_not_empty,check_valid_num
import random
def main_menu():
    menu_selection = input("""
================================
          ROLL DICE
================================

1. Start New Game
2. View Game History
3. View Statistics
4. Exit

Choose an option:
    """)

def get_input(msg):
    return input(msg)

def play_flow():
    game_results = []
    while True:
        name = get_input("Enter Name: ")
        if not check_not_empty():
            continue
        #save in dict
        break
    while True:
        num_of_rounds = get_input("Enter Number of Rounds: ")
        if not check_valid_num(num_of_rounds,10):
            continue
        num_of_rounds = int(num_of_rounds)
        break

    for i in range (num_of_rounds):
        player,computer = roll_dice()
        round_ = create_round(player,computer,i)
        show_round(name,round_)
        game_results.append(round_)

    player_score, computer_score = calculate_points(game_results)
    show_end_game()
    show_game_results(game_results)
    load_to_json(game_results)


def show_end_game(name,player_score,computer_score):
    print(f"""
================================
          GAME OVER
================================

{name}:    2 points
Computer: 1 points

WINNER: {name if player_score > computer_score else "Computer" if computer_score > player_score else "Tie Game"}!

Game saved successfully!
""")


def calculate_points(game_results):
    player_score, computer_score = 0
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
            "round": round_num,
            "player_dice": player_score,
            "computer_dice": computer_socre,
            "winner": name if player_score > computer_socre else "Computer" if computer_socre > player_score else "Draw"
        }
    return round

def show_round(name,round):
    print(f"""
---------- ROUND {round["round"]} ----------

{name}:    🎲 {round["player_dice"]}
Computer: 🎲 {round["computer_dice"]}

{round["winner"]} wins this round!

""")

def roll_dice():
    player_roll = random.randint(1,6)
    computer_roll = random.randint(1,6)
    return player_roll,computer_roll