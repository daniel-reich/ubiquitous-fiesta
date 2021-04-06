
def is_undulating(n):
    if len(str(n)) < 3:
        return False
    else:
        digits = []
        for numbers in str(n):
            if numbers not in digits:
                digits.append(numbers)
        if len(digits) != 2:
            return False
        else:
            stringer = str(n)
            for i in range(len(stringer) - 1):
                if stringer[i] == stringer[i + 1]:
                    return False
                else:
                    continue
            return True

