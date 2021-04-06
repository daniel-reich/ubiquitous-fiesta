
def bird_code(lst):
    birds_codes = []
    for bird in lst:
        bird_names = bird.replace("-", " ").split()
        if len(bird_names) == 1:
            code = ""
            for i in range(4):
                code += bird_names[0][i]
            birds_codes.append(code.upper())
​
        if len(bird_names) == 2:
            code = ""
            for j in range(len(bird_names)):
                for i in range(2):
                    code += bird_names[j][i]
            birds_codes.append(code.upper())
​
        if len(bird_names) == 3:
            code = ""
            for j in range(len(bird_names) - 1):
                for i in range(1):
                    code += bird_names[j][i]
            code += bird_names[2][0]
            code += bird_names[2][1]
            birds_codes.append(code.upper())
        if len(bird_names) == 4:
            code = ""
            for j in range(len(bird_names)):
                for i in range(1):
                    code += bird_names[j][i]
            birds_codes.append(code.upper())
​
    return birds_codes

