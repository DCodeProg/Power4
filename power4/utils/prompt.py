from colorama import Fore, Back, Style

def your_choice():
    print("\n" + Fore.BLUE + "⇒ Your choice: " + Style.RESET_ALL, end="")
    
def back_to_main_menu():
    print("\n" + Fore.BLUE + "⇒ Press <ENTER> to go back in main menu" + Style.RESET_ALL, end=" ")
    
def goodbye(on_new_line: bool = True):
    if on_new_line:
        print()
    print(Fore.GREEN + "👋 Goodbye!" + Style.RESET_ALL, end="\n\n")
    print(Back.RED + "❌ Quitting..." + Style.RESET_ALL, end="\n\n")