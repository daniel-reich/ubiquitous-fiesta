
from random import shuffle as CHAOS
def gen_deck():
  MahDek = [(x, y) for x in range (2, 15) for y in ('c','d','h','s')]
  CHAOS(MahDek)
  return MahDek

