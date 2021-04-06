
maxvalue=0
maxtake={}
​
def knapsack(capacity, items):
  global maxvalue
  global maxtake
  maxvalue=0
  maxtake={}
​
  
  def test(take,weight,value):
    global maxvalue
    global maxtake
  # weight=sum([items[t]['weight'] for t in take])
  # value=sum([items[t]['value'] for t in take])
    if weight<=capacity and maxvalue<value:
      maxvalue=value
      maxtake=take
    if weight<=capacity:
      for i in range(max(take+[0]),len(items)):
        if i not in take :
          test(take+ [i], weight+ items[i]['weight'] , value+ items[i]['value']  )
  
  test([],0,0)
​
  print(maxtake)
  itemsout=[items[t] for t in maxtake]
  print(itemsout)
  #itemsout=[]
  out={'capacity':capacity,'items':itemsout,'weight':sum([items[t]['weight'] for t in maxtake]),'value':sum([items[t]['value'] for t in maxtake])}
  return(out)

