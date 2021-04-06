
def jumping_frog(stones,lst):
    i,jumps=0,[]
    while i<(stones):
        if i == stones:break
        elif lst[i]==0:return ("no chance :-(")
        if i not in jumps:jumps.append(i)
        if (i<stones-2):
         if lst[i-1]>lst[i] and lst[i-1]>lst[i+1]:
            jumps.append(i - 1)
            i=i-1
            continue
         if i>=stones:
                jumps.append(i)
                break
        i = i + lst[i]
    return len(jumps)+1

