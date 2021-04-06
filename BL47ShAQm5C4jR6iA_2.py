
def third_most_expensive(d):
  return False if not d or len(d)<3 else sorted(d, key=lambda x: d[x])[-3]

