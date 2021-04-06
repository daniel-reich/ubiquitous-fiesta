
def multiply_nums(nums):
    t=1
    l=nums.split(",")
    for i in l:
        t*=int(i)
    return t    
print(multiply_nums("2,3"))

