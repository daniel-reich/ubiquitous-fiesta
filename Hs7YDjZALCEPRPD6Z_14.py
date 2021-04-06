
def count_uppercase(lst):
    b=[]
    count=0
    for i in lst:
        for x in i:
            if x.isupper():
                count=count+1
    return (count)

