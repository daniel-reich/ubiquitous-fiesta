
def is_heteromecic(n,i = 0):
    if n == i * (i + 1):
      return True
    if n < i * (i +1):
        return False
    i+=1
    return is_heteromecic(n, i)

