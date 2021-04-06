
def possible_palindrome(txt):
 lst = len([x for x in txt if txt.count(x)%2])
 return lst==1 or lst==0 or len(set(txt))==1

