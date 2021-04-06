
def lambda_to_def(code):
    name, left = code.split(' = ')
    left, body = left.split(': ')
    args = left[7:]
    return 'def {}({}):\n\treturn {}'.format(name, args, body)

