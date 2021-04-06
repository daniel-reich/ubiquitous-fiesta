
def get_vote_count(votes):
    return votes["upvotes"]-votes["downvotes"]
print(get_vote_count({ "upvotes": 13, "downvotes": 0 }))

