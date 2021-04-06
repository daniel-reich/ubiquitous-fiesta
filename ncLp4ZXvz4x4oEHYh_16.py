
def sum_of_two(a, b, v):
  complement = v-a[0]
  if complement in b:
    return True
  else:
    complement = v-a[1]
    if complement in b:
      return True
    else:
      complement = v-a[2]
      if complement in b:
        return True
  return False

