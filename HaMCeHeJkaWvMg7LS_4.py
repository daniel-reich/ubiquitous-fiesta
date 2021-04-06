
def sun_loungers(beach):
    
    beach = [x for x in beach]
    
    chairs = 0
    i = 0
    while i < len(beach):
        if beach[i] == '0':
            if i == 0:
                try:
                    if beach[i+1] == '0':
                        chairs += 1
                        beach[i] = '1'
                        i += 1
                    else:
                        i += 1
                except: 
                    chairs += 1
                    i += 1
                
            elif i == len(beach) - 1:
                if beach[i - 1] == '0':
                    chairs += 1
                    i += 1
                else:
                    i += 1
            else:
                if beach[i-1] == '0' and beach[i+1] == '0':
                    chairs += 1
                    beach[i] = '1'
                    i += 1
​
                else:
                    i += 1
        else: 
            i += 1
    return chairs

