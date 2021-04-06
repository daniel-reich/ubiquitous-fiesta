
def describe_num(n):
  sentence = "The most "
  if n % 1 == 0:
    sentence += "brilliant "
  if n % 2 == 0:
    sentence += "exciting "
  if n % 3 == 0:
    sentence += "fantastic "
  if n % 4 == 0:
    sentence += "virtuous "
  if n % 5 == 0:
    sentence += "heart-warming "
  if n % 6 == 0:
    sentence += "tear-jerking "
  if n % 7 == 0:
    sentence += "beautiful "
  if n % 8 == 0:
    sentence += "exhilarating "
  if n % 9 == 0:
    sentence += "emotional "
  if n % 10 == 0:
    sentence += "inspiring "
  sentence += "number is " + str(n) + "!"
  return sentence

