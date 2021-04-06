
def reverse_list(num):
  lst = []
  while num>0:
    lst.append(num % 10)
    num = num//10
  return lst

