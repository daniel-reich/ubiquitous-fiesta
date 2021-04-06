
def add_str_nums(n1, n2):
  final = []
  for n in n1,n2:
    if n == "":
      final.append(0)
    else:
      try:
        final.append(int(n))
      except:
        return "-1"
  return str(sum(final))

