
def check_flush(table, hand):
  parse_suit = lambda card: card[-1]
  table_suit_list = list(map(parse_suit,table))
  for table_suit in table_suit_list:
    numSuit_table = table_suit_list.count(table_suit)
    if numSuit_table + list(map(parse_suit,hand)).count(table_suit) >= 5:
        return True
  return False

