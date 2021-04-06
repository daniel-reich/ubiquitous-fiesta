
import re
def bracket_logic(text):
    new_text = re.findall(r'[\(\)<>\[\]\{\}]',text)
    stack = []
    match_list = ["<>","{}","[]","()"]
    length = len(new_text)
    if length == 0:
        return True
    if length%2 == 1:
        return False
    stack = []
    for i in range(length):
        if len(stack) == 0:
            if new_text[i] in ")]}>":
                return False
            else:
                stack.append(new_text[i])
        else:
            if new_text[i] in ")]}>":
                if (stack[-1]+ new_text[i]) not in match_list:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(new_text[i])
    if len(stack) != 0:
        return False
    else:
        return True

