
def kix_code(addr):
  new=addr.split(",")
  new2=new[2].split(" ")
  new3=new[1].split(" ")
  if new3[len(new3)-1].isalpha():
    new4=" ".join(new3[len(new3)-2:])
  else:
    new4="".join(new3[-1])
  result=""
  result+=new2[1]
  result+=new2[2]
  for letter in new4:
    if letter.isdigit():
      result+=letter
    elif letter.isalpha():
      result+=letter.upper()
    else:
      result+="X"
  return result

