
def dial(number):
  newnumber = ""
  for letter in number.lower():
    if 'a'== letter or 'b' == letter or 'c' == letter:
      newnumber += "2"
    elif 'd'== letter or 'e' == letter or 'f' == letter:
      newnumber += "3"
    elif 'g'== letter or 'h' == letter or 'i' == letter:
      newnumber += "4"
    elif 'j'== letter or 'k' == letter or 'l' == letter:
      newnumber += "5"
    elif 'm'== letter or 'n' == letter or 'o' == letter:
      newnumber += "6"
    elif 'p'== letter or 'q' == letter or 'r' == letter or 's'== letter:
      newnumber += "7"
    elif 't' == letter or 'u' == letter or 'v'== letter :
      newnumber += "8"
    elif 'w' == letter or 'x' == letter or 'y' == letter or 'z' == letter:
      newnumber += "9"
    else:
      newnumber += letter
  return newnumber

