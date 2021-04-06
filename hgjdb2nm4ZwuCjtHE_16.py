
def math_expr(expr):
    for i in list(expr):
        if i.isalpha():
            return False
    else:
        return True

