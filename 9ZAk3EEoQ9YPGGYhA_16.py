
def items_purchase(store, wallet):
    
    items = []
    
    wallet = int(wallet[1:])
    
    for i in store.keys():
        
        if int(store[i][1:].replace(',','')) <= wallet:
            
            items.append(i)
            
    return sorted(items) if len(items)>0 else 'Nothing'

