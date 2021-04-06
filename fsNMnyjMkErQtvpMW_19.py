
def holey_sort(lst):
 return sorted(lst, key=lambda x: sum([1 if y in '0469' else 2 if y=='8' else 0 for y in str(x)]))

