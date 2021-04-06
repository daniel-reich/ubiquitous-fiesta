
def validate_relationships(txt):
    return eval(txt.replace('=', '==').replace('<==', '<=').replace('>==', '>='))

