
import re
​
def lambda_to_def(code):
    arr = re.split('( = lambda )|(: )', code)
    return 'def {}({}):\n\treturn {}'.format(arr[0], arr[3], arr[6])

