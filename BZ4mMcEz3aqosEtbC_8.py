
def mean(num):
    count=0
    sum=0
    num=str(num)
    for i in num:
        i=int(i)
        sum+=i
        count+=1
    return (sum//count)
print(mean(666))

