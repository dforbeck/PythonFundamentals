class Cat:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'<CAT: {self.name}>'
    
    def __str__(self):
        return f'{self.name} is a cat.'

fido = Cat("Fido")

print(fido)
print(str(fido))