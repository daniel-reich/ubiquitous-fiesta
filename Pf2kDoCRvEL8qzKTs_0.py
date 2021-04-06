
def order_people(lst, people):
  if people > lst[0] * lst[1]:
    return 'overcrowded'
  #list of people plus all the placeholder zeroes
  p = list(range(1, people +1)) + [0]*(lst[0]*lst[1] - people)
  #forward slice of length lst[1] if index even, backward if odd
  return [p[0+i:i+lst[1]] if (i//lst[1])%2==0 else p[i+(lst[1]-1):i-1:-1] for i in range(0, len(p), lst[1])]

