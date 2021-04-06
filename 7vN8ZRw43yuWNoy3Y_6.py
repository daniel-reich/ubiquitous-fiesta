
def parse_code(txt):
    return dict(zip(['first_name', 'last_name', 'id'], txt.replace('0', ' ').split()))

