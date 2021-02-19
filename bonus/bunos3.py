
import networkx as nx

def nba_to_g(nba):
    g = nx.DiGraph() 
    for delta in nba['delta']:
        g.add_edge(delta[0], delta[2])
    return g

def get_safe(nba):
    g = nba_to_g(nba)
    cycles = list(nx.simple_cycles(g))
    q = set()
    for cycle in cycles:
        for node in cycle:
            if node in nba['f']:
                for n in cycle:
                    q.add(n)
    d = set()
    for delta in nba['delta']:
        if delta[0] in q and delta[2] in q:
            d.add(delta)
    safe ={'q':q,'sigma':nba['sigma'],'delta':d,'q0':nba['q0'],'f':q}
    return safe

def get_live(nba,safe):
    live = get_nba(safe)
    res = {}
    res['q0'] = {(q,1) for q in nba['q0']}.union({(q,2) for q in live['q0']})
    res['f'] = {(f,1) for f in nba['f']}.union({(f,2) for f in live['f']})
    res['q'] = {(q,1) for q in nba['q']}.union({(q,2) for q in live['q']})
    res['delta'] = {((d[0],1),d[1],(d[2],1)) for d in nba['delta']}.union({((d[0],2),d[1],(d[2],2)) for d in live['delta']})
    res['sigma'] = nba['sigma']
    return res


def get_nba(safe):
    nba={}
    delta = safe["delta"].copy()
    for q in safe['q']:
        condition = ' or '.join(['('+delta[1]+')' for delta in safe['delta'] if q==delta[0]])
        delta.add((q,"not("+condition+")",'___qfinal___'))
    delta.add(('___qfinal___', 'True', '___qfinal___'))
    nba['sigma'] = safe['sigma'].copy()
    nba['delta'] = delta
    nba['f'] = {'___qfinal___'}
    nba['q'] = safe['q'].copy().union(nba['f'])
    nba['q0'] = safe['q0'].copy()
    return nba

def decompose(nba):
    safe =  get_safe(nba)
    live = get_live(nba,safe)
    return safe,live


