
def relation_to_luke(name):
    relations = {
        "Darth Vader":"father",
        "Leia":"sister",
        "Han":"brother in law",
        "R2D2":"droid",
    }
    return "Luke, I am your " + relations[name] + "." if name in relations else ""

