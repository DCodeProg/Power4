from colorama import Fore, Back, Style

# MENUS RELATED FUNCTIONS
def label(text: str):
    """This function prints the given text in a yellow color (for section/menu title).

    Args:
        text (str): The text to be printed.
    """
    print(Fore.YELLOW + text + Style.RESET_ALL)

def your_choice():
    """This function prompts the user to enter a choice.
    """
    print("\n" + Fore.BLUE + "⇒ Your choice: " + Style.RESET_ALL, end="")
    
def back_to_main_menu():
    """Prompts the user to press enter to go back to the main menu.
    """
    print("\n" + Fore.BLUE + "⇒ Press <ENTER> to go back in main menu" + Style.RESET_ALL, end=" ")


# GAME TITLE
def game_title():
    """Show game title in the console
    """
    print(Fore.CYAN + """ _____                   ___ 
|  _  |___ _ _ _ ___ ___| | |
|   __| . | | | | -_|  _|_  |
|__|  |___|_____|___|_|   |_|
""", Style.RESET_ALL)


# ERRORS RELATED FUNCTIONS
def error(text: str):
    """Print the given text in red color to display an error message.

    Args:
        text (str): The text to be printed.
    """
    print(Back.LIGHTRED_EX + text + Style.RESET_ALL)
    
def goodbye(on_new_line: bool = True):
    """Print a goodbye message to the console.

    Args:
        on_new_line (bool, optional): Whether to print the message on a new line. Defaults to True.
    """
    if on_new_line:
        print()
        
    print(Fore.GREEN + "👋 Goodbye!" + Style.RESET_ALL, end="\n\n")
    print(Back.RED + "❌ Quitting..." + Style.RESET_ALL, end="\n\n")