
def relation_to_luke(name):
    output_string = "Luke, I am your "
​
    if name == "Darth Vader":
        return  output_string + "father."
    elif name == "Leia":
        return output_string + "sister."
    elif name == "Han":
        return output_string + "brother in law."
    else:
        return output_string + "droid."

