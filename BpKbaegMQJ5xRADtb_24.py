
def is_unprimeable(num):
  p,num=lambda n:all(int(n)%i for i in range(2,int(n))) and int(n)>1,str(num)
  lst = [int(i) for i in sum(([num[:i] + str(x) + num[i+1:] for x in \
    range(10)] for i in range(len(num))), []) if p(i) and int(i)]
  return ("Prime Input" if p(num) else "") or sorted(lst) or "Unprimeable"

