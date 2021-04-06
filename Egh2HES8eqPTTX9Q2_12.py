
def rolling_cipher(txt, n):
  code = "".join(chr(i + ord('a')) for i in range(26))
  if n > 0:
    for i in range(n):
      code = code[1:] + code[:1]
  else:
    for i in range(-n):
      code = code[-1:] + code[:-1]
  return code[:len(txt)]

