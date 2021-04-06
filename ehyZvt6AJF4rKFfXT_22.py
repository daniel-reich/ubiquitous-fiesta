
def uncensor(txt, vowels):
  output = ""
  lst = txt.split("*")
  print(lst)
  for i in range(len(vowels)):
    output += lst[i] + vowels[i]
  output += lst[-1]
  return output

