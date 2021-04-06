
def bar_chart(results):
    l = list(results.keys())
    l.sort(key=lambda x:results[x])
    l.reverse()
    d = {}
    for k in l:
        if(d.get(results[k]) == None):
            d[results[k]] = []
        ll = d[results[k]]
        ll.append(k)
        ll.sort()
        d[results[k]] = ll
    
    #print(l)
    #print(d)
    la = list(d.keys())
    la.sort()
    la.reverse()
    #print('LA',la)
    s = ''
    for k in la:
        for key in d[k]:
            #print(key, results[key])
            if(results[key] == 0):
                s = s + key + '|' + '0' + '\n'
            else:
                s = (s + key + '|' + '#'*int(results[key] / 50) +
                    ' ' + str(results[key]) + '\n')
    s = s.strip()
    return s

