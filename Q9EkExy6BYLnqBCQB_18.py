
def wrap_around(st,n):
    st1=""
    if n >= 0:
        if n < len(st):
            st1+=st[n: ]+st[ :n]
        else:
            n= n%len(st)
            st1+=st[n: ]+st[ :n]
    else:
        if n > -(len(st)):
            st1+=st[n: ]+st[ :n]
        else:
            n = n%len(st)
            st1+=st[n: ]+st[ :n]
    return st1
print(wrap_around("Hello, World!", 2))
print(wrap_around("From what I gathered", -4))
print(wrap_around("Excelsior", 30))
print(wrap_around("Nonscience", -116))

