
def jumping_frog (n, stones) :
    
    '''input : the number of places he has to cross & the number of stones per place
    output : if he can reach the end and if he can, the number of jumps he needs to make'''
    
    index, jumps, lost = 0, 1, False
    
    while index < n :
        try :
            while lost == False :
                index += stones[index]
                jumps += 1
                if stones[index] == 0 :
                    index -= 2*stones[index]
                    if stones[index] == 0 :
                        lost = True
                        return "no chance :-("
                    elif index < 0 :
                        index = 0
                        jumps += 1
                elif index - 2*stones[index] > 0 and stones[index - 2*stones[index]] > 5 :
                    index -= 2*stones[index]
                    if stones[index] == 0 :
                        lost = True
                        return "no chance :-("
                    elif index < 0 :
                        index = 0
                        jumps += 1
        except IndexError :
            return jumps

