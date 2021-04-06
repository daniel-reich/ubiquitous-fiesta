
def calculate(num1, num2, operator):
    if operator == "+":
        return num1+ num2
    if operator == "-":
        return num1- num2
    if operator == "*":
        return num1* num2
    if operator == "//":
        return num1// num2
    if operator == "%":
        return num1% num2
    if operator == "/":
        return num1/ num2
print(calculate(4, 9, "+"))
print(calculate(12, 5, "-"))
print(calculate(6, 3, "*"))
print(calculate(25, 5, "//"))
print(calculate(14, 3, "%"))
print(calculate(7, 2, "/"))

