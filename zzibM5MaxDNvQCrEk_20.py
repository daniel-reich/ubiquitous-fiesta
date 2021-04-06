
def will_fit(holds, cargo):
  d = {'S' : 50, 'M':100, 'L': 200}
  return all(d[holds[x]] >= cargo[x] for x in range(len(holds)))

