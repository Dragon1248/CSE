world_map = {
    'WESTHOUSE': {
        'NAME': 'West of House',
        'DESCRIPTION': 'You are west of a white house.',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'SOUTHHOUSE': {
        'NAME': 'South of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'North of house',
        'DESCRIPTION': "Insert Description Here",
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    },
    'BUSSTOP':  {
        'NAME': '',
        'DESCRIPTION': "Insert Description Here",
        'PATHS': {
            ''
        }
    }
}

current_node = world_map['WESTHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
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