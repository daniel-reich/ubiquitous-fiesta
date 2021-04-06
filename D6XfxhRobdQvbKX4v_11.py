
def first_before_second(s, first, second):
    if s.rfind(first) < s.find(second):
        return True
    else:
        return False

