
def digits(number):
  number -= 1
  acc = 0
  if (number < 10):
    return number % 10
  else:
    acc += (number - int("9" * (len(str(number)) - 1))) * len(str(number))
    for i in range(len(str(number)) - 2, 0, -1):
      acc += (int("9" * (i + 1)) - int("9" * i)) * (i + 1)
    return acc + 9

