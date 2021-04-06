
def nico_cipher(message, key):
  s = key + message
  col = len(key)
  row = int(len(s)/col + 0.99)
  s = s.ljust(row*col)
​
  lst = [(''.join(s[j*col+i] for j in range(row))) for i in range(col)]
  lst_sorted = sorted(lst, key=lambda x: x[0])
​
  sum = [''] * row
  for i in lst_sorted:
    both = zip(sum, i)
    sum = [x+y for (x,y) in both]
​
  return ''.join(j for j in sum[1:])

