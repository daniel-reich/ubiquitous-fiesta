
def make_plus_function(base_num):
    def specific_plus_function(plus_num):
        new_num = base_num + plus_num
        return new_num
​
    return specific_plus_function

