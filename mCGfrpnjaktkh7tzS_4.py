
def is_it_true(relation):
    if '=' in relation:
        relation = relation.replace('=', '==')
        if eval(relation) == True:
            return True
        else:
            return False
    elif eval(relation) == True:
        return True
    else:
        return False

