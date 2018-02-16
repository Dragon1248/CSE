world_map = {
    'BusStop': {
        'NAME': 'BUS',
        'DESCRIPTION': 'BusStop is where you wait for the bus to get a ride to anywhere',
        'PATHS': {
            'NORTH': 'HOUSE',
            'SOUTH': 'DINER'
        }
    },
    'DINER': {
        'NAME': 'Diner',
        'DESCRIPTION': 'Diner is where you can eat breakfast and Drink',
        'PATHS': {
            'NORTH': 'Store'
        }
    },
    'STORE': {
        'NAME': 'STORE',
        'DESCRIPTION': 'Store is where you can buy food',
        'PATHS': {
            'South': 'Mechanic',
            'East': 'House'
        }
    },
    'Mechanic': {
        'NAME': 'MECHANIC',
        'DESCRIPTION': 'MECHANIC is where you can get your car fixed ',
        'PATHS': {
            'NORTH': 'STORE',
            'East': 'HOUSE'
        }
    },

}




current_node = world_map['BusStop']
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
             current_node = world_map[name_of_node]
        except KeyError:
            print("You can not go this way")
    else:
        print("Command not recognized")