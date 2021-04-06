
from string import ascii_lowercase as a
​
def decode(txt):
    abc = a[13:-3]+a[-3:-1]+' '+a[-1]+a[:3]+a[3:13]
    x = [x for x in range(19)]
    nums = x[2:12]+x[3:6]+x[15:]+x[1:11]
    encrypt = dict(zip(abc, nums))
    res = [encrypt[x.lower()]+4 if x.isupper() else encrypt[x] for x in txt]
    return res

