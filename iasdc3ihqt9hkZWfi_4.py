
def can_give_blood(donor, receiver):
    donations = {
        "O+" : ["O+", "A+", "B+", "AB+"], 
        "O-" : ["O+", "O-", "A+", "A-", "B+", "B-", "AB+", "AB-"], 
        "A+" : ["A+", "AB+"], 
        "A-" : ["A+", "A-", "AB+", "AB-"], 
        "B+" : ["B+", "AB+"], 
        "B-" : ["B+", "B-", "AB+", "AB-"],
        "AB+" : ["AB+"], 
        "AB-" : ["AB+", "AB-"]
    }
    return receiver in donations[donor]

