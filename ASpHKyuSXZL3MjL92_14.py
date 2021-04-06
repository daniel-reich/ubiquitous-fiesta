
def amplify(num):
    return [i*10 if i % 4 == 0 else i for i  in range(num+1)][1:]

