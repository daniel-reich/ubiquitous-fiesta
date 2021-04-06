
def staircase(n):
  if n > 0:
    return "\n".join("_" * (n-i) + "#" * i for i in range(1, n+1))
  else:
    return "\n".join("_" * i + "#" * (-n-i) for i in range(-n))

