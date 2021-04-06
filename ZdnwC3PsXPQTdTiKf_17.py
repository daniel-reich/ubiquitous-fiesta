
def calculator(num_1: int, operator: str, num_2: int) -> int:
    if num_2 == 0 and operator == "/":
        return"Can't divide by 0!"
    funcs = {
        "+": int.__add__,
        "-": int.__sub__,
        "*": int.__mul__,
        "/": int.__floordiv__
    }
    return funcs[operator](num_1, num_2)

