
def palindrome_descendant(num):
    num=str(num)
    even=[]
    odd=[]
    total=[]
    string=[]
    if len(num)%2!=0:
        return False
    else:
        if num==num[::-1]:
            return True
        else:
            for i in range(len(num)):
                if i%2==0:
                    even.append(int(num[i]))
                else:
                    odd.append(int(num[i]))
            for i in range(len(even)):
                total.append(even[i]+odd[i])
            for i in range(len(total)):
                string.append(str(total[i]))
            o=''.join(string)
            #print(o)
            if len(o)>1 and len(o)%2==0:
                if o==o[::-1]:
                    return True
                else:
                    return palindrome_descendant(int(o))
            else:
                return False

