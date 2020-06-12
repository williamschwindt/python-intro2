class Item:
    def __init__(self, name):
        self.name = name

class Light(Item):
    def __init__(self, name, brightness):
        super().__init__(name)
        self.brightness = brightness
    def __str__(self):
        return f'{self.name} has a brightness of {self.brightness}'

class Tool(Item):
    def __init__(self, name, functional):
        super().__init__(name)
        self.functional = functional
    def __str__(self):
        return f'{self.name} is functional: {self.functional}'