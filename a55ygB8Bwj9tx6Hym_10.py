
def steps_to_convert(txt):
  return len([i for i in txt if i.isupper()]) if len([i for i in txt if i.isupper()]) < len(txt) / 2 else len(txt) - len([i for i in txt if i.isupper()])

