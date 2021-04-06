
import binascii
def binary_conversion(txt):
  if txt == '':
    return ''
  return binascii.unhexlify('%x' % int(txt, 2)).decode("utf-8")

