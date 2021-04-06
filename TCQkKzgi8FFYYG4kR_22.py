
def camel_to_snake(s):
    return ' '.join([f(w) for w in s.split()])
​
def f(w):
    ans = ''
    for x in w:
        if x.islower() or not x.isalpha():
            ans += x
        else:
            ans += '_' + x.lower()
    return ans

