
def bar_chart(results):
    results1 = sorted(results.items(), key=lambda x: x[0])
    results2 = sorted(results1, key=lambda x: x[1], reverse=True)
    out = ''
    for k, v in results2:
        hashes = v//50 * '#'
        if hashes:
            out += "%s|%s %d\n" % (k, hashes, v)
        else:
            out += "%s|%d\n" % (k, v)
    return out.strip()

