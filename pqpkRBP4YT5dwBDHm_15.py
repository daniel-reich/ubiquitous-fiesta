
def show_the_love(lst):
  shared = [x * 0.75 if x != min(lst) else x + sum(x * 0.25 for x in lst if x != min(lst)) for x in lst]
  return [int(x) if str(x)[-1] == '0' else x for x in shared]

