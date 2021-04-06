
def sexagenary(year):
    first=['Metal', 'Metal', 'Water', 'Water', 'Wood', 'Wood', 'Fire', 'Fire', 'Earth', 'Earth']
    animals=['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Sheep', 'Monkey', 'Rooster', 'Dog', 'Pig']
    if year<2000:
        return str(first[int(str(year)[-1])])+" "+str(animals[int(str(year)[-2:])%12])
    else:
        return str(first[int(str(year)[-1])])+" "+str(animals[int(str(year)[-2:])%12+4])

