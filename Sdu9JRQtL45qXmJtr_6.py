
def to_base(n, b):
  BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
  return "0" if not n else to_base(n//b, b).lstrip("0") + BS[n%b]
def happy_birthday(age):
  for i in range(2,100):
    a=to_base(age,i)
    if a=='20' or a=='21':
      return "Mubashir is just {}, in base {}!".format(str(a),str(i))

