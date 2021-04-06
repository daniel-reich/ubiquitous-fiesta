
def countdown(operands, target):   
    sign = ["+", "-", "*", "//"]
    for i in range(4):
        for o1 in range(len(operands)):
            for o2 in range(len(operands)):     
                if len(operands) > 2:
                    for o3 in range(len(operands)):
                        for j in range(4):
                            if len(operands) > 3:
                                for o4 in range(len(operands)):    
                                    for k in range(4):
                                        if len(operands) > 4:
                                            for o5 in range(len(operands)):
                                                for l in range(4):
                                                    if o1 != o2 != o3 != o4 != o5 and o3 != o1 != o4 and o4 != o2 != o5 and o1 != o5 != o3:
                                                        result = str(operands[o1])+sign[i]+str(operands[o2])+sign[j]+str(operands[o3])+sign[k]+str(operands[o4])+sign[l]+str(operands[o5])
                                                        if eval(result) == target:
                                                            return result
                                        else:
                                            if o1 != o2 != o3 != o4 and o3 != o1 != o4 and o2 != o4:
                                                result = str(operands[o1])+sign[i]+str(operands[o2])+sign[j]+str(operands[o3])+sign[k]+str(operands[o4])
                                                if eval(result) == target:
                                                    return result
                            else:
                                if o1 != o2 != o3 and o3 != o1:
                                    result = str(operands[o1])+sign[i]+str(operands[o2])+sign[j]+str(operands[o3])
                                    if eval(result) == target:
                                        return result
                else:
                    if o1 != o2:
                        result = str(operands[o1])+sign[i]+str(operands[o2])
                        if eval(result) == target:
                            return result

