from dice_game.game import play_flow,review_game_history_flow,view_statistics_flow
from dice_game.outputs import main_menu
from dice_game.helper_functions import check_json

def main ():
    check_json()
    while True:
        menu_selection = main_menu()
        match menu_selection:
            case "1":
                play_flow()
            case "2":
                review_game_history_flow()
            case "3":
                view_statistics_flow()
            case "4":
                exit()
            case _:
                print ("\ninvalid menu selection\n")

if __name__ == "__main__":
    main()