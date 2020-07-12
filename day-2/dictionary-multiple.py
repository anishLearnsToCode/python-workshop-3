complex = {
    1: 100,
    'hello': 'world',
    'complex': {
        'i': 'am',
        range(1, 10): range(5, 10, 3)
    },
    5: [1, 2, 3, 4],
    'odd': [1, 3, 5, 7],
    'pi': 3.14,
    range(1, 9, 3): [
        190,
        [1, 2, 3],
        {
            'am': 'batman'
        }
    ]
}

print(complex[range(1, 9, 3)][2]['am'])
