
from string import ascii_uppercase
def polybius(text):
  letters = ascii_uppercase.replace("J","")
  let_to_code = {char: str(i//5+1)+str(i%5+1) for i, char in enumerate(letters)}
  code_to_let = {v: k.lower() for k, v in let_to_code.items()} 
  let_to_code["J"] = let_to_code["I"]
  words = text.split(" ")
  if text[0].upper() in ascii_uppercase:
    return " ".join(["".join([let_to_code[char.upper()] for char in word if char.upper() in ascii_uppercase]) for word in words])
  else:
    return " ".join(["".join([code_to_let[word[2*i:2*i+2]] for i in range(int(len(word)/2))]) for word in words])

