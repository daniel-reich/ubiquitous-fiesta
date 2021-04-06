
def sexagenary(year):
  stems=('Metal','Metal','Water','Water','Wood','Wood','Fire','Fire','Earth','Earth')
  branches=('Monkey','Rooster','Dog','Pig','Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep')
  return stems[year%10]+' '+branches[year%12]

