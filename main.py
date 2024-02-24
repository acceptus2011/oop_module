import random

from models import Player, Enemy, GameOver

from Game.game import Game

from models import GameOver

if __name__ == "__main__":
    game = Game()

    while True:
        print("Scroll:")
        print("1. Start a new game")
        print("2. Show points")
        print("3. Exit")
        choice = input("Select actions: ")

        if choice == "1":
            game.start_new_game()
        elif choice == "2":
            game.show_scores()
        elif choice == "3":
            print("Exit the game. Goodbye!")
            break
        else:
            print("Incorrect choice. Try again.")