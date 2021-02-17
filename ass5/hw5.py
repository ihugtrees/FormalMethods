
from itertools import product


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
                        TS['to'] = TS['to'].union({(start, a1, next), })
                        if next not in visited:
                            visited.append(next)
                            queue.append(next)
                    elif a2 in h and start[1] == f2 and a1 == a2:
                        next = (t1, t2)
                        TS['to'] = TS['to'].union({(start, a1, next), })
                        if next not in visited:
                            visited.append(next)
                            queue.append(next)
                if start[1] == f2:
                    if a2 not in h:
                        next = (start[0], t2)
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
    PG['Loc'] = set(product(pg1['Loc'], pg2['Loc']))
    PG['Act'] = pg1['Act'].union(pg2['Act'])
    PG['Loc0'] = set(product(pg1['Loc0'], pg2['Loc0']))
    pg1g0 = pg1['g0']
    pg2g0 = pg2['g0']
    PG['g0'] = f'{pg1g0} and {pg2g0}'

    def evaluate(cond, eta):
        if cond == PG['g0']:
            return (pg1['Eval'](pg1['g0'], eta) and pg2['Eval'](pg2['g0'], eta))
        else:
            try:
                return pg1a['Eval'](cond, eta)
            except:
                return pg2['Eval'](cond, eta)

    def effect(act, eta):
        if act in pg1['Act']:
            return pg1['Effect'](act, eta)
        else:
            return pg2['Effect'](act, eta)

    to = set()
    for (lfrom, cond, act, lto) in pg1['to']:
        for l in pg2['Loc']:
            to.add(((lfrom, l), cond, act, (lto, l)))

    for (lfrom, cond, act, lto) in pg2['to']:
        for l in pg1['Loc']:
            to.add(((l, lfrom), cond, act, (l, lto)))

    PG['Eval'] = evaluate
    PG['Effect'] = effect
    PG['to'] = to

    return PG


def evaluate(cond, eta):
    return {
        'true': lambda eta: True,
        'ncoke > 0': lambda eta: eta['ncoke'] > 0,
        'nsprite > 0': lambda eta: eta['nsprite'] > 0,
        'ncoke=0 && nsprite=0': lambda eta: eta['ncoke'] == 0 and eta['nsprite'] == 0,
        'ncoke=2 && nsprite=2': lambda eta: eta['ncoke'] == 2 and eta['nsprite'] == 2,
    }[cond](eta)
