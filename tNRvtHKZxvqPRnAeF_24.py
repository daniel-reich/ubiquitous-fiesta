
def digit_occurrences(start, end, digit):
    s =''
    for i in range(start,end+1):
          s+=str(abs(i))
    s = list(map(lambda x:int(x),list(s)))
    return s.count(digit)

