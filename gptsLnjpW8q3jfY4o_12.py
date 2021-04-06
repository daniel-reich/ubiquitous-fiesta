
def Formula(n):
    if(n < 0):
        if(n == -1):
            return "1/(a+b)"
        elif(n == -2):
            return "1/(a^2+2ab+b^2)"
        else:
            num = [1]
            y = [0]
            for x in range(max(abs(n),0)):
                num= [l+r for l,r in zip(num+y, y+num)]
                #print(num)
            series_a = ["a^{}".format(abs(n)-i) for i in range(abs(n)+1)]
            #print(series_a)
            series_b = ["b^{}".format(i) for i in range(abs(n)+1)]
            #print(series_b)
            pattern = [i+j for i,j in zip(series_a,series_b)]
            #print(pattern)
            expansion = [str(i)+j for i,j in zip(num,pattern)]
            #print(expansion)
            final_output = [i.replace("a^0",'') if('a^0' in i) else i.replace("b^0",'') if('b^0' in i) else i.replace(i,i) for i in expansion]
            final_output[1] = final_output[1].replace("b^1",'b')
            final_output[-2] = final_output[-2].replace("a^1",'a')
        #print(final_output)
        #removing 1 at the start
        final_output[0] = "a^{}".format(abs(n))
        final_output[-1] = "b^{}".format(abs(n))
        #last = "+".join(final_output)
        return "1/({})".format("+".join(final_output))
    elif(n>=0):
        if(n == 0):
            return "1"
        elif(n == 1):
            return "a+b"
        elif(n == 2):
            return "a^2+2ab+b^2"
        else:
            num = [1]
            y = [0]
            for x in range(max(n,0)):
                num= [l+r for l,r in zip(num+y, y+num)]
            #print(num)
            series_a = ["a^{}".format(n-i) for i in range(n+1)]
            #print(series_a)
            series_b = ["b^{}".format(i) for i in range(n+1)]
            #print(series_b)
            pattern = [i+j for i,j in zip(series_a,series_b)]
            #print(pattern)
            expansion = [str(i)+j for i,j in zip(num,pattern)]
            #print(expansion)
            final_output = [i.replace("a^0",'') if('a^0' in i) else i.replace("b^0",'') if('b^0' in i)  else i.replace(i,i) for i in expansion]
            
            
            final_output[1] = final_output[1].replace("b^1",'b')
            final_output[-2] = final_output[-2].replace("a^1",'a')
        #print(final_output)
        #removing 1 at the start
        final_output[0] = "a^{}".format(n)
        final_output[-1] = "b^{}".format(n)
        return "+".join(final_output)
​
        
#print(Formula(int(input("Enter a number: "))))

