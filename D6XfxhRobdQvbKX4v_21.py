
def first_before_second(s, first, second):
    
    first_indexes = []
    second_indexes = []
    
    for i in range (len(s)):
        if s[i]==first:
            first_indexes.append(i)
​
        if s[i] == second:
            second_indexes.append(i)
​
​
​
    if max(first_indexes)<min(second_indexes):
        return True
    
    else:
        return False

