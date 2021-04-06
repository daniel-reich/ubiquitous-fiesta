
def parse_list(lst):
   return [str(i) if isinstance(i, int) else i for i in lst]

