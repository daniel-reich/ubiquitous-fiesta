
def odds_vs_evens(num):
 return 'even' if sum([int(i) for i in str(num) if int(i)%2==0])>sum([int(i) for i in str(num) if int(i)%2==1]) else 'odd' if sum([int(i) for i in str(num) if int(i)%2==0])<sum([int(i) for i in str(num) if int(i)%2==1]) else 'equal'

