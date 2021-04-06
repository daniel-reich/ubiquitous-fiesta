
def is_shape_possible(n, angles):
    if n > 2:
      angleSum = (n - 2) * 180
      
      if angleSum == sum(angles) and n == len(angles):
        for i in angles:
          if i >= 180:
            return False
        return True
      else:
        return False
    else:
      return False

