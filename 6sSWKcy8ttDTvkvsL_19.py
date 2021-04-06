
def after_n_days(days, n):
  lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
        "Sunday"]
  return [lst[(lst.index(day)+n)%7] for day in days]

