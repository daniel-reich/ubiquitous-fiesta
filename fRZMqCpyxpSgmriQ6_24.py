
def sorting(s):
  l = "".join(filter(lambda x: x.isalpha(), sorted(sorted(s, reverse=True), key=str.lower)))
  n = "".join(i for i in sorted(s) if i.isdigit())
  return l + n

