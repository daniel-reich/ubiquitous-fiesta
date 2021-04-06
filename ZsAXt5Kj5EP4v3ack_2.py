
def secret(txt):
    number = sum(1 for ch in txt if ch == "$")
    parent, child, class_name, times = "".join(
        "." if ch in ">*" else "" if ch == "$" else ch for ch in txt).split(".")
    return "<{}>".format(parent) + "".join("<{} class='{}{}'></{}>".format(child, class_name, "0"*(number - 1) + str(n), child) for n in range(1, int(times) + 1)) + "</{}>".format(parent)

