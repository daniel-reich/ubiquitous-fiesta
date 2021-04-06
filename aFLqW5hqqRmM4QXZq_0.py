
def bar_chart(results):
    ordered = sorted(results.items(), key=lambda x: (-x[1], x[0]))
    chart = '\n'.join('{}|{} {}'.format(k, '#'*(v//50), v) for k, v in ordered).replace('| ', '|')
    return chart

