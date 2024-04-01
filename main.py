import power4

def main():
    game = power4.Game()
    
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt: # Custom existing message
        power4.utils.prompt.goodbye()