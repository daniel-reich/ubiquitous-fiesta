
def briscola_score(my_deck1, my_deck2):
    x=my_deck1
    y=my_deck2
    x=[d.replace('2', '0') for d in x]
    x=[d.replace('4', '0') for d in x]
    x=[d.replace('5', '0') for d in x]
    x=[d.replace('6', '0') for d in x]
    x=[d.replace('7', '0') for d in x]
    y=[d.replace('2', '0') for d in y]
    y=[d.replace('4', '0') for d in y]
    y=[d.replace('5', '0') for d in y]
    y=[d.replace('6', '0') for d in y]
    y=[d.replace('7', '0') for d in y]
    z=[]
    c=[]
    for i in range (len(x)):
        z.append(x[i][0])
    z=[d.replace('3', '10') for d in z]
    z=[d.replace('A', '11') for d in z]
    z=[d.replace('K', '4') for d in z]
    z=[d.replace('Q', '3') for d in z]
    z=[d.replace('J', '2') for d in z]
    
    sum=0
    for i in z:
        sum=sum+int(i)
    for h in range (len(y)):
        c.append(y[h][0])
    c=[d.replace('3', '10') for d in c]
    c=[d.replace('A', '11') for d in c]
    c=[d.replace('K', '4') for d in c]
    c=[d.replace('Q', '3') for d in c]
    c=[d.replace('J', '2') for d in c]
    sum1=0
    for d in c:
        sum1=sum1+int(d)
    final_sum=sum+sum1
    if final_sum>120:
        return("You Win!")
    elif final_sum<120:
        return("You Lose!")
    elif final_sum==120:
        return("Draw!")

