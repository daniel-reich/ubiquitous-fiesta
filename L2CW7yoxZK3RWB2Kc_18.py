
def nico_cipher(message, key):
  keys_lst = [y for y in key]
  sorted_lst = sorted(keys_lst)
  number = lambda i: sorted_lst.index(keys_lst[i]) + keys_lst[:i].count(keys_lst[i])
  message += (len(key) - (len(message) % len(key))) * " "
  groups = [message[x:x+len(key)] for x in range(0,len(message),len(key))]
  numbers = [number(x) for x in range(0,len(key))]
  index = lambda i: numbers.index(i)
  groups = [''.join(group[index(i)] for i in range(0,len(group))) for group in groups]
  return ''.join(groups)

