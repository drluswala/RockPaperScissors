"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']
"""The Player class is the parent class for all of the Players in this game."""
"""Define the learn method in the Player Class so it can be reused"""


class Player:
    my_move = 0
    their_move = 0

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class HumanPlayer(Player):

    def move(self):
        while True:
            userResponse = input('Select: Rock, Paper, or Scissors:')
            if userResponse.lower() not in moves:
                print('Input not valid:  Select Rock, Paper, or Scissors:')
            else:
                break
        return userResponse


class RockPlayer(Player):

    def move(self):
        return 'rock'


class RandomPlayer(Player):

    def move(self):
        return(random.choice(moves))


class ImitatePlayer(Player):

    def move(self):
        if self.their_move == 'paper':
            return 'paper'
        elif self.their_move == 'scissors':
            return 'scissors'


class CyclePlayer(Player):

    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissors'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            print("Player One Wins!")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Player Two Wins!")
            self.p2_score += 1
        else:
            print("It's a Tie!")

    def play_game(self):
        print("Game start!")
        while True:
            for round in range(9):
                print(f"Round number: {round + 1}")
                self.play_round()
            print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()
