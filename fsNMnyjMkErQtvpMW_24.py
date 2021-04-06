
def holey_sort(lst):
  hole_dict = {'0':1, '1':0, '2':0, '3':0, '4':1, '5':0, '6':1, '7':0, '8':2, '9':1}
  digit_holes = [[hole_dict[digit] for digit in str(num)] for num in lst]
  sort_lst = [sum(d) for d in digit_holes]
  lst_ = sorted(zip(lst, sort_lst), key = lambda x: x[1])
  return [l[0] for l in lst_]

