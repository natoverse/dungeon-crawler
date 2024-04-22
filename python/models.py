
class Player():
    def __init__(self, name='Player', starting_position=[1, 1]):
        self.position = starting_position
        self.name = name
        self.health = 100
        self.symbol = '🥷'
        self.gold = 0   


class Monster():
    def __init__(self, name='Monster', starting_position=[1, 1]):
        self.position = starting_position
        self.name = name
        self.health = 100
        self.symbol = '👹'