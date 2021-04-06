
def sexagenary(year):
    stem = ['Wood', 'Wood', 'Fire', 'Fire', 'Earth', 'Earth',
            'Metal', 'Metal', 'Water', 'Water']
    branch = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse',
              'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig']
    return stem[(year - 1984) % 10] + ' ' + branch[(year - 1984) % 12]

