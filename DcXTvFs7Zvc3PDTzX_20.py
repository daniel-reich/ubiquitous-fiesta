
def validate_binary(b):
    return [b.count(i) for i in b][0]%2==0

