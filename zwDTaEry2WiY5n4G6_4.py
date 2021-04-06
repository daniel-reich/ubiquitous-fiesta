
def digital_vowel_ban(n, ban):
  
  a= []
  b = list(str(n))
  
  for i in range(len(str(n))):
    b[i] = b[i].replace("1", "one")
    b[i] = b[i].replace("2", "two")
    b[i] = b[i].replace("3", "three")
    b[i] = b[i].replace("4", "four")
    b[i] = b[i].replace("5", "five")
    b[i] = b[i].replace("6", "six")
    b[i] = b[i].replace("7", "seven")
    b[i] = b[i].replace("8", "eight")
    b[i] = b[i].replace("9", "nine")
    b[i] = b[i].replace("0", "zero")
    
  for i in range(len(str(n))):
    if not ban in b[i]:
      a.append(b[i])
​
  for i in range(len(a)):
    a[i] = a[i].replace("one", "1")
    a[i] = a[i].replace("two", "2")
    a[i] = a[i].replace("three", "3")
    a[i] = a[i].replace("four", "4")
    a[i] = a[i].replace("five", "5")
    a[i] = a[i].replace("six", "6")
    a[i] = a[i].replace("seven", "7")
    a[i] = a[i].replace("eight", "8")
    a[i] = a[i].replace("nine", "9")
    a[i] = a[i].replace("zero", "0")
​
  c = ''.join(str(i) for i in a)
  
  if a == []:
    return "Banned Number"
  else:
    return int(c)

