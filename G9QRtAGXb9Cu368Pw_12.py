
def combinations(*items):
    value1 = 1
    for num1 in items:
          if num1 != 0:
             value1 = num1 * value1
    return value1

