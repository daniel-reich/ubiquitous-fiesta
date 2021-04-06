
import statistics
def greatest_impact(lst):
    msg=('Nothing','Weather','Meals','Sleep')
    s=[[lst[i][j] for i in range(len(lst))] for j in range(len(lst[0]))]
    sd=[statistics.stdev(g) for g in s[1:]]
    return msg[sd.index(max(sd))+1*(max(sd)!=0)]

