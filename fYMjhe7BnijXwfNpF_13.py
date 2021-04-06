
def stmid(string):
  string = string.split()
  answer = ""
  for word in string:
    if len(word)%2 == 0:
      answer += word[0]
    else:
      answer += word[len(word)//2]
  return answer

