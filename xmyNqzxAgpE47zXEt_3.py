
def is_alphabetically_sorted(sentence):
    a = sentence.split()
    for item in a:
        if len(item)>=3:
            if item.isalpha() == False:
                
                if item[0:-1] == ''.join(sorted(item[0:-1])):
                    return True
                else:
                    pass
            
            elif item == ''.join(sorted(item)):
                return True
        else:
            pass
    return False

