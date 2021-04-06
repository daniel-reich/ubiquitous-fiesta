
def min_removals(txt1, txt2):
        count = 0
        for ch in txt1:
            if ch not in txt2:
                count+=1
        for ch in txt2:
            if ch not in txt1:
                count+=1
                
        return(count)

