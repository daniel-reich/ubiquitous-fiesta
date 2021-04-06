
def list_of_multiples (num, length):
  return [i for i in range(num, (num*length) + 1, num) if i%num == 0]

