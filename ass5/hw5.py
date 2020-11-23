
from itertools import product


class Hashabledict(dict):
    def __hash__(self):
        return hash(frozenset(self.items()))


def get_dict_combinations(dikt):
    return (dict(zip(dikt.keys(), values)) for values in product(*dikt.values()))


def bfsCreateTo(TS, ts1, ts2, h):
    queue = list(TS['I'])
    visited = list(queue)
    TS['S'] = TS['I'].copy()

    while queue:
        start = queue.pop(0)
        for (f1, a1, t1) in ts1['to']:
            for (f2, a2, t2) in ts2['to']:
                if start[0] == f1:
                    if a1 not in h:
                        next = (t1, start[1])
                        # to.add(set(next))
                        TS['to'] = TS['to'].union({(start, a1, next), })
                        if next not in visited:
                            visited.append(next)
                            queue.append(next)
                    elif a2 in h and start[1] == f2 and a1 == a2:
                        next = (t1, t2)
                        # to.add(set(next))
                        TS['to'] = TS['to'].union({(start, a1, next), })
                        if next not in visited:
                            visited.append(next)
                            queue.append(next)
                if start[1] == f2:
                    if a2 not in h:
                        next = (start[0], t2)
                        # to.add(set(next))
                        TS['to'] = TS['to'].union({(start, a2, next), })
                        if next not in visited:
                            visited.append(next)
                            queue.append(next)

    for (s1, a, s2) in TS['to']:
        TS['S'].add(s2)


def interleave_transition_systems(ts1, ts2, h):
    TS = {}
    TS['I'] = set(product(ts1['I'], ts2['I']))
    TS['S'] = TS['I'].copy()
    TS['Act'] = set(ts1['Act'].union(ts2['Act']))
    TS['AP'] = set(ts1['AP'].union(ts2['AP']))
    TS['to'] = set()
    TS['S'] = set()

    def L(s):
        return ts1['L'](s[0]).union(ts2['L'](s[1]))
    TS['L'] = L

    bfsCreateTo(TS, ts1, ts2, h)

    return TS


def interleave_program_graphs(pg1, pg2):
    PG = {}
    return PG
