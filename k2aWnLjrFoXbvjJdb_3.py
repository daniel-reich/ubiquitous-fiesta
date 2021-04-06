
def vigenere(text, keyword):
  letters = [chr(i) for i in range(65,91)]
  grid = [letters[i:]+letters[:i] for i in range(0,26)]
  formatted = "".join(map(lambda x: x.upper(),filter(lambda x: x.isalpha(), text)))
  key = keyword.upper()*(len(formatted)//len(keyword))+keyword.upper()[:len(formatted)%len(keyword)]
  #if text given is ciphertext
  if formatted == text:
    return "".join(map(lambda x: grid[0][grid[letters.index(key[x])].index(formatted[x])], range(len(formatted))))
  #if text given is plaintext
  return "".join(map(lambda x: grid[letters.index(key[x])][letters.index(formatted[x])], range(len(formatted))))

