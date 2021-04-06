
def will_fit(holds, cargo):
  counter = 0
  mydct = {'S':50,'M':100,'L':200}
  for i in set(holds):
    counter+= holds.count(i) * mydct[i]
  if counter >= sum(cargo):
    return True
  return False

