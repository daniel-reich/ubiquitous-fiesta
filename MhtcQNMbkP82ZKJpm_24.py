
def get_notes_distribution(s):
        vn=[1,2,3,4,5]
        n={5:0,4:0,3:0,2:0,1:0}
        for i in range(0,len(s)):
                for j in s[i]['notes']:
                        if j in vn:
                                n[j]=n[j]+1
        for k in range(1,6):
                if n[k]==0:
                        del n[k]
        return n

