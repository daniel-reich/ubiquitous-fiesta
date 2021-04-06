
def markdown(symb):
    def italicise(string, correct):
        import re
        string_list = string.split()
        string_list_copy = string_list.copy()
        for i in range(len(string_list_copy)):
            if string_list_copy[i].isalpha() != True:
                list_list = list(string_list_copy[i])
                while string_list_copy[i].isalpha() != True:
                    list_list.pop(-1)
                    string_list_copy[i] = ''.join(list_list)
            
            
        for i in range(len(string_list)):
            if string_list_copy[i].lower() == correct.lower():
                new_list = [symb, symb, symb]
                new_list[1] = string_list[i]
                string_list[i] = ''.join(new_list)
                
        return ' '.join(string_list)
    return italicise

