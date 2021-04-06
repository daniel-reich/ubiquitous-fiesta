
def get_name(address):    
    name = ''    
    for i in range(address.index('@')):
        if address[i].isalpha():
            name += address[i]
    return name

