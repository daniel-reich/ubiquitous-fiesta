
def knapsack(capacity, items):
    '''
    Returns a dictionary giving capacity, a list of chosen items from items,
    total weight and total value of selected items as per instructions
    '''
    weights = [item['weight'] for item in items]
    values = [item['value'] for item in items]  # extract weights and values
    table = [[0] * (capacity + 1) for i in range(len(items)+1)] # DP table
             
    # Populate table with effects of increasing items
    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            table[i][j] = table[i-1][j]
            if j >= weights[i-1] and table[i][j] < table[i-1][j-weights[i-1]] + values[i-1]:
                table[i][j] = table[i-1][j-weights[i-1]] + values[i-1] # include this one
​
    # Extract selected items
    n = len(table) - 1
    j = len(table[0]) - 1
    selected = {'capacity': capacity, 'items': [], 'weight': 0, 'value': table[n][-1]}
    
    while n != 0:
        if table[n][j] != table[n-1][j]:  # include this one
            selected['weight'] += weights[n-1]
            selected['items'].append(items[n-1])
            j = j - weights[n-1]
        n -= 1
​
    selected['items'].reverse()  # to reflect original order
    return selected

