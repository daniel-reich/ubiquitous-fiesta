
TABLE = str.maketrans('EAea','WEwe')
def direction(lst):
  return [i.translate(TABLE) for i in lst]

