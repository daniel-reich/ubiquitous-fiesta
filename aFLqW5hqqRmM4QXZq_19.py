
def bar_chart(results):
  bars = []
  for quarter, sales in sorted(results.items(), key=lambda kv: (kv[1],4-int(kv[0][1])), reverse=True):
    bar = quarter + "|"
    bar += "0" if sales==0 else ("#" * (sales//50)) + " " + str(sales)
    bars.append(bar)
  return "\n".join(bars)

