from room import Room
from player import Player
from item import Torch
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Torch('large old torch', 65)]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
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
        
#     except:
#         print("I'm not sure where the player wondered off to. Pick a different direction")
#         direction = input('Pick a direction. (n, s, e, w) or q to quit ')

def get_key(val): 
    for key, value in room.items(): 
         if val == value: 
             return key 
  
    return "key doesn't exist"

def has_items(cur_room):
    items = room[cur_room].items
    if len(items) > 0:
        print(f'In the corner of your eye you see something shimmer')
        inspect = input('Press i to investigate or m to move on ')

        if inspect == 'i':
            has_item = input(f'As you approach the shimmer you realize it is a {items[0].name}. Press y to pick up or n to leave on the ground ')
            if has_item == 'y':
                player.items.append(items[0])
                print(f'You have picked up the {items[0].name}')

game_playing = True

while game_playing == True:
    print(player)
    print(room[player.current_room].description)
    has_items(get_key(room[player.current_room]))
    direction = input('Pick a direction. (n, s, e, w) or q to quit ')

    if direction == 'q':
        break
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
        direction = input("I'm not sure where the player wondered off to. Press any key to go back ")

