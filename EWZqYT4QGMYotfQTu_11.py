
def tap_code(text):
  if text[:1]=='.':
    lst=text.split(' ')
    code=''
    for i in range(0, len(lst), 2):
      index = (len(lst[i])-1)*5 + len(lst[i+1])
      code += chr(index + ord('a')) if index > ord('k') - ord('a') else chr(index + ord('a') - 1)
    return code
  else:
    code=''
    for c in text:
      if c=='k':
        c='c'
      index = ord(c) - ord('a') if ord(c) < ord('k') else ord(c) - ord('a')-1
      row = index//5 + 1
      column = index%5 + 1 
      code += '.'*row + ' '+'.'*column + ' '
  return code[:-1]

