
stems = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
branches = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig']
​
def sexagenary(year):
  y = year - 1300
  sx = ((y - 4) % 10) // 2
  bx = (y % 12)
  return ' '.join([stems[sx], branches[bx]])

