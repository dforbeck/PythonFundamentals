from datetime import datetime
import pprint

class Human:
    earthian = True

    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday

    def have_birthday(self):
        self.age += 1
    
    def greet(self):
        return f'Hello my name is{self.name}'

    def human_globals(self):
        return globals()

mini_me = Human("Carson", 0, datetime(year=2019, month=6, day=27))

pprint.pprint(mini_me.__dict__)
# pprint makes print look nicer

pprint.pprint(dir(mini_me))
# dir to find out what methods and keys there are in your object
# pprint makes print look nicer

help(Human)


