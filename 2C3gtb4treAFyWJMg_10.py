
def polybius(text):
  if str.isdigit(text[0]):
    return decode(text)
  return encode(text)
​
def encode(text):
  encode_dict = {
    "A": "11", "B": "12", "C": "13", "D": "14", "E": "15", 
    "F": "21", "G": "22", "H": "23", "I": "24", "J": "24", "K": "25",
    "L": "31", "M": "32", "N": "33", "O": "34", "P": "35",
    "Q": "41", "R": "42", "S": "43", "T": "44", "U": "45",
    "V": "51", "W": "52", "X": "53", "Y": "54", "Z": "55", " ": " "
  }
  
  s = ""
  for char in str.upper(text):
    if char in encode_dict:
      s += str.lower(str(encode_dict.get(char)))
    
  return s
​
def decode(text):
  decode_dict = {
    "11": "A", "12": "B", "13": "C", "14": "D", "15": "E", 
    "21": "F", "22": "G", "23": "H", "24": "I", "25": "K",
    "31": "L", "32": "M", "33": "N", "34": "O", "35": "P",
    "41": "Q", "42": "R", "43": "S", "44": "T", "45": "U",
    "51": "V", "52": "W", "53": "X", "54": "Y", "55": "Z" 
  }
  
  s = ""
  i = 0
  while i < len(text) - 1:
    if text[i] == ' ':
      s += ' '
      i += 1
    else:
      temp = text[i] + text[i+1]
      if temp in decode_dict:
        s += str.lower(str(decode_dict.get(temp)))
        i += 2
  return s

