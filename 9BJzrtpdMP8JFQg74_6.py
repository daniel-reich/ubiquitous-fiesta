
def twins(lst):
  front,back = [lst[0]],lst[1:]
  while sum(front)!=sum(back):
    front.append(back[0])
    back=back[1:]
  return max(len(front),len(back))

