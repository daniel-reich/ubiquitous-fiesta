
def hamming_code(message):
  lst = ["{:0>8}".format(bin(ord(i))[2:]) for i in message]
  return ''.join(i*3 for i in ''.join(lst))

