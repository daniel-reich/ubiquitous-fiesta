
def weekly_salary(lst):
  weekly = 0
  end_week = 0
  weekly_overtime = 0
  end_week_overtime = 0
  daily = 0
  daily_overtime = 0
  end_result = 0
  end_overtime_result = 0
  for i in range(len(lst)):
    if i < 5:
      if lst[i] > 8:
        weekly_overtime += lst[i] - 8
      weekly += lst[i]
    elif i >= 5:
      if lst[i] > 8:
        end_week_overtime += lst[i] - 8
      end_week += lst[i]
  daily += (weekly - weekly_overtime) * 10
  daily_overtime += weekly_overtime * 15
  end_result += (end_week - end_week_overtime) * 20
  end_overtime_result += end_week_overtime * 30
  return daily + daily_overtime + end_result + end_overtime_result

