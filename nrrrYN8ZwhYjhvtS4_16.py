
def extend_vowels(word, num):
  if num == int(abs(num)):
    return ''.join([i*(num+1) if i.lower() in 'ioeau' else i for i in word])
  else:
    return "invalid"

