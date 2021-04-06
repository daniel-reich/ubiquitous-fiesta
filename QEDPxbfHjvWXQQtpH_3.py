
def count_palindromes(num1, num2):
  tot = 0
  for i in range(num1, num2 + 1):
    i = str(i)
    cnt = 0
    pal = True
    while cnt < len(i):
      if i[cnt] is i[-(cnt + 1)]:
        cnt += 1
      else:
        pal = False
        break
    if pal is True:
      tot += 1
  return(tot)
print(count_palindromes(1, 10))

