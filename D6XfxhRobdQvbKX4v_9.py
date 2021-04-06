
def first_before_second(s, first, second):
  first_found = False
  second_found = False
  for letter in s:
      if letter == first:
          if second_found:
              return False
          first_found = True
      elif letter == second:
          if first_found == False:
              return False
          second_found = True
  return True

