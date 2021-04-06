
def mumbling(s):
  return "-".join((s[i]*(i+1)).title() for i in range(len(s)))

