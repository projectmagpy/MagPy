import constants

def rank(g, y, b):
    r = []
    ignore = ["youtube", "xda", "answers.yahoo", "stackoverflow", "stackexchange", "git", "facebook"]
    for i in g:
        if any(d in i[1] for d in ignore):
            g.remove(i)
    for i in y:
        if any(d in i[1] for d in ignore):
            y.remove(i)
    for i in b:
        if any(d in i[1] for d in ignore):
            b.remove(i)

    if constants.search_algo == "seo":
        for i in zip(g, y, b):
            r.extend(list(i))
        for i in r:
            if r.count(i)>1:
                n = len(r)
                for j in r[::-1]:
                    n -= 1
                    if i == j and r.count(i)>1:
                        r.pop(n)

    elif constants.search_algo == "rec":
        from collections import Counter
        r = [i for (i, j) in Counter(g+b+y).most_common()]

    return r[:3]