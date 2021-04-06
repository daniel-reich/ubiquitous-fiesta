
def steps_to_convert(txt):
  upper_count = len([i for i in txt if i.isupper()])
  return min(upper_count, len(txt) - upper_count)

