
def meme_sum(a, b):
  if len(str(a)) < len(str(b)):
    number_one = str(a)
    number_two = str(b)
    number_three = ''
    while len(number_one) < len(number_two):
      number_one = '0' + number_one
    for i in range(len(number_one)):
      number_three += str(int(number_one[i]) + int(number_two[i]))
    return int(number_three)
  else:
    number_one = str(a)
    number_two = str(b)
    number_three = ''
    while len(number_two) < len(number_one):
      number_two = '0' + number_two
    for i in range(len(number_two)):
      number_three += str(int(number_one[i]) + int(number_two[i]))
    return int(number_three)

