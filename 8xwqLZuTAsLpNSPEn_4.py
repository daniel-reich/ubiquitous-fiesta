
def award_prizes(names):
  awards = ['Bronze','Silver','Gold']
  lst = sorted([k for k,v in names.items()],key=lambda x: names[x],reverse=True)
  return {k:(awards.pop() if awards else 'Participation') for k in lst}

