from room import Room
from player import Player
from item import Light
from item import Tool
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Light('large old torch', 65), Light('broken torch', 0)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Tool('metal detector', True)]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been emptied by
earlier adventurers and all that is left is one single gold coin. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('william', 'outside', [])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
        

def get_key(val): 
    for key, value in room.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def inspect_item(number):
    items = room[get_key(room[player.current_room])].items

    has_item = input(f'As you approach the shimmer you realize it is a {items[number].name}. Press y to pick up or n to leave on the ground ')
    if has_item == 'y':
        player.items.append(items[number])
        print(f'You have picked up the {items[number].name}')
        items.pop(number)


def has_items(cur_room):
    items = room[cur_room].items
    if len(items) == 1:
        print(f'In the corner of your eye you see something shimmer')
        inspect = input('Press i to investigate or m to move on ')

        if inspect == 'i':
            inspect_item(0)

    elif len(items) == 2:
        inspect = input('You see two items shimmering on either side of you. Press l to inspect the item to the left, r to inspect the item to the right or m to move on ')

        if inspect == 'l':
            inspect_item(0)
        elif inspect == 'r':
            inspect_item(1)

def drop_item():
    item_name = input('Type the name of an item in your inventory to drop ')
    player.items = [item for item in player.items if item.name != item_name]
    print(f'You have droped the {item_name}')

def metal_detector(detector):
    if detector.functional == True:
        print(f'Your metal detector starts beeping. As you look down at it an arrow pointing north appears')
    elif detector.functional == False:
        print(f'Your metal detector starts beeping rapidly before it explodes in your hand')

game_playing = True

while game_playing == True:
    print(chr(27))
    print(player)
    print(room[player.current_room].description)

    if len(player.items) > 0:
            print(f'Items currently holding: ')
            for item in player.items:
                print(item.name)

    has_items(get_key(room[player.current_room]))

    if player.current_room == 'narrow':
        for item in player.items:
            if item.name == 'metal detector':
                metal_detector(item)

    direction = input('Pick a direction. (n, s, e, w) or q to quit. Also press d to drop an item ')

    if direction == 'q':
        break

    elif direction == 'd':
        drop_item()

    elif direction == 'n' and hasattr(room[player.current_room], 'n_to'):
        full_new_room = room[player.current_room].n_to
        new_room = get_key(full_new_room)
        player.current_room = new_room

    elif direction == 's' and hasattr(room[player.current_room], 's_to'):
        full_new_room = room[player.current_room].s_to
        new_room = get_key(full_new_room)
        player.current_room = new_room

    elif direction == 'e' and hasattr(room[player.current_room], 'e_to'):
        full_new_room = room[player.current_room].e_to
        new_room = get_key(full_new_room)
        player.current_room = new_room

    elif direction == 'w' and hasattr(room[player.current_room], 'w_to'):
        full_new_room = room[player.current_room].w_to
        new_room = get_key(full_new_room)
        player.current_room = new_room
    else:
        direction = input("All you see ahead is a thick layer of fog. Press any key to go back ")


