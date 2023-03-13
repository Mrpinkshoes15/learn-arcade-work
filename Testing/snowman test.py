class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west

def main():
    room_list = []

    room = Room("Welcome to your DOOM... You are in the entry way, there is a hallway to the east.", None, 1, None,
                None)
    room_list.append(room)

    room = Room("You are in the hallway, you can continue east or turn back to the west.", None, 1, None, 1)
    room_list.append(room)

    room = Room("you are in the main room now, you may continue to the east or to the north.", 1, 1, None, None)
    room_list.append(room)

    current_room = 0
    done = False

    while not done:
        print()
        print(room_list[current_room].description)
        direction = input("Which way would you like to go? (n s e w)").lower()
main()