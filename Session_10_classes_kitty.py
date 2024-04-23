class Kittie:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("{}: Meow!".format(self.name))

    def eat(self, food):
        print("{}: Meow meow! I like {} very much!".format(self.name, food))

# Create an instance of Kittie with the name 'Smokey'
smokey = Kittie('Smokey')

# Call the meow method
smokey.meow()

# Call the eat method with an argument
smokey.eat('catfood')
