class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{}: I like {} very much!".format(self.name, food))


class Kittie(Animal):
    def meow(self):
        print("{}: Meow!".format(self.name))


class Doggie(Animal):
    def woof(self):
        print("{}: Woof!".format(self.name))

class snake(Animal):
    def __init__(self, name):
        name = name.replace('s', 'sss')
        name = name.replace('S', 'Sss')
        super().__init__(name)


stanley = snake('Susi')
stanley.eat('mouse')

smokey = Kittie('Smokey')
smokey.meow()
smokey.eat('mouse')

doggo = Doggie('Doggo')
doggo.woof()
doggo.eat('bone')

