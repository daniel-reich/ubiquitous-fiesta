
def replace_vowel(word):
  ans=""
  for i in word:
    if i == "a":
      ans+="1"
    elif i == "e":
      ans+="2"
    elif i == "i":
      ans+="3"
    elif i == "o":
      ans+="4"
    elif i == "u":
      ans+="5"
    else:
      ans+=i
  return ans

