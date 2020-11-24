
from itertools import product


class Hashabledict(dict):
    def __hash__(self):
        return hash(frozenset(self.items()))


def get_dict_combinations(dikt):
    return (dict(zip(dikt.keys(), values)) for values in product(*dikt.values()))


def bfsCreateTo(PG, TS):
    queue = list(TS['I'])
    visited = list(queue)

    while queue:
        start = queue.pop(0)
        for to in PG['to']:
            if start[0] == to[0] and PG['Eval'](to[1], start[1]):
                next = (to[3], Hashabledict(PG['Effect'](to[2], start[1])))
                TS['to'] = TS['to'].union({(start, to[2], next),})
                if next not in visited:
                    visited.append(next)
                    queue.append(next)
                TS['S'] = TS['S'].union({next})


def transitionSystemFromProgramGraph(PG, vars, labels):
    TS = {}
    TS['I'] = set()
    TS['Act'] = set(PG['Act'])
    TS['to'] = set()
    TS['AP'] = set(PG['Loc'].union(labels))

    for g0 in list(get_dict_combinations(vars)):
        if PG['Eval'](PG['g0'], g0):
            for i in PG['Loc0']:
                TS['I'].add((i, Hashabledict(g0)))

    TS['S'] = set(TS['I'])
    bfsCreateTo(PG, TS)

    def L(s):
        tags = set()
        tags.add(s[0])
        for label in labels:
            if PG['Eval'](label, s[1]):
                tags.add(label)
        return tags

    TS['L'] = L
    return TS
