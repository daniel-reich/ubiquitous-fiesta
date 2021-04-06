
def award_prizes(names):
    placing = {
        0: "Gold",
        1: "Silver",
        2: "Bronze"
    }
    sorted_names = sorted(names.items(), key=lambda x: x[1], reverse=True)
    return {item[0]: placing.get(i, "Participation") for i, item in enumerate(sorted_names)}

