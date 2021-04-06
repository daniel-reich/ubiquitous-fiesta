
def lychrel(n):
  count, num = 0, str(n)
  while num != num[-1::-1]:
    if count == 500: return True
    num = str(int(num) + int(num[-1::-1]))
    count += 1
  return count

