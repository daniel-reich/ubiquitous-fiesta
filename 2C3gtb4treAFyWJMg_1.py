
def polybius(text):
  def code_to_char(code):
    asc = (int(code[0]) - 1) * 5 + int(code[1]) - 1 + ord('a')
    return chr(asc) if asc < ord('j') else chr(asc + 1)
​
  def char_to_code(char):
    n = ord(char) - (1 if char >= 'j' else 0) - ord('a')
    return str(n // 5 + 1) + str(n % 5 + 1)
​
  if text[0].isdigit():
    words =[]
    for code_word in text.split():
      words.append("".join(code_to_char(code_word[i:i+2]) for i in range(0, len(code_word), 2)))
    return ' '.join(words)      
  else:
    code_words = []
    for word in text.lower().replace("'", '').replace(":", '').split():
      code_words.append(''.join(char_to_code(char) for char in word))
    return ' '.join(code_words)

