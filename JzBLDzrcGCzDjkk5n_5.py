
def encrypt(word):
  new_txt=''
  for i in word[::-1]:
    if i=='a': new_txt+='0'
    elif i=='e': new_txt+='1'
    elif i=='o': new_txt+='2'
    elif i=='u': new_txt+='3'
    else: new_txt+=i
  new_txt+='aca'
  return new_txt

