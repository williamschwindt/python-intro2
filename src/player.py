class Player:
    def __init__(self, name, current_room, items):
        self.name = name
        self.current_room = current_room
        self.items = items
    def __str__(self):
        return f' Your location: {self.current_room}'
