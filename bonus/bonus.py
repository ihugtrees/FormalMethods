
from itertools import product
from re import findall
import networkx as nx


def gnba_to_nba(g):
    nba = {}
    nba['sigma'] = g['sigma']
    nba['f'] = {(n, 1) for n in g['f'][0]}
    nba['q0'] = {(n, 1) for n in g['q0']}
    nba['q'] = set(product(g["q"], range(1, len(g["f"]) + 1)))

    delta = set()
    for (src, cond, dest) in g['delta']:
        for i in range(len(g['f'])):
            if src not in g['f'][i]:
                delta.add(((src, i+1), cond, (dest, i+1)))
            else:
                delta.add(
                    ((src, i+1), cond, (dest, ((i+1) % len(g['f'])) + 1)))

    nba['delta'] = delta
    return nba


def upholds(s, phi):
    '''
    :param s: set of literals.
    :param phi: logical expression.
    :return: s |= phi

    for instance:
    upholds({'a'}, 'not(a or b) and not c') -> False
    upholds({'d'}, 'not(a or b) and not c') -> True
    upholds({'a', 'b', 'c'}, 'not(a or b) and not c') -> False
    '''
    symbols = {'and', 'or', 'not', '(', ')', ' '}
    literals = set(findall(r"[\w']+", phi)) - symbols
    eta = {x: x in s for x in literals}
    return eval(phi, None, eta)


def bfsCreateTo(TS, ts, a):
    queue = list(TS['I'])
    visited = list(queue)
    TS['S'] = TS['I'].copy()

    while queue:
        start = queue.pop(0)
        for (f1, a1, t1) in ts['to']:
            for (f2, phi, t2) in a['delta']:
                if start[0] == f1 and start[1] == f2 and upholds(ts['L'](t1), phi):
                    next = (t1, t2)
                    TS['to'] = TS['to'].union({((f1, f2), a1, next), })
                    if next not in visited:
                        visited.append(next)
                        queue.append(next)

    for (s1, a, s2) in TS['to']:
        TS['S'].add(s2)


def transition_system_nba_product(ts, a):
    TSxA = {}

    i = set()
    for s0 in ts['I']:
        for delta in a['delta']:
            if delta[0] in a['q0'] and upholds(ts['L'](s0), delta[1]):
                i.add((s0, delta[2]))

    def L(tup):
        return tup[1]

    TSxA['Act'] = ts['Act']
    TSxA['AP'] = a['q']
    TSxA['L'] = L
    TSxA['I'] = i
    TSxA['to'] = set()

    bfsCreateTo(TSxA, ts, a)

    return TSxA


def make_safe(nba):
    safe = {'sigma': nba['sigma'].copy(),
            'q0': nba['q0'].copy(),
            'q': set(),
            'delta': set(),
            'f': set()}

    graph = nx.DiGraph()
    for delta in nba['delta']:
        graph.add_edge(delta[0], delta[2])
    cycles = list(nx.simple_cycles(graph))

    for cycle in cycles:
        for node in cycle:
            if node in nba['f']:
                for n in cycle:
                    safe['q'].add(n)
                    safe['f'].add(n)

    for delta in nba['delta']:
        if delta[0] in safe['q'] and delta[2] in safe['q']:
            safe['delta'].add(delta)

    return safe


def reverse(safe):
    rev_safe = {'q0': safe["q0"].copy(),
                'f': {'___qfinal___'},
                'sigma': safe["sigma"].copy(),
                'q': safe["q"].copy(),
                'delta': safe["delta"].copy()}
    rev_safe['q'].add('___qfinal___')

    for q in safe['q']:
        new_cond = ' or '.join(
            [f'({delta[1]})' for delta in safe['delta'] if q == delta[0]])
        rev_safe['delta'].add((q, f"not({new_cond})", '___qfinal___'))

    rev_safe['delta'].add(('___qfinal___', 'True', '___qfinal___'))
    return rev_safe


def make_live(nba, safe):
    reverse_nba = reverse(safe)
    live = {'sigma': nba['sigma'].copy(),
            'q': {(q, 1) for q in nba['q']},
            'f': {(f, 1) for f in nba['f']},
            'q0': {(q, 1) for q in nba['q0']},
            'delta': {((d[0], 1), d[1], (d[2], 1)) for d in nba['delta']}}

    live['q0'] = live['q0'].union({(q, 2) for q in reverse_nba['q0']})
    live['f'] = live['f'].union({(f, 2) for f in reverse_nba['f']})
    live['q'] = live['q'].union({(q, 2) for q in reverse_nba['q']})
    live['delta'] = live['delta'].union(
        {((d[0], 2), d[1], (d[2], 2)) for d in reverse_nba['delta']})
    return live


def decompose(nba):
    safe = make_safe(nba)
    live = make_live(nba, safe)
    return safe, live
