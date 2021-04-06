
def digital_cipher(m, k):
  return  [(ord(m[i])-96)+int(str(k)[i%len(str(k))]) for i in range(len(m))]

