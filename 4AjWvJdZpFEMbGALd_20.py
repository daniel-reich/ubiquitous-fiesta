
def who_goes_free(n, k):
    Prisoners = list (range(n))
    shooting= True
    shoot_start = k-1
    quing = len(Prisoners)
    lst_temp=[]
    
    while shooting:
        for execute in range(shoot_start, quing , k):
            Prisoners[execute] = "--"
        lst_temp=[]
        
        for shot in range(quing):
            if Prisoners[shot] != "--":
                lst_temp.append(Prisoners[shot])
        Prisoners = lst_temp.copy()
        
        Tail = quing - execute -1
        quing = len(Prisoners)
        shoot_start = (k - Tail -1) % quing
        
        if quing == 1:
            shooting = False
    
    return Prisoners[0]

