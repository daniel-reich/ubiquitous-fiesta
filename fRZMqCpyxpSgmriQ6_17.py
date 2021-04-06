
def sorting(s):
  return "".join(sorted(s, key=lambda x: (x.isdigit(), x.lower(), x.isupper())))

