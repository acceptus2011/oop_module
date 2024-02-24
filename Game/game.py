import random

from models import Player, Enemy, GameOver

class Game:
    def __init__(self, player=None):
        self.player = player
        self.enemy = Enemy()
        self.level = "normal"

    def create_enemy(self):
        self.enemy = Enemy()

    def start_new_game(self):
        self.player = Player(input("Enter your name: "))
        difficulty = input("Select the difficulty level (normal 4 / high 8): ").lower()
        if difficulty == "8":
            self.enemy.scores = 8 
        self.play()

    def show_scores(self):
        if self.player is not None:
            print(f"Points player: {self.player.scores}")
        else:
            print("No player created yet.")

        print(f"Computer points: {self.enemy.scores}")

    def play(self):
        while True:
            try:
                player_choice = self.player.select_input()
                enemy_choice = random.choice(["1", "2", "3"])
                print(f"{self.player.name}: {player_choice}")
                print(f"Computer: {enemy_choice}")
                if player_choice == enemy_choice:
                    print("It's a tie!")
                elif (
                    (player_choice == "1" and enemy_choice == "2")
                    or (player_choice == "2" and enemy_choice == "3")
                    or (player_choice == "3" and enemy_choice == "1")
                ):
                    print(f"{self.player.name} win!")
                    self.player.activate_scores(is_winner=True)
                    self.enemy.activate_scores()
                else:
                    print("You lose!")
                    self.enemy.activate_scores(is_winner=True)
                    self.player.activate_scores()

                self.show_scores()

            except GameOver as e:
                print(f"Game over. {self.player.name} lose. Reason: {str(e)}")
                break
