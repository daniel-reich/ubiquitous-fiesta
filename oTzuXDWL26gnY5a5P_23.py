
def prime_numbers(num):
 list1= [j for j in range(2,num) for i in range(1,j) if j%i==0]
 return len([k for k in list1 if list1.count(k)==1])

