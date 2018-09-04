import time
import random

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('-------------------')
    print('  WIZARD GAME APP')
    print('-------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)
    ]
    hero = Wizard('Gandolf', 75)

    while True:
        creature = random.choice(creatures)
        print('The wizard {} sees a {}'.format(hero.name, creature.name))
        print()
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(creature):
                creatures.remove(creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
        elif cmd == 'r':
            print('The wizard {} runs away!'.format(hero.name))
        elif cmd == 'l':
            print('The wizard {} looks around and sees:'.format(hero.name))
            for c in creatures:
                print('* A level {} {}'.format(c.level, c.name))
        else:
            print('OK, exiting game... Bye!')
            break

        if not creatures:
            print("You've defeated all the creatures, well done!")
            break

        print()


if __name__ == '__main__':
    main()
