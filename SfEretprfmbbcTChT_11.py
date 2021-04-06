
def reverse_words(words):
  list = words.split()
  ans = ""
  for item in list[::-1]:
    ans = ans + item + " "
  return ans.strip()

