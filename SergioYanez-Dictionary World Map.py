world_map = {
    'WESTHOUSE': {
        'NAME': 'West of House',
        'DESCRIPTION': 'You are west of a white house.',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'SOUTHHOUSE':{
        'NAME': 'South of House',
        'DESCIPTION': "Insert Description here",
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
    }
}