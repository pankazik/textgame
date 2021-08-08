import random


class Character:
    def __init__(self, hp, dex, strength, inteligence):
        self.hp = hp
        self.dex = dex
        self.str = strength
        self.int = inteligence
        self.gold = 0

    def __repr__(self):
        return f"hp: {self.hp} dex: {self.dex} str: {self.str} int: {self.int} gold: {self.gold}"


def fight(setplayer, setenemy):
    if setplayer.hp <= 0:
        print('u died')
        input()
        exit('u died')
    if setenemy.hp <= 0:
        del setenemy
        goldroll = random.randint(25, 40)
        print(f'u won and loot : {goldroll} gold')
        setplayer.gold += goldroll
        options()

    print("enemy hp :" + str(setenemy.hp) + "\nplayer hp :" + str(setplayer.hp) + '\na to attack r to escape')
    choice = input()
    if choice.lower() == 'a':
        setenemy.hp -= random.randint(5, 10) * setplayer.str
        setplayer.hp -= random.randint(5, 10) * setenemy.str
        return fight(setplayer, setenemy)
    if choice.lower() == 'r':
        if setplayer.dex + random.randint(1, 10) - setenemy.dex > 10:
            print('escaped successfully')
            del setenemy
            options()
        else:
            print("escape failed|enemy attacked")
            setplayer.hp -= random.randint(5, 10) * setenemy.str
            return fight(setplayer, setenemy)

    else:
        print("wrong action")
        return fight(setplayer, setenemy)


def road():
    print('Empty road')
    for a in range(1, 11):
        if a == 6:
            print(10 * '  ' + "o")
        print(9 * ' *' + '    ' + 9 * ' *')
    options('road')


def forest():
    print('Forest')
    for a in range(1, 11):
        if a == 6:
            print(10 * '  ' + "o")
        print(9 * '/|' + '    ' + 9 * '/|')
    options('forest')


def city():
    print('City')
    for a in range(1, 11):
        if a == 3:
            print(' +  W E A P O N  +     + + + G Y M + + +')
        if a == 6:
            print(10 * '  ' + "o")
        if a == 9:
            print(' +  T A V E R N  +     + T H I E V E S +')
        print(9 * ' +' + '    ' + 9 * ' +')
    options('city')


def cave():
    print('Dark cave')
    for a in range(1, 11):
        print(9 * 'OO' + '    ' + 9 * 'OO')
    options("Cave")


def randomroad():
    optionset = [road, forest, cave, city]
    choice = random.randint(0, 2)
    townroll = random.randint(1, 6)
    if townroll == 3:
        choice = 3
    return optionset[choice]()


def headinchat(sight, loc):
    sights = {'e': 'You are heading East, straight to the ', 'w': 'You are heading West, straight to the ',
              'n': 'You are heading North, straight to the ', 's': 'You are heading South, straight to the '}
    if sight in sights:
        return print(sights[sight]), randomroad()
    else:
        return print('Wrong option'), options(loc)


def options(loc=None):
    if loc:
        print(f"Your actual position is : {loc}")
    print(
        f' Which way do you want to go ?\n E-East W-West N-North S-South\n exit to exit f - to find an enemy \n'
        f' stats {player} \nType:')
    if loc == 'city':
        print(f"While you are in city,type 'gym',to train your strength at the GYM for {(player.str + 5) * 4}"
              f" gold or 'heal' to heal 250HP for 20 gold")
    typed = input()
    if typed.lower() == 'exit':
        exit()
    if typed.lower() == 'f' and loc != 'city':
        enemy1 = Character(random.randint(200, 600), 5, 6, 7)
        fight(player, enemy1)
    if typed.lower() == 'gym' and loc == 'city':
        if player.gold >= (player.str + 5) * 4:
            player.str += 1
            player.gold -= (player.str + 5) * 4
        else:
            print('not enough gold')
        options('city')
    if typed.lower() == 'heal' and loc == 'city':
        if player.gold >= 15:
            player.hp += 250
            player.gold -= 15
        else:
            print('not enough gold')
        options('city')
    headinchat(typed, loc)


player = Character(700, 10, 10, 10)

print(' You woke up in a lost city.\n You dont remember anything.')
options()
