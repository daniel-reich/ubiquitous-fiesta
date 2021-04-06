
def split_bunches(d):
  return [{'name':b['name'], 'quantity':1} \
    for b in d for i in range(b['quantity'])]

