
def shuffle_count(num):
  deck = list(range(num))
  un_shf = list(range(num))
  s_num = 0
  hlf = num // 2
  while True:
    new_deck = []
    for i in range(hlf): new_deck += [deck[i], deck[i + hlf]]
    deck = new_deck
    s_num += 1
    if deck == un_shf: return s_num

