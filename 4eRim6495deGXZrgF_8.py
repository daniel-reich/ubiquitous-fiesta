
def column_chart(productA, productB, targets):
    heights = (['  '] +[str(x) for x in range(10, max(targets)+20, 10)])[::-1]
    pillars = ['|'] * len(heights) 
    c = [heights, pillars]
    a = {0: 'Mo', 1: 'Tu', 2: 'We', 3: 'Th', 4: 'Fr', 5: 'Sa', 6: 'Su'}
    for x in range(7):
        day= [a[x]] + (['++'] * (productA[x]//10)) + (['**'] * (productB[x]//10))
        day += ['  '] * (len(heights) - len(day))
        day[targets[x]//10+1] = '__'
        c.append(day[::-1])
    c = c[:] + [pillars[:]]
    return '\n'.join([' '.join(x) for x in zip(*c)])

