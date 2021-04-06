
def sexagenary(year):
  st="Metal Water Wood Fire Earth".split()
  br="Monkey Rooster Dog Pig Rat Ox Tiger Rabbit Dragon Snake Horse Sheep".split()
  return st[year%10//2] + " " + br[year%12]

