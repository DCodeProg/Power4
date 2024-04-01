import os
from colorama import Fore, Back, Style

from party import Party
from utils import *

# Relative path
CUR_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CUR_DIR)

class Game:
    def __init__(self) -> None:
        # Current game party
        self.party: Party | None = None
        
        # Main game loop
        self._game_loop()

    def _game_loop(self) -> None:
        """Main game loop
        """        
        while True:
            self.main_menu()


    "MENUS"
    def main_menu(self):
        """Displays the main menu and handles user input.
        The main menu consists of the following options:
            - New Party: Starts a new game.
            - Party History: Displays a list of saved parties.
            - Credits: Displays information about the game developers and licence.
            - Quit: Exits the game.
        """

        # Menu options
        menu = "(n): New party\n(h): Party history\n(c): Credits\n(q): Quit"

        def show_menu():
            """Print the main menu in the console
            """
            # Clear the console
            os.system('cls') 
            
            # Game title, menu title and menu options
            prompt.game_title()
            prompt.label("MAIN MENU:")
            print(menu)
            
            
        show_menu()
        while True:
            prompt.your_choice()
            match input().lower():
                # New party
                case "n":
                    self.start_new_party()
                    show_menu()
                    
                # Party history                
                case "h":
                    self.history_menu()
                    show_menu()
                                        
                # Credits
                case "c":
                    self.credits_menu()
                    show_menu()
                    
                # Quit
                case "q":
                    self.quit()
                    
                # Invalid choice
                case _:
                    prompt.error("⚠️ Invalid choice!")

    def credits_menu(self):
        """Displays information about the game developers and licence
        """
        # Clear the console
        os.system('cls')
        
        # Game title
        prompt.game_title()
        
        # Project description
        prompt.label("DESCRIPTION")
        print("A project of power 4 made for \"Fondamentaux Python\" course at EPSI Lille." + Style.DIM + "\nCreated in march 2024" + Style.RESET_ALL)
        
        # Author infos
        prompt.label("\nAUTHOR INFOS")
        print("Name: Danaël LEGRAND")
        print("Email: danael.legrand@ecoles-epsi.net")
        print("Github: https://github.com/DCodeProg")
        
        # Licence infos
        prompt.label("\nLICENCE")
        with open(os.path.join(ROOT_DIR, "LICENSE"), "r") as file:
            print(file.read())
        
        
        # Back to main menu prompt
        prompt.back_to_main_menu()
        input()
    
    def history_menu(self):
        """Displays a list of saved parties
        """
        # Clear the console
        os.system('cls')
        
        # Game title
        prompt.game_title()
        
        # List of saved parties
        prompt.label("PARTY HISTORY")
        path = os.path.join(ROOT_DIR, r'saves\party_saves')
        files = [f.removesuffix('.txt') for f in os.listdir(path)]
        print("\n".join(files[:10]))
        
        # Back to main menu prompt
        prompt.back_to_main_menu()
        input()


    "ACTIONS"
    def start_new_party(self):
        """Star a new power4 party
        """
        self.party = Party()
       
    
    "OTHER"
    def quit(self) -> None:
        """Display goodbye message and exit the game
        """
        prompt.goodbye(on_new_line=False)
        quit()


def test_game():
    game = Game()
        
if __name__ == "__main__":
    test_game()