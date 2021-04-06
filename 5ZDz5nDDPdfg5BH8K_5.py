
def only_5_and_3(n):
  if n<6: return n in {3,5}
  return (only_5_and_3(n//3) if not n%3 else False) or (only_5_and_3(n-5) if n>5 else False)

