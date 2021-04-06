
def determine_who_cursed_the_most(d):
  me = sum(ro["me"] for ro in d.values())
  sp = sum(ro["spouse"] for ro in d.values())
  
  return 'ME!' if me>sp else 'SPOUSE!' if me<sp else 'DRAW!'

