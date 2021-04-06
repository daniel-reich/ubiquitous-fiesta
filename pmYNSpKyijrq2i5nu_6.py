
#
# [3, 6, 8, 11, 15, 19, 22], 3, 35), ["8-8-19"]
#
def darts_solver (sections, darts, target) :  
    solutions = set() # solution set
    add_dart(sections, darts, [], target, solutions)
    solutions.remove(None)
    return list(solutions)
            
# spin through the possible throws and determine if a solution is found
def add_dart(sections, darts, throws, target, solutions) :
    
    count = len(throws)
    
    # if this is too many darts, we have failed.
    if count > darts :
        return "None"
    
    #increment the throw count
    count += 1
    
    for t in sections :
        throws.append(t)
​
        # we found a solution
        if (sum(throws) == target and count == darts) :
            solutions.add(throw_solution(throws))
​
            # if we still have more throws call add_dart again
        elif count < darts :
            pot_sol = add_dart(sections, darts, throws, target, solutions) 
            if (pot_sol != 'None') :
                solutions.add(pot_sol)
        
        # if we made it this far, we haven't found a solution
        throws.pop()
    
   
def throw_solution(throws) :
    """
    Input:
        list of dart throws
        
    Return:
        Formatted string of throws separated by dashes
            ex: 3-8-25
    """
    throws.sort()
    sol = str(throws[0])
    for s in throws[1:-1] :
        sol += "-" + str(s)
    
    sol +=  "-" + str(throws[-1])
    
    return sol

