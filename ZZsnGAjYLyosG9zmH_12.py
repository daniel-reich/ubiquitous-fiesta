
def flash(fc):
    var1, oper, var2 = fc
    return var1 + var2 if oper == '+' else var1 - var2 if oper == '-' else var1 * var2 if oper == 'x' else round(var1 / var2, 2) if oper == '/' and var2 else None

