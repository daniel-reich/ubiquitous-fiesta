
def kempner(value):
    index = 1
    factorial = 1
    while True:
        factorial = factorial * index
        if factorial % value == 0:
          return index
        else:
           index = index + 1

