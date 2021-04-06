
def reverse_odd(txt):
  temp = list(txt.split(' '))
  for i in range(len(temp)):
    if len(temp[i]) % 2 == 1:
      temp[i] = temp[i][::-1]
  return ' '.join(temp)

