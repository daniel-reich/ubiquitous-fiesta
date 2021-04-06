
def split(number):
  return 3*split(number-3) if number>4 else number

