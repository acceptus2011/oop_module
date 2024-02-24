import random

class Player:
    def __init__(self, name):
        self.name = name
        self.scores = 4

    def select_input(self):
        print("Choose: 1. Rock, 2. Scissors, 3. Paper")
        choice = input("Enter your choice (1/2/3): ")
        return int(choice)

    def activate_scores(self, is_winner=False):
        if is_winner:
            self.scores += 1
        else:
            self.scores -= 1
        if self.scores == 0:
            raise GameOver()

class Enemy:
    def __init__(self):
        self.scores = 4

    def activate_scores(self, is_winner=False):
        if is_winner:
            self.scores -= 1
        else:
            self.scores += 1

        if self.scores == 0:
            raise GameOver()
        
class GameOver(Exception):
    pass

