
def check_flush(table, hand):
  handTypes = [i[-1] for i in hand]
  tableTypes = [i[-1] for i in table]
  
  overallTypes = handTypes + tableTypes
  for card in overallTypes:
    if overallTypes.count(card) >=5:
      return True
  return False

