
def guess_score(str1,str2):
# key to solving this problem is to replace the values in both 
# strings at the indices where a match is found unless 
# there is match at same index positions 
    str1=list(str1)
    str2=list(str2)
    mydict={'black':0,'white':0}    
    for i in range(len(str1)):
        for  j in range(len(str2)):
            if i==j and str1[i]==str2[j]:
                mydict['black']+=1
                str1[i]='s'
                str2[j]='q'
            elif i!=j and str1[i]==str2[j] and str1[i]!=str2[i] and str1[j]!=str2[j]:
                mydict['white']+=1
                str1[i]='s'
                str2[j]='q'
​
    return mydict

