
def encrypt(key, message):
  lst_message = list(message)
  for i in range(len(lst_message)):
    idx = key.find(lst_message[i])
    if idx != -1:
      if idx % 2 == 0:
        lst_message[i] = key[idx + 1]
      else:
        lst_message[i] = key[idx - 1]
  return ''.join(lst_message)

