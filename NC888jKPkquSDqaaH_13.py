
from collections import OrderedDict
def clean_up(files, sort):
    dict=OrderedDict()
    for x in files:
        if sort=="prefix":
            if x.split(".")[0] in dict:
                dict[x.split(".")[0]]=dict[x.split(".")[0]] + "," + x 
            else:
                dict[x.split(".")[0]]=x 
        elif sort=="suffix":
            if x.split(".")[1] in dict:
                dict[x.split(".")[1]]=dict[x.split(".")[1]] + "," + x 
            else:
                dict[x.split(".")[1]]=x 
    return [x.split(",") for x in dict.values()]

