
def valid_color(text):
    new_text = text.replace("(", ",")
    new_text2 = new_text.replace(")", "")
    new_text4 = new_text2.replace(" ", "")
    temp_list = new_text4.split(",")
    
        
    if text[(text.index("("))-1] == " ":
        return False
    else:
        if temp_list[0] == "rgba":
            if len(temp_list) != 5:
                return False
            else:
                for index in range(1,len(temp_list)-1):
                    if "%" not in temp_list[index]:
                      if float(temp_list[index]) <= 255 and float(temp_list[index]) >= 0:
                          continue
                      else:
                          return False
                    if "%" in temp_list[index]:
                      integer = (temp_list[index].replace("%",""))
                      if float(integer) >= 0 and float(integer) <= 100:
                          continue
                      else:
                          return False
                if float(temp_list[-1]) >= 0 and float(temp_list[-1]) <= 1:
                    return True
                else:
                    return False
            
        if temp_list[0] == "rgb":
            if len(temp_list) != 4:
                return False
            else:
                for index in range(1,len(temp_list)):
                    if index == len(temp_list) -1:
                        if "%" not in temp_list[index]:
                            if temp_list[index] != "":
                                if float(temp_list[index]) <= 255 and float(temp_list[index]) >= 0:
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        if "%" in temp_list[index]:
                            integer = (temp_list[index].replace("%",""))
                            if float(integer) >= 0 and float(integer) <= 100:
                                return True
                            else:
                                return False
                    if "%" not in temp_list[index]:
                        if temp_list[index] != "":
                          if float(temp_list[index]) <= 255 and float(temp_list[index]) >= 0:
                              continue
                          else:
                              return False
                        else:
                            return False
                    if "%" in temp_list[index]:
                      integer = (temp_list[index].replace("%",""))
                      if float(integer) >= 0 and float(integer) <= 100:
                          continue
                      else:
                          return False

