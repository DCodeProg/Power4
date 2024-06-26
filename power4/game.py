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
            self.print_game_title()
            print(Fore.YELLOW + "MAIN MENU : " + Style.RESET_ALL)
            print(menu)
            
            
        show_menu()
        while True:
            print_choise_prompt()
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
                    print(Back.LIGHTRED_EX + "⚠️ Invalid choice!" + Style.RESET_ALL)

    def credits_menu(self):
        """Displays information about the game developers and licence
        """
        # Clear the console
        os.system('cls')
        
        # Game title
        self.print_game_title()
        
        # Project description
        print(Fore.YELLOW + "DESCRIPTION" + Style.RESET_ALL)
        print("A project of power 4 made for \"Fondamentaux Python\" course at EPSI Lille." + Style.DIM + "\nCreated in march 2024" + Style.RESET_ALL)
        
        # Author infos
        print("\n" + Fore.YELLOW + "AUTHOR INFOS" + Style.RESET_ALL)
        print("Name: Danaël LEGRAND")
        print("Email: danael.legrand@ecoles-epsi.net")
        print("Github: https://github.com/DCodeProg")
        
        # Licence infos
        print("\n" + Fore.YELLOW + "LICENSE" + Style.RESET_ALL)
        print("""MIT License

Copyright (c) [2024] [Power4]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.""")
        
        
        # Back to main menu prompt
        print("\n" + Fore.BLUE + "⇒ Press <ENTER> to go back in main menu" + Style.RESET_ALL, end=" ")
        input()
    
    def history_menu(self):
        """Displays a list of saved parties
        """
        # Clear the console
        os.system('cls')
        
        # Game title
        self.print_game_title()
        
        # List of saved parties
        print(Fore.YELLOW + "PARTY HISTORY: " + Style.RESET_ALL)
        path = os.path.join(ROOT_DIR, r'saves\party_saves')
        files = [f.removesuffix('.txt') for f in os.listdir(path)]
        print("\n".join(files[:10]))
        
        # Back to main menu prompt
        print("\n" + Fore.BLUE + "⇒ Press <ENTER> to go back in main menu" + Style.RESET_ALL, end=" ")
        input()


    "ACTIONS"
    def start_new_party(self):
        """Star a new power4 party
        """
        self.party = Party()
    
        
    "DISPLAY"
    def print_game_title(self) -> None:
        """Show game title in the console
        """
        print(Fore.CYAN + """ _____                   ___ 
|  _  |___ _ _ _ ___ ___| | |
|   __| . | | | | -_|  _|_  |
|__|  |___|_____|___|_|   |_|
""", Style.RESET_ALL)
    
    
    "OTHER"
    def quit(self) -> None:
        """Display goodbye message and exit the game
        """
        print_goodbye(on_new_line=False)
        quit()


def test_game():
    game = Game()
        
if __name__ == "__main__":
    test_game()