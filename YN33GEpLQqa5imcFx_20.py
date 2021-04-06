
def pascals_triangle(row):
    if(row==1):
        return "1 1"
    else:
        i=1
        lst=[1,1]
        while(i<row):
            lst2=[]
            for i in range(0,len(lst)):
                if(i!=len(lst)-1):
                    lst2.append(lst[i]+lst[i+1])
            lst=[1]+lst2+[1]
            i+=1
        result=""
        for i in range(0,len(lst)):
            if(i!=len(lst)-1):
                result+=str(lst[i])+" "
            else:
                result+=str(lst[i])
        return result

