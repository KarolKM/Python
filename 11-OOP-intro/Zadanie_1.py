class Dog():

    def __init__(self, name, color, rase):
        self.name = name
        self.color = color
        self.rase = rase


    def voice(self, number = 1):
        return 'Hau ' * number


    def tail(self):
        return '{} wags the tail'.format(self.name)

obj_flash = Dog('Flash', 'White', 'Samoyed')
obj_arrow = Dog('Arrow', "Brown", "German Shepherd")
obj_atom = Dog('Atom', "Grey", "American Staffordshire")

print(obj_arrow.__dict__)
print(obj_flash.voice(10))
print(obj_atom.tail())
