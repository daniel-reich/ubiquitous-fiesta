
def incremental_depth(lst):
    ret = []
    for num,ele in enumerate(lst):
        num = int(num)
        if num == 0:
            ret.append(ele)
        else:
        #why this site doesn't support f-string?f*ck this
            ele = [ele]
            if num == 1:
                eval('ret.append(ele)')
            else:
                eval('ret'+ ("[1]" * (num-1)) + '.append(ele)')
    return ret
    
    
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

