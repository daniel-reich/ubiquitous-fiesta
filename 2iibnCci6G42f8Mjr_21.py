
def guess_score(code,guess):
    
    black, white, matching_index  = 0, 0, []
    for c in range(len(code)):
        for g in range(len(guess)):
            if code[c] == guess[g]:
                if c == g:
                    matching_index.append(c)
                    black += 1
​
    matching_index.reverse()
​
    if not matching_index == [] :                
        for i in matching_index:
            code = code[:i]+ code[i+1:]
            guess = guess[:i]+ guess[i+1:]
    
    for num in code:
        if num in set(guess):
            white += 1
            
    return {"black":black,"white":white}

