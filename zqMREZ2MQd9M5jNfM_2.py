
def is_symmetrical(num):
  return num == int(''.join(reversed(list(str(num)))))

