
def gold_distribution(gold):
  a = []
  while len(gold)!=0:
      if gold[0]>=gold[-1]:
          a.append(gold[0])
          gold = gold[1:]
      else:
          a.append(gold[-1])
          gold.pop()
  b = [a[i] for i in range(len(a)) if i%2]
  c = [a[i] for i in range(len(a)) if i%2==0]
  return [sum(c), sum(b)]

