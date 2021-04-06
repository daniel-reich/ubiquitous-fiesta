
def digital_decipher(eMessage, key):
  cypher = {1:"a" ,2:"b",3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}
  key = str(key)
  current_index = 0
  x = ""
  for index, i in enumerate(eMessage):
    i = i- int(key[current_index])
    current_index += 1
    if current_index == len(key):
      current_index = 0
    x += cypher[i]
  return x

