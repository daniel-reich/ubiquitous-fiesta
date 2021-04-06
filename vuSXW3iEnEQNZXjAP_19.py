
def create_square(length):
    if length is None:
        return ''
    if length <= 0:
        return ""
    if length == 1:
        return "#"
    if length == 2:
        return "##\n##"
    return "#"*length + "\n" + ("#" + " " * (length -2) + "#" + "\n") * (length -2)+"#"*length

