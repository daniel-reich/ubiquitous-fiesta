
def convert_binary(string):
  ascii_lowercase = 'abcdefghijklm'
  res = ['0'if i in ascii_lowercase else '1' for i in string.lower()]
  return ''.join(res)

