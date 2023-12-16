class PlayerCharacter:
    #Class Object Attribute
    membership = True
    def __init__(self, name='anonymous', age=21):
        self.name = name #attributes
        self.age = age

    def run(self):
        print('run')
        return ('done')

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 21)
player3 = PlayerCharacter()

print(player2.membership)
print(player1.membership)
print(player3.name, player3.age)