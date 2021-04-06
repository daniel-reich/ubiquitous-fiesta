
def grr(x):
    if x.islower():
        return ord(x) - 32.5
    else:
        return ord(x)
​
def sorting(s):
    numbers = "".join(sorted([num for num in s if num.isnumeric()]))
    string = "".join(sorted([i for i in s if i.isalpha()], key=grr))
    return string + numbers

