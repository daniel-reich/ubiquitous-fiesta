
def sexagenary(year):
    stem = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
    branch = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig']
    return ' '.join([stem[((year-1984)%10)//2],branch[(year-1984)%12]])

