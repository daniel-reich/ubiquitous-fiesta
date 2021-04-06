
### returns polybius square reference for a given letter
def polybius(letter):
  n = ord(letter) - 97
  if n > 8:
    n -= 1
  return [n//5 + 1, n%5 + 1]
​
### main function
def bifid(txt):
  ### encryption
  if " " in txt:
    ### prepare plaintext
    txt = "".join(char for char in txt.lower().replace("j","i") if char.isalpha())
    
    ### get polybius square row and column values 
    rows, columns = [], []
    for letter in txt:
      value = polybius(letter)
      rows.append(value[0])
      columns.append(value[1])
    
    ### scramble values
    num_lst = rows + columns
    letter_codes = [[num_lst[i],num_lst[i+1]] for i in range (0,len(num_lst),2)]
  
  ### decryption  
  else:
    ### get polybius values
    num_lst = []
    for letter in txt:
      num_lst += polybius(letter)
    
    ### unscramble values
    n = len(num_lst)//2
    letter_codes = [[num_lst[i],num_lst[i+n]] for i in range (n)]
  
  ### get output text
  output = ""
  for code in letter_codes:
    n = (code[0]-1) * 5 + code[1] + 96
    if n > 105:
      n += 1
    output += chr(n)
  
  return output

