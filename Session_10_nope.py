""" if list:
    print ('There is something in the list!')
else:
    print ('The list is empty!')


a = [1, 2, 3]
b = list(a)

print(b)
a.append(4)
print(b)
print(a)
b = a
print(b)

power_of_two = []
for number in range (10):
    power_of_two.append (2 ** number)
print(power_of_two)

words = 'This sentence is complex, split it into words!'.split()
print(words)

records = '3A, 8B, 2E, 9D'.split(',')
print(records)

sentence = ' '.join(words)
print(sentence) """

#records = ['john doe', 'John Smith', 'Stuart little', 'petr File']
#def record_control(records):
 #   error_entries = []
  #  ok_entries = []
   #    corected_entries = []

class Katze:
    def __init__(self, name, farbe, alter):
        self.name = name
        self.farbe = farbe
        self.alter = alter

    def miauen(self):
        return "{}: Miau!".format(self.name)

    def vorstellen(self):
        return "Ich bin {} und ich bin eine {} Katze und {} Jahre alt.".format(self.name, self.farbe, self.alter)

# Erstellen von drei verschiedenen Katzen
katze1 = Katze("Whiskers", "schwarze", 3)
katze2 = Katze("Socks", "weiße", 2)
katze3 = Katze("Bella", "getigerte", 5)

# Jede Katze ruft die Methode miauen auf
print(katze1.miauen())
print(katze2.miauen())
print(katze3.miauen())

# Jede Katze stellt sich vor
print(katze1.vorstellen())
print(katze2.vorstellen())
print(katze3.vorstellen())