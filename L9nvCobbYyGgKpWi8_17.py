
def to_list(num):
 return [int(i) for i in str(num)]
  
​
def to_number(lst):
 return int(''.join(list(map(str,lst))))

