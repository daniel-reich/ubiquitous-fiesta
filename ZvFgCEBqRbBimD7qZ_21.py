
def bowling(pins):
    i = 0
    total_score = 0
    frame = 1
    
    while frame<=10:
        
        #if its a strike
        if pins[i]==10:
            total_score = total_score+10+pins[i+1]+pins[i+2]
            frame+=1
            
        #if its a spare
        elif (pins[i] + pins[i+1])==10:
            total_score = total_score+10+pins[i+2]
            i+=1
            frame+=1
        
        elif (pins[i] + pins[i+1])<10:
            total_score = total_score+pins[i] + pins[i+1]
            i+=1
            frame+=1
            
        
        
        
        
        
        
        i+=1
    return total_score

