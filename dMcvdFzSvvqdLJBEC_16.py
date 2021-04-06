
def num_of_days(cost, savings, start):
        a=cost-savings
        i,b,d=0,0,0
        while a>0:
                a=a-((i+start)*2+6)*7/2
                i+=1
        while a<0:
                a+=start+i+6-d
                d+=1
        return 7*i-d+1 if 7*i-d+1>3 else 7*i-d

