
def majority_vote(lst):
   
   cnt = 0
   lenLst = len(lst)
   temp = 0
   val = None
   for cnt  in range(lenLst):
       n =  majority_vote_helper(lst, cnt) 
       if n > lenLst/2:
            if n > temp:
               temp = n
               val = lst[cnt]
       cnt = cnt + 1
   return val   
        
def majority_vote_helper(lst, p):
    cnt = 0
    for x in lst:
        if x == lst[p]:
             cnt = cnt+1
        else:
           cnt = cnt
    return cnt
majority_vote(["A", "A", "A", "B", "C", "A"])

