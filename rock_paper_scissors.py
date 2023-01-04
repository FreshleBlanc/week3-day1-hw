import random 


options = ['rock', 'paper', 'scissors']


class Game:
    def __init__(self):
        self.player = ""
        self.computer = ""
        self.options = options

    def checkvictory(self):
        print(self.player, self.computer)
        if self.player == self.computer:
            print("That's a Draw!")
        elif self.player == "paper" and self.computer == "rock":
            print("You Won!")
        elif self.player == "rock" and self.computer == "scissors":
            print("You Won!")
        elif self.player == "scissors" and self.computer == "paper":
            print("You Won!")
        else:
            print("You Lose.")


run = 'yes'
while run == 'yes':
    newgame = Game()
    newgame.player = (input('Rock, Paper, Scissors?')).lower()
    newgame.computer = random.choice(options)
    newgame.checkvictory()
    run = (input('Would you like to play again?')).lower()
