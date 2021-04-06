
def josephus(n):
  people = list(range(n))
  i = 0
  while len(people) > 1:
    i = (i+1) % len(people)
    people.pop(i)
  return False if n < 1 else people[0]

