
def count_palindromes(num1, num2):
  lst = []
  for i in range(num1,num2+1):
    i = str(i)
    if i == i[::-1]:
      lst.append(i)
  return len(lst)

