
#for even numbered lenth and even indexes
def valid_credit_card(number):
    a = list(str(int(number)))
    if(len(a)%2==0):
        #a = list(str(int(number)))
        #print("lenghth before pop: ",len(a))
        x = a.pop(-1)
        #a.append("x")
        #print("list: ",a)
        #print("length after pop: ",len(a))
        #print("x: ",x)
        fin = [int(a[i])*2 if(i%2==0) else int(a[i]) for i in range(len(a))]
        #print("fin:",fin)
        fin_1 = sum([(fin[i]-9) if((i%2==0) and (fin[i]>9)) else int(fin[i]) for i in range(len(a))])
        #print("fin_1:",fin_1)
        last = str(fin_1*9)
        #print("last:", last)
        if(str(last[-1]) == x):
            return True
        else:
            return False
    elif(len(a)%2==1):
        #a = list(str(int(number)))
        #print("lenghth before pop: ",len(a))
        x = a.pop(-1)
        #a.append("x")
        #print("list: ",a)
        #print("length after pop: ",len(a))
        #print("x: ",x)
        fin = [int(a[i])*2 if(i%2==1) else int(a[i]) for i in range(len(a))]
        #print("fin:",fin)
        fin_1 = sum([(fin[i]-9) if((i%2==1) and (fin[i]>9)) else int(fin[i]) for i in range(len(a))])
        #print("fin_1:",fin_1)
        last = str(fin_1*9)
        #print("last:", last)
        if(str(last[-1]) == x):
            return True
        else:
            return False
print(valid_credit_card(79927398713))

