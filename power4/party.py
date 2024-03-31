import os
from datetime import datetime
from colorama import Fore, Back, Style

from board import Board
from utils import *

CUR_DIR = os.path.dirname(__file__)
ROOT_DIR = os.path.dirname(CUR_DIR)

class Party:
    """Class representing a party of Power4"""
    def __init__(self):
        # Set the party's staring date
        self.start_date = datetime.now()
        
        # Save emplacement
        self.save_dir: str = os.path.join(ROOT_DIR, r'saves/party_saves/')
        self.save_path: str = fr"Power4 {self.start_date.strftime('%Y-%m-%d %Hh%M %Ss')}.txt"
        
        # Party utilities
        self.board = Board()
        self.turn = 0
        
        # party loop
        self._party_loop()
                
    def _party_loop(self):
        def next_turn():
            """Go to the next turn
            """
            global player
            
            # update the turn and player
            self.turn += 1
            player = 1 if self.turn % 2 != 0 else 2 
            
            # show the turn information in console (turn, player, hints, grid)
            self.show_turn(self.turn, player)
            
        # Create a new party save file
        self.save_party()
        
        next_turn()
        while True:
            # Check if the grid is full
            if self.board.is_full():
                print("\n", Back.MAGENTA + "🟰 Grid full! Equality" + Style.RESET_ALL, sep="")
                return self.end_game_menu()
            
            print_choise_prompt()
            match input().lower():
                # Column selection
                case num if num.isdigit():
                    num = int(num)-1
                    
                    # Check if the column is valid
                    if not num in range(self.board.column_count):
                        print(Back.LIGHTRED_EX + "⚠️ Invalid column!" + Style.RESET_ALL)
                        continue
                    
                    # Check if the column is already full
                    if not self.board.is_move_possible(num):
                        print(Back.LIGHTRED_EX + "⚠️ Column already full!" + Style.RESET_ALL)
                        continue
                    
                    # Drop the pawn in the column and save the turn
                    self.board.drop_pawn(num, player)
                    self.save_turn(self.turn, player, num)
                    
                    # Check if the player has won
                    if self.board.check_victory():
                        # Show the turn informations wihout the game hints
                        self.show_turn(self.turn, player, True)
                        
                        # Display the winner and end game menu
                        print("\n", Fore.GREEN + "🎉 Player " + str(player) + " won!" + Style.RESET_ALL, sep="")
                        return self.end_game_menu()
                    else:
                        next_turn()
                    
                # Restart the party
                case "r":
                    return self.restart_party()
                
                # Go back to the main menu
                case "q":
                    break
                
                # Invalid choice
                case "":
                    self.show_turn(self.turn, player)
                    continue
                case _:
                    print(Back.LIGHTRED_EX + "⚠️ Invalid option!" + Style.RESET_ALL)
                    continue
    
    
    "MENUS"
    def end_game_menu(self):
        
        print("(n): Start a new party")
        print("(h): View turn history")
        print("(q): Go back to the main menu")
        
        while True:
            print_choise_prompt()
            match input().lower():
                case "n":
                    return self.restart_party()
                case "h":
                    self.print_history()
                case "q":
                    break
                case _:
                    print(Back.LIGHTRED_EX + "⚠️ Invalid choice!" + Style.RESET_ALL)
                    
    
    "ACTIONS"
    def restart_party(self):
        """Restarts the party by clearing the board, resetting the turn counter, and starting a new game.
        """
        self.board.empty_grid()
        self.turn = 0
        self.start_date = datetime.now()
        self._party_loop()
        
    def save_party(self):
        """Create a new party save file
        """
        with open(os.path.join(self.save_dir + self.save_path), 'w') as file:
            ...
            
    def save_turn(self, turn: int, player: int, column: int):
        """Save the given turn in the party save file

        Args:
            turn (int): Turn of the party
            player (int): Player of the turn
            column (int): Column where the pawn was dropped
        """
        with open(os.path.join(ROOT_DIR, r'saves/party_saves/' + self.save_path), 'a') as file:
            file.write(f"{datetime.now()};{turn};{player};{column}\n")
    
    "DISPLAY"
    def show_turn(self, turn: int, player: int, hide_hints: bool = False):
        """Displays the current turn, player and if enable game hints.

        Args:
            turn (int): The current turn of the game.
            player (int): The player whose turn it is (1 or 2).
            hide_hints (bool, optional): Whether to hide the game hints. Defaults to False.
        """
        # Clear the console
        os.system('cls')
        
        # Show the current turn and the player
        print(f"Turn {turn} - ", end="")
        match player:
            case 1:
                print(Fore.BLACK + Back.YELLOW + "Player 1" + Style.RESET_ALL, end="\n\n")
            case 2:
                print(Fore.BLACK + Back.RED + "Player 2" + Style.RESET_ALL, end="\n\n")
        
        # If enabled, show the game hints
        if not hide_hints:
            print(f"(1-{self.board.column_count}) to play")
            print("(r) to restart the party")
            print("(q) to go back to the main menu", end="\n\n")
        
        # Show the grid
        self.board.print_grid()
        
    def print_history(self):
        """Prints the turn history of the game.
        """
        list_moves = []
        with open(os.path.join(ROOT_DIR, r'saves/party_saves/' + self.save_path), 'r') as file:
            for line in file.readlines():
                list_moves.append(line.strip().split(";"))
        
        # Display the turn history
        for move in list_moves:
            if move[2] == "1":
                print(f"Turn {move[1]}:", Fore.BLACK + Back.YELLOW + "Player 1" + Style.RESET_ALL, f"place in column {int(move[3])+1}")
            else:
                print(f"Turn {move[1]}:", Fore.BLACK + Back.RED + "Player 2" + Style.RESET_ALL, f"place in column {int(move[3])+1}")
            
        
# TESTING
def test_party():
    try:
        p = Party()
    except KeyboardInterrupt:
        print("\n", Back.RED + "❌ Quitting..." + Style.RESET_ALL, sep="")
        
if __name__ == "__main__":
    test_party()