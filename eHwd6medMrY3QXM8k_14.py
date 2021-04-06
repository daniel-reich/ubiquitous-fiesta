
def is_consecutive(s):
  for i in range(2, len(s)):
    lst = split_string(s, i)
    print(lst)
    print("range: " + str(list(range(lst[0], lst[0] + len(lst)))))
    if list(range(lst[0], lst[0] + len(lst))) == lst or list(range(lst[0], lst[0] - len(lst),  -1)) == lst:
        return True
        
  return False
  
def split_string(txt, amount):
  step = int(len(txt)/amount)
  results = []
  for i in range(amount + 2):
    try:
      results.append(int(txt[i*step:(i+1)*step]))
    except ValueError:
      pass
  return results

