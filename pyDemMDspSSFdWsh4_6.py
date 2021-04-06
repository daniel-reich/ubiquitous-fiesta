
def digital_decipher(eMessage, key):
  import string 
  a_z_list = list(string.ascii_lowercase)
  key_list = list(str(key))
  n = round(len(eMessage)/len(key_list))+1
  key_list = key_list*n
  result = []
  for i in range(len(eMessage)):
    code = eMessage[i] - int(key_list[i])
    index = code-1
    result.append(a_z_list[index])
  return ''.join(result)

