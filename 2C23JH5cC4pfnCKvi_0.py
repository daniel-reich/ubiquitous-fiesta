
def check_flush(table, hand):
  return any(sum(card[-1] == suit for card in table+hand) > 4 for suit in 'CHSD')

