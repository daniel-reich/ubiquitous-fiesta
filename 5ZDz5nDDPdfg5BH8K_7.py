
def only_5_and_3(n):
  return only_5_and_3_util(0, 0, n)
​
def only_5_and_3_util(current_number, increment, n):
    if increment == 3 and current_number > 0:
        current_number *= increment
    else:
        current_number += increment
    if current_number < n:
        for i in range(3, 6, 2):
            if only_5_and_3_util(current_number, i, n):
                return True
        return False
    elif current_number > n:
        return False
    else:
        return True

