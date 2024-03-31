from colorama import Fore, Back, Style

def print_choise_prompt():
    print("\n" + Fore.BLUE + "⇒ Your choice: " + Style.RESET_ALL, end="")
    
def print_goodbye(on_new_line: bool = True):
    if on_new_line:
        print()
    print(Fore.GREEN + "👋 Goodbye!" + Style.RESET_ALL, end="\n\n")
    print(Back.RED + "❌ Quitting..." + Style.RESET_ALL, end="\n\n")