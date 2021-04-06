
import itertools
def simple_equation(a,b,c):
    numbers = [a,b,c]
    for eachcombo in itertools.permutations(numbers,2):
        first_num = eachcombo[0]
        second_num = eachcombo[1]
        if c != first_num and c != second_num:
            if first_num + second_num == c:
                return '{}+{}={}'.format(first_num,second_num,c)
            elif first_num - second_num == c:
                return '{}-{}={}'.format(first_num,second_num,c)
            elif first_num * second_num == c:
                return '{}*{}={}'.format(first_num,second_num,c)
            try:
                if first_num // second_num == c:
                    return '{}/{}={}'.format(first_num,second_num,c)
            except Exception as e:
                continue
        elif b != first_num and b != second_num:
            if first_num + second_num == b:
                return '{}+{}={}'.format(first_num,second_num,b)
            elif first_num - second_num == b:
                return '{}-{}={}'.format(first_num,second_num,b)
            elif first_num * second_num == b:
                return '{}*{}={}'.format(first_num,second_num,b)
            try:
                if first_num // second_num == b:
                    return '{}/{}={}'.format(first_num,second_num,b)
            except Exception as e:
                continue
        elif a != first_num and a != second_num:
            if first_num + second_num == a:
                return '{}+{}={}'.format(first_num,second_num,a)
            elif first_num - second_num == a:
                return '{}-{}={}'.format(first_num,second_num,a)
            elif first_num * second_num == a:
                return '{}*{}={}'.format(first_num,second_num,a)
            try:
                if first_num // second_num == a:
                    return '{}/{}={}'.format(first_num,second_num,a)
            except Exception as e:
                continue
    return ''

