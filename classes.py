class Dog():    
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self):
        print(f"woof! my name is {self.name}")

my_dog = Dog('pug','princess')

print(f'{my_dog.name}')
my_dog.bark()

