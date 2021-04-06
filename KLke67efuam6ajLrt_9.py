
def shuffle_count(num):
  ns, cards = 0, list(range(1, num+1))
  while ns==0 or cards[1]!=2:
    l1, l2 = cards[:num//2], cards[num//2:]
    cards[::2] = l1
    cards[1::2] = l2
    ns += 1
  return ns

