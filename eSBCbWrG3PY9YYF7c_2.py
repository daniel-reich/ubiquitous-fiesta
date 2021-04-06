
def sexagenary(year):
    elements = 'Wood, Fire, Earth, Metal, Water'.split(', ')
    animals = 'Rat, Ox, Tiger, Rabbit, Dragon, Snake, Horse, Sheep, Monkey, Rooster, Dog, Pig'.split(', ')
    return '{} {}'.format(elements[(year%10)//2-2], animals[(year%12)-4])

