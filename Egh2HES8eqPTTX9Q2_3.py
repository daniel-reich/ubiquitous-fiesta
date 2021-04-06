
def rolling_cipher(t,n):
  return "".join([chr(((ord(i)+n-97)%26)+97) for i in t])

