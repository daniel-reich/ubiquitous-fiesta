
def steps_to_convert(txt):
  low = [i for i in txt if i.islower()]
  high = [i for i in txt if i.isupper()]
  return len(low) if len(high) > len(low) else len(high)

