
def add_letters(a):
  if a==[]:
    return 'z'
  let = sum(ord(i)-96 for i in a)
  while let>26:
    let-=26
  return chr(let+96)

