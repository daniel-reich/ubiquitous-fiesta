
def who_goes_free(n, k):
  Prisoners = list(range(n))
  killer = 0
  while len(Prisoners) != 1:
    die = int((killer-1+k)%len(Prisoners))
    Prisoners.pop(die)
    killer = die
  return Prisoners[0]

