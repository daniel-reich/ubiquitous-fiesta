
def digital_vowel_ban(n, ban):
  dic = {'0': "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"}
  s = str(n)
  res = "".join(l for l in s if ban not in dic[l])
  if res == "": return "Banned Number"
  else: return int(res)

