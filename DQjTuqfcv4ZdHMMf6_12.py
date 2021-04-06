
def kaprekar(num):
  c = 0
  while num!=6174:
    if num<1000:  num = int(str(num)+('0'*(4-len(str(num)))))
    des = int(''.join(str(x) for x in sorted([int(i) for i in str(num)], reverse=True)))
    asc = int(''.join(str(x) for x in sorted([int(i) for i in str(num)])))
    num = des-asc
    c+=1
  return c

