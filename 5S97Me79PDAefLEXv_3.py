
def lambda_to_def(code):
    fname = code.split('=')[0].strip()
    idx = code.find('lambda')
    code = code[idx+6:]
    idx = code.find(':')
    params, code = code[:idx], code[idx+1:]
    ans = 'def ' + fname + '(' + params.strip() + '):\n\treturn ' + code.strip()
    return ans

