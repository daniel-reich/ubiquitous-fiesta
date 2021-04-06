
def cleave(string, lst):
    for my_index in list(reversed(sorted(word_list,key=len))):
        if my_index in string:
            string = string.replace(my_index," " + my_index.upper() + " ")
    string = string.lower().strip().replace("  "," ")        
    if(all(x in word_list for x in string.split(" "))): 
        return string
    else:
        return 'Cleaving stalled: Word not found'

