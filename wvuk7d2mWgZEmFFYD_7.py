
def shared_letters(a, b):
    count=0
    for i in set(a):
       if i in b:
           count=count+b.count(i)
    return count

