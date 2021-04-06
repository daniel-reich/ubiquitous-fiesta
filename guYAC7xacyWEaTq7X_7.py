
def is_autobiographical(n):
  counts = {}
  n = str(n)
  for i in range(len(n)+1):
    counts[i] = 0
  for i in n:
    try:
      counts[int(i)] += 1
    except:
      return False
  for i in range(len(n)):
    if counts[i] != int(n[i]):
      return False
  return True

