
def fifty_thirty_twenty(ati):
  categories = ['Needs', 'Wants', 'Savings']
  percentages = [.5, .3, .2]
  return {c:ati*p for c, p in zip(categories, percentages)}

