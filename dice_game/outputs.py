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
    return menu_selection

def show_game_history(game_history):
    print ("\n----- GAME HISTORY -----")
    counter = 1
    for game in game_history:
            print (f"""
    ------- GAME {counter} -------
    PLAYER: {game["player_name"]}
    ROUNDS: {game["rounds"]}
    {game["player_name"]} SCORE: {game["player_score"]} 
    COMPUTER SCORE: {game["computer_score"]}
    WINNER: {game["winner"]}
    """)
            counter +=1

def show_statistics(game_count,player_wins,computer_wins,draws,player_win_stats):
    print(f"""
NUMBER OF GAMES: {game_count}
PLAYER WINS: {player_wins}
COMPUTER WINS: {computer_wins}
DRAWS: {draws}
PLAYER WIN STATS: {round(player_win_stats,2)*100}%
""")

def show_end_game(name,player_score,computer_score):
    print(f"""
================================
          GAME OVER
================================

{name.upper()}: {player_score} points
Computer: {computer_score} points

WINNER: {name if player_score > computer_score else "Computer" if computer_score > player_score else "Tie Game"}!

Game saved successfully!
""")

def show_round(name,round):
    print(f"""
---------- ROUND {round["round"]} ----------

{name}:    🎲 {round["player_dice"]}
Computer: 🎲 {round["computer_dice"]}

{round["winner"]} wins this round!
""")