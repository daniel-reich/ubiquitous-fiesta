
def baconify(*args):
  alphabet = {'a': '11111', 'b': '11110', 'c': '11101', 'd': '11100', 'e': '11011', 'f': '11010', 'g': '11001',
              'h': '11000', 'i': '10111', 'j': '10110', 'k': '10101', 'l': '10100', 'm': '10011', 'n': '10010',
              'o': '10001', 'p': '10000', 'q': '01111', 'r': '01110', 's': '01101', 't': '01100', 'u': '01011',
              'v': '01010', 'w': '01001', 'x': '01000', 'y': '00111', 'z': '00110', '.': '00001', ' ': '00000'}
  rev_alphabet = {i: j for j, i in alphabet.items()}
  
  if len(args) == 1:
    mask = "".join([i for i in str(args[0]) if i.isalpha()])
    split_str = []
    for i in range(len(mask) // 5):
        split_str.append(mask[i * 5:(i + 1) * 5])
    for i in range(len(split_str)):
      for letter in list(split_str[i]):
        if letter.isupper():
          split_str[i] = split_str[i].replace(letter, "1", 1)
        else:
          split_str[i] = split_str[i].replace(letter, "0", 1)
    for i in range(len(split_str)):
      split_str[i] = rev_alphabet[split_str[i]]
    return "".join(split_str)
  elif len(args) == 2:
    msg, mask = [i for i in args[0].lower() if i.isalpha() or i in ". "], list(args[1])
    for i in range(len(msg)):
      msg[i] = alphabet[msg[i]]
    msg = "".join(msg)
    j = 0
    for i in msg:
      while not mask[j].isalpha(): j += 1
      mask[j] = mask[j].upper() if int(i) else mask[j].lower()
      j += 1
    return "".join(mask)

