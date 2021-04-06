
def correct_stream(usr, correct):
    output = []
    for i in range(len(correct)):
        if usr[i] == correct[i]:
            output.append(1)
        else:
            output.append(-1)
    return output

