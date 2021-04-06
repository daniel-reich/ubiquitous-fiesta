
def sexagenary(year):
    stems = ('Wood', 'Wood', 'Fire', 'Fire', 'Earth', 'Earth', 'Metal', 'Metal', 'Water', 'Water')
    branches = ('Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig')
    
    diff = year - 1984
    return ' '.join((stems[diff%10], branches[diff%12]))

