
def square_digits(n):
  answer = ""
  n = str(n)
  for i in n:
    answer += str(int(i)**2)
  return int(answer)

