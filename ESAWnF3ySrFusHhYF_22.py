
def edit_words(lst):
  result = []
  for i in lst:
    word = ""
    if i == "": word = "-"
    for j in range(len(i)):
      if len(i) // 2 ==j:
        word += "-" 
      word += i[j]
    result.append(word[::-1].upper())
  return result

