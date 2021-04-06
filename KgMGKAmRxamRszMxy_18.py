
def spartans_cipher(message, n_Slide):
  col = int(len(message) / n_Slide + 0.99)
  message = message.ljust(col * n_Slide)
  a = [message[slice(i*col, (i+1)*col)] for i in range(n_Slide)]
  sum = [''] * col
  for i in a:
    for j in range(col):
      sum[j] += i[j]
    new_message = ''.join(k for k in sum).strip()
  return new_message

