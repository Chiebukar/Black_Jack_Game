class Player(object):
    def blast(self, enemy):
        enemy.die()


class Alien(object):
    def die(self):
        print("Oh, you didn't have to do that, now i am dead ")


hero = Player()
invader = Alien()

hero.blast(invader)

