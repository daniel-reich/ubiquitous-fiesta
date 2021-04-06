
def josephus(n):
  people = [x for x in range(n)]
  if len(people) < 1: return False
  person, kill = 0, True
  while people.count(-1) < n-1:
    person += 1
    person %= n
    if people[person] >= 0 and kill:
      people[person] = -1
      kill = False
    elif people[person] >=0 and not kill:
      kill = True
  return max(people)

