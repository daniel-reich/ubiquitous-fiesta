
def create_letter_dict():
  d = dict()
  alphabet = "abcdefghiklmnopqrstuvwxyz"
  for i in range(5):
    for j in range(5):
      d[alphabet[5*i + j]] = str(i+1) + str(j+1)  
    
  d['j'] = '24'
  return d
​
def create_number_dict():
  d = dict()
  alphabet = "abcdefghiklmnopqrstuvwxyz"
  for i in range(5):
    for j in range(5):
      d[str(i+1) + str(j+1)] = alphabet[5*i + j]
​
  return d
​
def encode(txt):
  letter_dict = create_letter_dict()
  encoded = ""
  for letter in txt:
    encoded += letter_dict[letter.lower()]
​
  return encoded
​
def decode(txt):
  number_dict = create_number_dict()
  decoded = ""
  for i in range(len(txt)):
    if i % 2 == 0:
      decoded += number_dict[txt[i] + txt[i+1]]
​
  return decoded
​
def polybius(text):
  words_list = text.split(" ")
  final_txt = list()
  #if want to decode
  if words_list[0] <= "9" and words_list[0] >= "0":
    for word in words_list:
      final_txt.append(decode(word))
​
  #want to encode
  else:
    for word in words_list:
      final_txt.append(encode(word))
​
  return ' '.join(final_txt)
def create_letter_dict():
  d = dict()
  alphabet = "abcdefghiklmnopqrstuvwxyz"
  for i in range(5):
    for j in range(5):
      d[alphabet[5*i + j]] = str(i+1) + str(j+1)  
    
  d['j'] = '24'
  return d
​
def create_number_dict():
  d = dict()
  alphabet = "abcdefghiklmnopqrstuvwxyz"
  for i in range(5):
    for j in range(5):
      d[str(i+1) + str(j+1)] = alphabet[5*i + j]
​
  return d
​
def encode(txt):
  letter_dict = create_letter_dict()
  encoded = ""
  for letter in txt:
    encoded += letter_dict[letter.lower()]
​
  return encoded
​
def decode(txt):
  number_dict = create_number_dict()
  decoded = ""
  for i in range(len(txt)):
    if i % 2 == 0:
      decoded += number_dict[txt[i] + txt[i+1]]
​
  return decoded
​
def polybius(text):
  not_allowed = ["'", ".", "?", ":"]
  text = ''.join([i for i in text if i not in not_allowed])
  words_list = text.split(" ")
  final_txt = list()
  #if want to decode
  if words_list[0] <= "9" and words_list[0] >= "0":
    for word in words_list:
      final_txt.append(decode(word))
​
  #want to encode
  else:
    for word in words_list:
      final_txt.append(encode(word))
​
  return ' '.join(final_txt)

