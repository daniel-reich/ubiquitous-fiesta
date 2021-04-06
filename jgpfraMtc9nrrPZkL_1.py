
def switch_gravity_on(lst):
  return list(map(list,zip(*(sorted(list(i),reverse=True) for i in zip(*lst)))))

