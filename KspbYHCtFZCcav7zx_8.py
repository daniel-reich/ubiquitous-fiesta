
def bill_split(spicy, cost):
  return [round(sum([i[1] if i[0]=="S" else i[1]/2 for i in zip(spicy,cost)])),\
  sum(cost)-round(sum([i[1] if i[0]=="S" else i[1]/2 for i in zip(spicy,cost)]))]

