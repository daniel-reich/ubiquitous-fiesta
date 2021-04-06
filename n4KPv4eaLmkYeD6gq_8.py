
face_interval = lambda l: ':' + ('/' if not isinstance(l, list) 
    else ')' if max(l) - min(l) in l 
    else '(')

