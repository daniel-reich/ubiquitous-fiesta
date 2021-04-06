
def math_expr(expr):
    try:
        return isinstance(eval(expr), (int, float))
    except NameError:
        return False

