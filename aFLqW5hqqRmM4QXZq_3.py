
def bar_chart(results):
  chart = ""
  q1 = "Q1|" + "#" * (results["Q1"]//50) +" {}\n".format(results["Q1"])
  q2 = "Q2|" + "#" * (results["Q2"]//50) +" {}\n".format(results["Q2"])
  q3 = "Q3|" + "#" * (results["Q3"]//50) +" {}\n".format(results["Q3"])
  q4 = "Q4|" + "#" * (results["Q4"]//50) +" {}\n".format(results["Q4"])
  
  qorder = [q[0] for q in sorted(list(results.items()), key=lambda x:(-x[1], x[0]))]
  for q in qorder:
    if q == 'Q1':
      chart += q1
    elif q == 'Q2':
      chart += q2
    elif q == 'Q3':
      chart += q3
    elif q == 'Q4':
      chart += q4
  return chart.replace(' 0','0')[:-1]

