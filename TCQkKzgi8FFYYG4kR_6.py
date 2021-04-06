
def camel_to_snake(txt):
    '''
    Converts txt from camelCase to underscore format.
    '''
    import re
​
    converter = lambda x: x.group(1) + '_' + x.group(2).lower()
​
    return re.sub(r'([a-z0-9])([A-Z])', converter, txt)

