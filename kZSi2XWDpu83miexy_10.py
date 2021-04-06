
def post_fix(astr):
    number_stack = []
    astr = astr.split(' ')
    operators = '+-/*'
    curr_operator = ''
    for eachpart in astr:
        if is_integer(eachpart):
            number_stack.append(int(eachpart))
        elif eachpart in operators:
            curr_operator = eachpart
            if eachpart == '+':
                first_number = float(number_stack[1])
                second_number = float(number_stack[0])
                number_stack = number_stack[2:]
                number_stack.insert(0,second_number + first_number)
            elif eachpart == '-':
                first_number = float(number_stack[1])
                second_number = float(number_stack[0])
                number_stack = number_stack[2:]
                number_stack.insert(0,second_number - first_number)
            elif eachpart == '*':
                first_number = float(number_stack[1])
                second_number = float(number_stack[0])
                number_stack = number_stack[2:]
                number_stack.insert(0,second_number * first_number)
            elif eachpart == '/':
                first_number = float(number_stack[1])
                second_number = float(number_stack[0])
                number_stack = number_stack[2:]
                number_stack.insert(0,second_number / first_number)
    return round(number_stack[0])
​
​
​
def is_integer(eachpart):
    try:
        int(eachpart)
        return True
    except Exception as e:
        return False

