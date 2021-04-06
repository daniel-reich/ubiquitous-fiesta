
def bill_split(spicy, cost):
 you=[]
 friend=[]
 output=[]
 for i in range(0,len(spicy)):
  if spicy[i] == "S":
   you.append(cost[i])
  else:
   you.append(cost[i]/2)
   friend.append(cost[i]/2)
 #print(you)
 #print(friend)
 you_pay=0
 for k in range(0,len(you)):
  you_pay+=you[k]
 output.append(int(you_pay))
 friend_pay=0
 for n in range(0,len(friend)):
  friend_pay+=friend[n]
 output.append(int(friend_pay))
 return output

