
def sexagenary(year):
  stem = ['Wood','Wood','Fire','Fire','Earth','Earth','Metal','Metal','Water','Water','Wood','Wood','Fire','Fire']
  branch = ['Rat','Ox','Tiger','Rabbit','Dragon','Snake','Horse','Sheep','Monkey','Rooster','Dog','Pig','Rat','Ox']
  return ' '.join([stem[(year-1984)%10], branch[(year-1984)%12]])

