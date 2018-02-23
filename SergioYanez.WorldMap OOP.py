class Room(object):
    def __init__(self, name, north, south, west, east):
        self.name = name
        self.north = north
        self.south = south

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self,direction)]


hdum = Room()





current_node = hdum
directions = ['north', 'south', 'east', 'west']

while True:
    print(current_node['NAME'])  # change
    print(current_node['DESCRIPTION'])  # change
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
             name_of_node = current_node['PATHS'][command]
             print(name_of_node)
        except KeyError:
            print("You can not go this way")
    else:
        print("Command not recognized")