
def even_odd_string(txt):
  E = enumerate(txt);
  ev = "".join(l for i,l in E if i%2==0)
  E = enumerate(txt);
  od = "".join(l for i,l in E if i%2==1)
  return ev + " " + od;

