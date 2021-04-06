
def rolling_cipher(txt, n):
  import string
  full = string.ascii_lowercase
  print(full)
  txt_result=''
  for each_letter in txt:
    num = full.find(each_letter)
    print(num)
    offset = (num + n) % len(full)
    print(offset)
    if offset < 0: ofsset = len(full) + offset
    print(offset)
    txt_result = txt_result + full[offset]
    print(txt_result) 
  return txt_result

