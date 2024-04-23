class Cat:
    def __init__(self, name):
        self.name = name
        self.lives = 9

    def meow(self):
        print("{}: Meow!".format(self.name))
    
    def takeoff_life(self):
        if self.lives >= 1:
            self.lives -= 1
            print("{}: Meow! Oh no, I lost one life. I am down to {} lifes".format(self.name, self.lives))

    def eat(self, food):
        if food == 'fish':
            if self.lives < 9:
                self.lives += 1
            print("{}: Meow meow! I like {} very much! It makes me stronger".format(self.name, food))
        else:
            #Call takeoff_life method
            print("{}: Ugh, this was aweful, I hate {}. Without fish I will die.".format(self.name, food))
            self.takeoff_life()
    
    def alive(self):
        if self.lives > 9:
            print("{}: Something's wrong. I have more lives than I should!".format(self.name))
        elif self.lives > 0:
            print("{}: Meow! I feel very alive with {} lives left!".format(self.name, self.lives))
        else:
            print("{}: Meow. I'm feeling dead.".format(self.name))
    
 


# Create an instance of Cat with the name 'Smokey'
smokey = Cat('Smokey')

# Call the meow method
smokey.meow()

# Call the eat method with an argument
smokey.eat('fish')

# Call the alive method
smokey.alive()

