
def free_throws(success, rows):
    success = int(success.strip('%')) *.01
    result = success
    while rows >1:
        result *= success
        rows -= 1
        
    result = round(result *100)
    
    return str(result)+'%'

