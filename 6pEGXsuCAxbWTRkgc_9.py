
def loves_me(n):
  if n == 1:
    return "LOVES ME"
  wordList = []
  for i in range(1,n+1):
    if i == n:
      if i%2 == 0:
        wordList.append("LOVES ME NOT")
      else:
        wordList.append("LOVES ME")
    elif i%2 == 0:
      wordList.append("Loves me not, ")
    else:
      wordList.append("Loves me, ")
  return "".join(wordList)

