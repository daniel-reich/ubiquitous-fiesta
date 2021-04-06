
def win_round(you, opp):
    res = []
  
    for item in [you, opp]:
        first = max(item)
        item.remove(first)
        second = max(item)
        res.append(int(str(first) + str(second)))
        
    you_score, opp_score = res
    if you_score > opp_score:
        return True
    
    return False

