import random


class Roll:

    pick = {    # [win, loss]
        'rock': ['scissors', 'paper'],
        'paper': ['rock', 'scissors'],
        'scissors': ['paper', 'rock']
    }

    def __init__(self, roll):
        self.roll = roll

    def win_loss(self, user):
        if Roll.pick[self.roll][0] == user.choice:
            print()
            print('{} beats {}'.format(self.roll.capitalize(), user.choice.capitalize()))
            print('Player is Defeated\n')
            user.loss += 1
            return False
        elif Roll.pick[self.roll][1] == user.choice:
            print()
            print('{} beats {}'.format(user.choice.capitalize(), self.roll.capitalize()))
            print('Player Wins!\n')
            user.win += 1
            return True
        else:
            print('Tie\n')
            return None


class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None
        self.win = 0
        self.loss = 0

    def get_roll(self):
        if self.name == 'Computer':
            self.choice = random.choice(rolls)
            print('{} chooses {}'.format(self.name, self.choice.roll.capitalize()))
        else:
            print('Please pick one of the following:\n[r]ock, [p]aper, [s]cissors')
            answer = input()
            while answer not in ['r', 'p', 's']:
                print('Error: Must enter r, p or s')
                answer = input()
            if answer == 'r':
                answer = 'rock'
            elif answer == 'p':
                answer = 'paper'
            elif answer == 's':
                answer = 'scissors'

            self.choice = answer
            print('Player chooses {}'.format(self.choice.capitalize()))


# game variables
rolls = [
    Roll('scissors'),
    Roll('rock'),
    Roll('paper')
    ]