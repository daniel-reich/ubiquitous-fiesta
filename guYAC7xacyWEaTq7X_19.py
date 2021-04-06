
def is_autobiographical(n):
  n = str(n)
  for i in range(len(n)):
    count = 0
    for digit in n:
      if digit == str(i):
        count += 1
    if str(count) != n[i]:
      return False
  return True
    
print(is_autobiographical(6210001000))

