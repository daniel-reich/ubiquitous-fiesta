
max_time = {'very easy': 5, 'easy': 10, 'medium': 15, 'hard': 20}
difficulty = ['very easy', 'very easy', 'easy', 'easy', 'medium', 'medium', 'hard', 'hard']
allowed_time = sum(max_time[diff] for diff in difficulty) + 20 
​
def interview(lst, tot):
    completed = len(lst) == len(difficulty)
    in_time = tot <= allowed_time
    questions = all(lst[i] <= max_time[difficulty[i]] for i in range(len(lst)))
    return "qualified" if completed and in_time and questions else "disqualified"

