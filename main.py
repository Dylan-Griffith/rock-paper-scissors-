from variables import Player
from time import sleep


def main():
    intro()
    player = Player('Dylan')
    computer = Player('Computer')
    while player.loss != 3:
        print('Player wins : {win}'.format(win=player.win))
        player.get_roll()
        sleep(1)
        computer.get_roll()
        sleep(1)
        computer.choice.win_loss(player)
        if not replay():
            break
        clear()


def clear():
    print('\n' * 25)


def intro():
    print('-------------------------')
    print('  Rock, Paper, Scissors')
    print('-------------------------')


def replay():
    print('Press enter to play again:')
    answer = input()
    if answer != '':
        return False
    return True


if __name__ == '__main__':
    main()