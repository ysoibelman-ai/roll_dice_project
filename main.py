from dice_game.game import main_menu,get_menu_selection
from dice_game.validations import check_valid_menu_selection

def main ():
    main_menu()
    while True:
        menu_selection = get_menu_selection
        match menu_selection:
            case "1":
                pass
            case "2":
                pass
            case "3":
                pass
            case "4":
                exit()
            case _:
                print ("\ninvalid menu selection\n")

    

if __name__ == "__main__":
    main()