import pickle


def pause(cur, t, i, r):
    l = [cur, t, i, r]
    wr = open("save.p", "w")
    pickle.dump(l, wr)

def resume():
    res = pickle.load(open("save.p"))
    return res

    # [cur, t, i, r]