
def is_autobiographical(n):
  return all(str(n).count(str(i))==int(str(n)[i]) for i in range(len(str(n))))

