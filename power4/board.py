from colorama import Fore, Back, Style

class Board:
    """Class representing a board of Puissance 4"""
    
    def __init__(self, row_count: int = 6, column_count: int = 7) -> None:
        """
        Args:
            row_count (int, optional): Number of rows in the board. Defaults to 6.
            column_count (int, optional): Number of columns in the board. Defaults to 7.
        """
        self.row_count: int = row_count
        self.column_count: int = column_count
        
        self.empty_grid()  
       
    
    "TESTS"
    def is_full(self) -> bool:
        """Check if the board is full

        Returns:
            bool: True if the board is full False otherwise
        """
        for row in self.grid:
            if 0 in row:
                return False
        return True
        
    def is_move_possible(self, column: int) -> bool:
        """Check if the specified column allows a move

        Args:
            column (int): Index of the column

        Returns:
            bool: True if the column allows a move False otherwise
        """
        return True if self.grid[0][column] == 0 else False    
    
    
    def check_victory(self) -> bool:
        """Check if there is a line of four in the grid

        Returns:
            bool: True if it's the case False otherwise
        """
        def check(line: list[int]) -> bool:
            if len(line) == 1 and line[0] != 0:
                return True
            
        # Check row
        for row in self.grid:
            for num_col in range(self.row_count - 2):
                if check(list(set(row[num_col:num_col+4]))): 
                    return True
                
        # Check column    
        for num_row in range(self.row_count - 3):
            for num_col in range(self.column_count):
                if check(list(set([self.grid[num_row+i][num_col] for i in range(4)]))):
                    return True
                
        # Check diagonal upward
        for num_row in range(self.row_count - 3):
            for num_col in range(self.column_count - 3):
                if check(list(set([self.grid[num_row+i][num_col+i] for i in range(4)]))):
                    return True

        # Check diagonal downward
        for num_row in range(3, self.row_count):
            for num_col in range(self.column_count - 3):
                if check(list(set([self.grid[num_row-i][num_col+i] for i in range(4)]))):
                    return True
        
        
        return False
                       
    
    "ACTIONS"
    def drop_pawn(self, column: int, player: int) -> bool:
        if self.is_move_possible(column):
            for i in range(self.row_count):
                if self.grid[self.row_count-i-1][column] == 0:
                   self.grid[self.row_count-i-1][column] = player
                   return True
        else:
            return False
    
    def empty_grid(self) -> None:
        """Clears the grid of all pawns.
        """
        self.grid = [[0] * self.column_count for ligne in range(self.row_count)]
        
        
    "DISPLAY"
    def print_grid(self) -> None:
        """Prints the current state of the board to the console
        """
        def style_pawn(p: int) -> str:
            match p:
                case 1:
                    return Fore.YELLOW + pawn1 + Style.RESET_ALL
                case 2:
                    return Fore.RED + pawn2 + Style.RESET_ALL
                case _:
                    return " "
        
        pawn1 = "⬤"
        pawn2 = "⬤"
                
        print(f" {''.join([str(i).center(4, ' ') for i in range(1, self.column_count+1)])} ")
        print(f" {''.join(["▼".center(4, ' ') for i in range(1, self.column_count+1)])} ")
        
        print(f"┌{'………┬'*(self.column_count-1)}………┐")
        
        for row in self.grid[:-1]:
            print(f"│ {' │ '.join(style_pawn(e) for e in row)} │")
            print(f"├{'───┼'*(self.column_count-1)}───┤")
            
        print(f"│ {' │ '.join(style_pawn(e) for e in self.grid[-1])} │")
        print(f"╚{'═══┴'*(self.column_count-1)}═══╝")
        


# TESTING
def test_board():
    b = Board()
    b.drop_pawn(4, 1)
    b.drop_pawn(3, 1)
    b.print_grid()
        
if __name__ == "__main__":
    test_board()      
