
def knapsack(max_weight, items):   
    sorted_items = sorted(items, key = lambda item: item['value'], reverse = True)
    pruned_items = [item for item in sorted_items if item['weight'] <= max_weight]
    best_result = {
          'capacity': max_weight,
          'items': [],
          'weight': 0,
          'value': 0
    } 
    while pruned_items:
        item = pruned_items.pop()
        sub_results = knapsack(max_weight - item['weight'], pruned_items)
        sub_results['items'].append(item)
        sub_results['weight'] += item['weight']
        sub_results['value'] += item['value']
        sub_results['capacity'] = max_weight
        if sub_results['value'] > best_result['value']:
            best_result = sub_results
    #order matters to edabit
    best_result['items'] = sorted(best_result['items'], key = lambda item: items.index(item))
    return best_result

