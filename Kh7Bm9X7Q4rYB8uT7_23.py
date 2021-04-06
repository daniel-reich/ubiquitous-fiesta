
def is_vowel_sandwich(s):
  s1 = list(s)
  print(s1)
  if len(s1) == 3:
    if s1[1] in ('a','e','i','o','u'):
      if s1[0] not in ('a','e','i','o','u') and s1[2] not in ('a','e','i','o','u'):
        return True
      else:
        return False
    else:
      return False
  else:
    return False

