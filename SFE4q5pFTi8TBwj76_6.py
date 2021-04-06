
def get_vote_count(votes):
    upvote = votes.get('upvotes')
    downvote = votes.get('downvotes')
    return upvote - downvote

