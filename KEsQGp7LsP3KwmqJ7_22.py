
def check(lst):
    a=sorted(lst)
    if lst==a:
        return 'NO'
    else:
        x=a[1:]+a[:1]
        y=a[2:]+a[:2]
        z=a[3:]+a[:3]
        return 'YES' if lst==x or lst==y or lst==z else 'NO'

