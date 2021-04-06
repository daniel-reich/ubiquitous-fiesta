
def win_round(a,b):
    a_number = ""
    a_number += str(max(a))
    a.remove(max(a))
    a_number += str(max(a))  
    b_number = ""
    b_number += str(max(b))
    b.remove(max(b))
    b_number += str(max(b)) 
    if int(a_number) > int(b_number):
        return True
    else:
        return False

