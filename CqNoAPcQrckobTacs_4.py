
def missing_letter(lst):
  ord_lst = [ord(x) for x in lst]
  to_chr = [chr(y) for y in range(min(ord_lst),max(ord_lst))]
  return [x for x in to_chr if x not in lst][0]

