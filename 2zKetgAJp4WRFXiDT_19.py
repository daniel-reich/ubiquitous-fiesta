
def number_length(num):
  return 1 if num<10 else 0 if num==9 else 1+number_length(num//10)

