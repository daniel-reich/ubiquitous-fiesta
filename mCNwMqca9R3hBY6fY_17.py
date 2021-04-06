
import re
 
​
def make_happy(string):
​
    SmileyRegex = re.compile(r'([:|8|x|;])([)|()])')
    MatchObject = SmileyRegex.search(string)
    
    if MatchObject == None:
        pass
    
    elif MatchObject.group(2) == '(':
        changed = SmileyRegex.sub(r'\1)', string)
        return changed
        
    elif MatchObject.group(2) == ')':
        changed = SmileyRegex.sub(r'\1(', string)
        return changed
        
    return string

