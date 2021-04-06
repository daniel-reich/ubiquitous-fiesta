
def remove_special_characters(txt):
  
    t = ""
    for i in txt:
        if i == '!' or i=='?' or i =='~' or i == "'" or i=="`" or i=="'" or i == ',' or i == '|'  or i == '@' or i == '<' or i == '>' or  i == '=' or i == '+' or i == '{' or i == '}' or i == '[' or i == ']' or i == '.' or i == '#' or i == '$' or i == '%' or i == '^'or i == '&' or i == '*' or i == '(' or i == ')':
            pass
        else:
            t = t + i
    return t

