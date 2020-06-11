class Item:
    def __init__(self, name):
        self.name = name

class Torch(Item):
    def __init__(self, name, brightness):
        super().__init__(name)
        self.brightness = brightness
    def __str__(self):
        return f'{self.name} has a brightness of {self.brightness}'