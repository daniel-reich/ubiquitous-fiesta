
def bar_chart(results):
​
    a = list(sorted(sorted(results), key =results.get, reverse=True))
    b = list(sorted(results.values(), reverse=True))    
    c= []
    for i in range(len(a)):
        if b[i] == 0:
            c.append(a[i]+"|"+"#"*(int(b[i]/50))+ str(b[i]))
        else:    
            c.append(a[i]+"|"+"#"*(int(b[i]/50))+" "+ str(b[i]))
    return ("\n".join(c))

