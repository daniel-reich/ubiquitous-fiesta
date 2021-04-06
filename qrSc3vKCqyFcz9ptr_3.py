
def sum_round(num):
  places = [x + '0'*i for i, x in enumerate(str(num)[::-1]) if int(x)]
  return ' '.join(places)

