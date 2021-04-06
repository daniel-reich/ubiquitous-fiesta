
def eng2nums(s):
    ans=''
    nums=[('zero'),('one'),('two','twenty'),('three','thirty'),('four','forty'),\
          ('five','fifty'),('six','sixty'),('seven','seventy'),('eight','eighty'),\
          ('nine','ninety'),('ten'),('eleven'),('twelve'),('thirteen'),('fourteen'),\
          ('fifteen'),('sixteen'),('seventeen'),('eighteen'),('nineteen')]
    sl=s.split()
    for i in sl:
        for j in range(len(nums)):
            if i in nums[j]:
                ans+=str(j)
                break
    if s[-2:]=='ty':
        ans+='0'
    elif 'hundred' in s:
        ans=ans[0]+'0'*abs(len(ans)-3)+ans[1:]
    return int(ans)

