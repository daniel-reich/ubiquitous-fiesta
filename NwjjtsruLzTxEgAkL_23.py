
from re import match
def assignment(date):
  return match(r"\d{4}/(" + '|'.join(['%02d' % i for i in range(1,13)])+ ')/('+  '|'.join(['%02d' % i for i in range(1, 32)]) +')', date) is not None

