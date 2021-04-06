
def get_drink_ID(flavor, ml):
    
    return ''.join(item[:3].upper() for item in flavor.split())+''.join(item for item in ml if item.isdigit())

