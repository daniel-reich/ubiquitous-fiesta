
def max_ham(s1, s2):
    s1list = list(s1)
    s2list = list(s2)
    
    hamming_distance = 0
    for i in range(len(s1list)):
        if s1list[i] != s2list[i]:
            hamming_distance += 1
        else: pass     
    
    for letter in s1:
        if letter in s2list: 
            pass
            s2list.remove(letter)
        else: return False
    if s2list == [] and len(s1)-hamming_distance <1 :
        return True
    elif s2list == []:
        return hamming_distance
    else: return False

