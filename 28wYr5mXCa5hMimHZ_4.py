
"""Without regex"""
​
def valid_name(name):
    status = False
    check_upper = lambda x: True if x.isupper() else False
    check_end = lambda x: True if x.endswith('.') else False
    check_dot = lambda x: True if '.' not in x else False
    list_ = name.split()
    last_word = list_[len(list_) - 1]
    last_name = True if check_upper(last_word[0]) and \
                        check_dot(last_word) and \
                        len(last_word) > 1 else False
    if last_name and len(list_) > 1:
        if len(list_) == 2:
            if len(list_[0]) == 2:
                if check_upper(list_[0][0]) and check_end(list_[0][1]):
                    status = True
            if len(list_[0]) > 2:
                if check_upper(list_[0][0]) and check_dot(list_[0]):
                    status = True
        if len(list_) == 3:
            if len(list_[0]) == 2 and len(list_[1]) == 2:
                if check_upper(list_[0][0]) and \
                        check_end(list_[0][1]) and \
                        check_upper(list_[1][0]) and \
                        check_end(list_[1][1]):
                    status = True
            if len(list_[0]) > 2 and len(list_[1]) == 2:
                if check_upper(list_[0][0]) and \
                        check_dot(list_[0]) and \
                        check_upper(list_[1][0]) and \
                        check_end(list_[1][1]):
                    status = True
            if len(list_[0]) > 2 and len(list_[1]) > 2:
                if check_upper(list_[0][0]) and \
                        check_dot(list_[0]) and \
                        check_upper(list_[1][0]) and \
                        check_dot(list_[1][1]):
                    status = True
    return status

