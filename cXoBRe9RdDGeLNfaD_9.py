
def eight_bit(exp):
  b = lambda x: "1{:0>7}".format(bin(x+128)[2:]) if x<0 else bin(x)[2:]
  x,y,z = exp.split(); x,z,e = int(x),int(z),eval(exp)
  return (e,"%s %s %s = %s"%(b(x),y,b(z),b(e))) if all(-129<n<128 
    for n in [x,z,e]) else "Overflow"

