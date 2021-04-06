
def grab_number_sum(s):
    import re
    return sum(map(int,re.findall(r'\d+', s)))
​
    #solution 2
    #from string import ascii_letters as letters
    #nums= ''.join([" " if l in letters else l for l in s]).split()
    #return sum(map(int,nums))

