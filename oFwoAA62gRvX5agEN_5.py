
from itertools import compress
def knapsack(capacity, items):
    if capacity>0 and len(items)>0:
        choice=[False]*len(items)
        def knapsack_recursion(item_index,rem_capacity):           
            wt=items[item_index]['weight']
            v=items[item_index]['value']
            if item_index==(len(items)-1):
                if wt<=rem_capacity:
                    choice[item_index]=True
                    return v
                else:
                    choice[item_index]=False
                    return 0
            elif wt<=rem_capacity:
                if v+knapsack_recursion(item_index+1,rem_capacity-wt)>=knapsack_recursion(item_index+1,rem_capacity):
                    choice[item_index]=True
                    return v+knapsack_recursion(item_index+1,rem_capacity-wt)
                else:
                    choice[item_index]=False
                    return knapsack_recursion(item_index+1,rem_capacity)
            else:
                choice[item_index]=False
                return knapsack_recursion(item_index+1,rem_capacity)
        val=knapsack_recursion(0,capacity)
        chosen_items=list(compress(items,choice))
        return {'capacity':capacity,'items':chosen_items,'weight':sum([i['weight'] for i in chosen_items]),'value':val}
    else:
        return {'capacity':0,'items':[],'weight':0,'value':0}

