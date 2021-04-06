
ELEMENT = 'Metal ,Water ,Wood ,Fire ,Earth '.split(',')
ANIMAL = 'Monkey Rooster Dog Pig Rat Ox Tiger Rabbit Dragon Snake Horse Sheep'.split()
def sexagenary(year):
    return ELEMENT[year // 2 % 5] + ANIMAL[year % 12]

