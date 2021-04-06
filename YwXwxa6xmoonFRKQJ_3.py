
def josephus(n):
  people = [i for i in range(n)]
  index = 1
  if n < 1:
    return False
  elif n == 1:
    return 0
  else:
    while len(people) != 1:
      if people[index] == people[-1]:
        people.pop(index)
        index = 1
      elif people[index] == people[-2]:
        people.pop(index)
        index = 0
      else:
        people.pop(index)
        index += 1
    return people[0]
      
# [0, 1, 2, 3]

