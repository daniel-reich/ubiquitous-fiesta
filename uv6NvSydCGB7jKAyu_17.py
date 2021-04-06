
#At least 2 instances of the letter "s" (must be together ss), or      
#Zero instances of the letter "s".
def is_parsel_tongue(sentence):
    sentence = sentence.lower().strip()
    s_list = sentence.split(" ")
    for i in s_list:
        if i.count("s") != 0 and i.count("s") < 2:
            print(s_list)
            return False
        if i.count("s") >= 2:
            if i[i.index("s")] == "s" and i[i.index("s")+1] == "s":
                return True
            else:
                return False
                
    return True

