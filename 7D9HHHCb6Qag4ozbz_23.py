
def find_zip(txt):
    
    n = [x.find('zip') for x in txt.split()]
   
    if n.count(0) > 1:
        return txt.rfind('zip')
        
    else:
        return -1

