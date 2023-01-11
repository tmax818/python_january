from players import players

tyler = {
    "name": "Tyler Jordan",
    "age": 25,
    "position": "small forward",
    "team": "Portland Trailblazers",
    "height": 10
    
}

class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']

# Complete challenge 3: Populate a new list with Player instances from the list of players.
# [<__main__.Player object at 0x0000020DAF044190>, <__main__.Player object at 0x0000020DAF044190>....]

player_objects = []

for player in players:
    player_obj = Player(player)
    print(player_obj)
    player_objects.append(player_obj)

player1 = Player(players[0])
player2 = Player(tyler)