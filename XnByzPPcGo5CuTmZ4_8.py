
def kix_code(addr):
​
    def find_first_digit(txt):
        for i, c in enumerate(txt):
            if c.isdigit():
                return i-1
​
    def replace_non_num(txt):
        new_str = ""
        for char in txt:
            if char.isalnum():
                new_str += char
            else:
                new_str += "X"
        return new_str.upper()
​
    addr_list = addr.split(",")
    first_part = addr_list[2].split()
    first_digit_pos = find_first_digit(addr_list[1])
    second_part = addr_list[1][first_digit_pos:]
    return first_part[0] + first_part[1] + replace_non_num(second_part[1:])

