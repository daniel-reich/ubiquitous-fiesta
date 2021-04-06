
def who_won(a):
        for i in range(0,3):
                if (len(set(a[i]))==1) or (a[0][i]==a[1][i]==a[2][i]):
                        return a[i][i]
        if (a[0][0]==a[1][1]==a[2][2]) or (a[2][0]==a[1][1]==a[0][2]):
                        return a[1][1]

