
def number_split(n):
  return [int(n/2)]*2 if not n%2 else [int(n/2), int(n/2)+1] if n > 0 else [int(n/2)-1, int(n/2)]

