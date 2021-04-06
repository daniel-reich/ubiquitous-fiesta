
def sorting(s):
  sorted_letters  =  sorted([e for e in s if e.isalpha()] ,key = lambda e : (e.lower() , -ord(e)) )
  sorted_nums  =  sorted([e for e in s if e.isdigit()]);
  return "".join(sorted_letters + sorted_nums);

