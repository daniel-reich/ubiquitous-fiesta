
def binary_conversion(txt):
  answer = ''
  for i in range(len(txt) // 8):
    substring = txt[8*i:8*(i+1)]
    answer += chr(int(substring, 2))
  return answer

