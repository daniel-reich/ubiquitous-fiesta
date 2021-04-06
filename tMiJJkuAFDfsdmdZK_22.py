
def to_snake_case(txt):
    ans = ''
    for x in txt:
        if x.isupper():
            ans += '_' + x.lower()
        else:
            ans += x
    return ans
  
​
def to_camel_case(txt):
    low = txt.split('_')
    return ''.join([w if i==0 else w.capitalize() for i, w in enumerate(low)])

