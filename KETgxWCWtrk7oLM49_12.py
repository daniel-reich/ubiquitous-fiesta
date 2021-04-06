
def tournament_scores(x):
    tt = []
    teams = []
    for i in x:
        j = i.split()
        j.remove('-')
        tt.append(j)    
        teams.append(j[0])   
        teams = sorted(set(teams))
​
    for i in teams:    
        j = [0,0,0]
        a = list(i)
        m = a + j    
        teams[teams.index(i)] = m
​
    for i in range(len(tt)):
        if tt[i][1]>tt[i][2]:
            for k in range(len(teams)):
                if tt[i][0] == teams[k][0]:
                    teams[k][1] += 3
                    teams[k][2] += int(tt[i][1])
                    teams[k][3] += int(tt[i][2])
                
                if tt[i][3] == teams[k][0]:
                    teams[k][2] += int(tt[i][2])
                    teams[k][3] += int(tt[i][1]) 
                   
        elif tt[i][1]<tt[i][2]:
            for k in range(len(teams)):
                if tt[i][0] == teams[k][0]:
                    teams[k][2] += int(tt[i][1])
                    teams[k][3] += int(tt[i][2])
               
                if tt[i][3] == teams[k][0]:
                    teams[k][1] += 3
                    teams[k][2] += int(tt[i][2])
                    teams[k][3] += int(tt[i][1]) 
        else:        
            for k in range(len(teams)):
                if tt[i][0] == teams[k][0]:
                    teams[k][1] += 1
                    teams[k][2] += int(tt[i][1])
                    teams[k][3] += int(tt[i][2])
              
                if tt[i][3] == teams[k][0]:
                    teams[k][1] += 1
                    teams[k][2] += int(tt[i][2])
                    teams[k][3] += int(tt[i][1]) 
​
    for i in teams:
        i[3] = i[2]-i[3] 
​
    return(sorted(teams,key=lambda x : [x[1],x[2],x[3]],reverse =True))

