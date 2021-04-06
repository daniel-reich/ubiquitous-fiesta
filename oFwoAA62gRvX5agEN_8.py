
def knapsack(capacity, items):
    result = []
    def helper(capacity,items,lst=[],weight=0,val=0):
        if weight <= capacity:
            result.append([lst,val])
        for i in range(len(items)):
            helper(capacity,items[i+1:],lst+[items[i]],weight+items[i]['weight'],val+items[i]['value'])
​
    helper(capacity,items)
    result = max(result,key=lambda x:x[1])
    return{'capacity':capacity,'items':result[0],'weight':sum(i['weight'] for i in result[0]),'value':result[1]}

