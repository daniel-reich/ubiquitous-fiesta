
def rank(lst):
   d = {}
   for i, x in enumerate(sorted(lst)):
      if x in d:
         d[x] = d[x] + [i]
      else:
         d[x] = [i]
   return [sum(d[x]) / len(d[x]) for x in lst]

