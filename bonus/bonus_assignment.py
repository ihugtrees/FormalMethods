from itertools import product
import itertools
from re import findall


def gnba_to_nba(gnba):
    nba = dict()
    nba["sigma"] = gnba["sigma"]
    nba["q"] = set(itertools.product(gnba["q"], range(1, len(gnba["f"])+1)))
    nba["q0"] = set(itertools.product(gnba["q0"], range(1, 2)))
    nba["f"] = set(itertools.product(gnba["f"][0], range(1, 2)))
    nba["delta"] = deltaCreation(gnba["delta"], gnba["f"])
    return nba


def deltaCreation(oldDelta, fGroups):
    delta = set()
    for curDelta in oldDelta:
        for i in range(1, len(fGroups)+1):
            if(curDelta[0] in fGroups[i-1]):
                delta.add(((curDelta[0], i), curDelta[1],
                           (curDelta[2], ((i % len(fGroups))+1))))
            else:
                delta.add(((curDelta[0], i), curDelta[1], (curDelta[2], i)))

    return delta


gnba = {'q': {'q2', 'q1', 'q0'},
        'sigma': {'true', 'not a', 'a'},
        'delta': {('q1', 'a', 'q0'), ('q1', 'not a', 'q2'), ('q0', 'true', 'q1'), ('q1', 'true', 'q1'), ('q2', 'true', 'q1')},
        'q0': {'q1'},
        'f': [{'q0'}, {'q2'}]
        }
nba = {'q': {('q2', 2), ('q0', 2), ('q2', 1), ('q1', 1), ('q0', 1), ('q1', 2)},
       'sigma': {'a', 'true', 'not a'},
       'delta': {(('q1', 2), 'a', ('q0', 2)), (('q0', 1), 'true', ('q1', 2)), (('q1', 1), 'a', ('q0', 1)), (('q2', 2), 'true', ('q1', 1)), (('q1', 1), 'not a', ('q2', 1)), (('q0', 2), 'true', ('q1', 2)), (('q1', 1), 'true', ('q1', 1)),
                 (('q2', 1), 'true', ('q1', 1)), (('q1', 2), 'not a', ('q2', 2)), (('q1', 2), 'true', ('q1', 2))},
       'q0': {('q1', 1)},
       'f': {('q0', 1)}}

# print(gnba_to_nba(gnba) == nba) # True
gnba = {'q': {'q2', 'q1', 'q0'},
        'sigma': {'true', 'not a', 'a'},
        'delta': {('q1', 'a', 'q0'), ('q1', 'not a', 'q2'), ('q0', 'true', 'q1'), ('q1', 'true', 'q1'), ('q2', 'true', 'q1')},
        'q0': {'q1'},
        'f': [{'q0'}, {'q2'}]
        }
nba = {'q': {('q2', 2), ('q0', 2), ('q2', 1), ('q1', 1), ('q0', 1), ('q1', 2)},
       'sigma': {'a', 'true', 'not a'},
       'delta': {(('q1', 2), 'a', ('q0', 2)), (('q0', 1), 'true', ('q1', 2)), (('q1', 1), 'a', ('q0', 1)), (('q2', 2), 'true', ('q1', 1)), (('q1', 1), 'not a', ('q2', 1)), (('q0', 2), 'true', ('q1', 2)), (('q1', 1), 'true', ('q1', 1)),
                 (('q2', 1), 'true', ('q1', 1)), (('q1', 2), 'not a', ('q2', 2)), (('q1', 2), 'true', ('q1', 2))},
       'q0': {('q1', 1)},
       'f': {('q0', 1)}}

# print(gnba_to_nba(gnba) == nba) # True


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


def transition_system_nba_product(ts, a):
    tsXa = dict()
    # tsXa["S"]=set(itertools.product(ts["S"],a["q"]))
    tsXa["Act"] = ts["Act"]
    tsXa["I"] = makeI(ts, a)
    toAndS = makeToAndS(ts, a, tsXa["I"], makeAllToOptions(ts, a))
    tsXa["S"] = toAndS["S"]
    tsXa["to"] = toAndS["to"]
    tsXa["AP"] = a["q"]
    tsXa["L"] = lambda s: s[1]
    return tsXa


def makeI(ts, a):
    I = set()
    for s in ts["I"]:
        for delta in a["delta"]:
            if(delta[0] in a["q0"] and upholds(ts["L"](s), delta[1])):
                I.add((s, delta[2]))
    return I


def makeAllToOptions(ts, a):
    allToOptions = set()
    for tsTo in ts["to"]:
        for aDelta in a["delta"]:
            if(upholds(ts["L"](tsTo[2]), (aDelta[1]))):
                allToOptions.add(
                    ((tsTo[0], aDelta[0]), tsTo[1], (tsTo[2], aDelta[2])))
    return allToOptions


def makeToAndS(ts, a, I, allToOptions):
    reachAble = I.copy()
    to = set()
    queue = I.copy()
    while(len(queue) != 0):
        cur = queue.pop()
        for toOption in allToOptions:
            if (toOption[0] == cur):
                to.add(toOption)
                if(toOption[2] not in reachAble):
                    reachAble.add(toOption[2])
                    queue.add(toOption[2])

    return {"to": to, "S": reachAble}


# Transition System
ts = {'S': {'s0', 's1', 's2', 's3', 's5', 's4'},
      'Act': {'beta', 'alpha', 'gamma'},
      'to': {('s5', 'alpha', 's2'), ('s3', 'gamma', 's1'), ('s5', 'beta', 's1'), ('s1', 'alpha', 's4'), ('s4', 'gamma', 's1'), ('s0', 'alpha', 's3'), ('s4', 'beta', 's5'), ('s2', 'gamma', 's1'), ('s0', 'beta', 's1')}, 'I': {'s0'},
      'AP': {'b', 'c', 'a'},
      'L': lambda s: {'s0': {'a', 'b'}, 's1': {'a', 'b', 'c'}, 's2': {'b', 'c'}, 's3': {'a', 'c'}, 's4': {'a', 'c'}, 's5': {'a', 'c'}}[s]}

# NBA
a = {'q': {'q3', 'q2', 'q0', 'q1'},
     'sigma': {'a', 'b and not c', 'not(b and not c) and not a', 'b and not c and not a', '(a or b) and not c', 'c', 'not(b and not c)', 'not(a or b) and not c'},
     'delta': {('q1', 'b and not c and not a', 'q1'), ('q2', 'c', 'q0'), ('q1', 'a', 'q2'), ('q0', 'not(b and not c)', 'q0'), ('q1', 'not(b and not c) and not a', 'q0'), ('q0', 'b and not c', 'q1'), ('q2', '(a or b) and not c', 'q3'), ('q2', 'not(a or b) and not c', 'q2')},
     'q0': {'q0'},
     'f': {'q3'}}

# TS x A
tsXa = {'S': {('s2', 'q0'), ('s0', 'q1'), ('s1', 'q0'), ('s1', 'q2'), ('s5', 'q0'), ('s3', 'q2'), ('s4', 'q0')},
        'Act': {'beta', 'alpha', 'gamma'},
        'to': {(('s1', 'q2'), 'alpha', ('s4', 'q0')), (('s5', 'q0'), 'alpha', ('s2', 'q0')), (('s1', 'q0'), 'alpha', ('s4', 'q0')), (('s2', 'q0'), 'gamma', ('s1', 'q0')), (('s4', 'q0'), 'beta', ('s5', 'q0')), (('s3', 'q2'), 'gamma', ('s1', 'q0')), (('s0', 'q1'), 'alpha', ('s3', 'q2')), (('s4', 'q0'), 'gamma', ('s1', 'q0')), (('s5', 'q0'), 'beta', ('s1', 'q0')), (('s0', 'q1'), 'beta', ('s1', 'q2'))},
        'I': {('s0', 'q1')},
        'AP': {'q3', 'q1', 'q2', 'q0'},
        'L': lambda s: s[1]}

newtsXa = transition_system_nba_product(ts, a)
# print(tsXa == newtsXa) # True

# print(newtsXa["S"]==tsXa["S"])
# print(newtsXa["Act"]==tsXa["Act"])
# print(newtsXa["to"]==tsXa["to"])
# print(newtsXa["I"]==tsXa["I"])
# print(newtsXa["AP"]==tsXa["AP"])
# print(newtsXa["L"]==tsXa["L"])
# TODO check that


def decompose(nba):
    a_safe = createAsafe(nba)
    # print(a_safe)
    a_live = createAlive(nba, a_safe)
    # print(a_live)
    return (a_safe, a_live)


def createAsafe(nba):
    aSafe = dict()
    aSafe["sigma"] = nba["sigma"]
    aSafe["q0"] = nba["q0"]
    qInFWithCycle = searchQInFWithCycle(nba)
    aSafe["q"] = goodNodes(nba, qInFWithCycle)
    aSafe["f"] = aSafe["q"]
    aSafe["delta"] = createDelta(nba, aSafe["q"])

    return aSafe


def searchQInFWithCycle(nba):
    qInFWithCycle = set()

    for qInF in nba['f']:
        reachAbleNodes = set()
        for delta in nba['delta']:
            if(delta[0] == qInF):
                reachAbleNodes.add(delta[2])
        if(qInF in reachAbleNodes):
            qInFWithCycle.add(qInF)
            continue
        queue = reachAbleNodes.copy()
        flag = False
        while(len(queue) != 0 and not flag):
            currNode = queue.pop()
            for delta in nba['delta']:
                if(delta[0] == currNode and delta[2] not in reachAbleNodes):
                    reachAbleNodes.add(delta[2])
                    if (qInF == delta[2]):
                        qInFWithCycle.add(qInF)
                        flag = True
                        break
    #print (qInFWithCycle)
    return qInFWithCycle


def goodNodes(nba, qInFWithCycle):
    goodNodes = qInFWithCycle.copy()

    for q in nba['q']:
        inGooNodesFlag = False
        if(q in goodNodes):
            break
        reachAbleNodes = set()
        for delta in nba['delta']:
            if(delta[0] == q):
                reachAbleNodes.add(delta[2])
                if(delta[2] in goodNodes):
                    goodNodes.add(q)
                    inGooNodesFlag = True
                    break
        queue = reachAbleNodes.copy()

        while(len(queue) != 0 and not inGooNodesFlag):
            currNode = queue.pop()
            for delta in nba['delta']:
                if(delta[0] == currNode and delta[2] not in reachAbleNodes):
                    reachAbleNodes.add(delta[2])
                    if (delta[2] in goodNodes):
                        goodNodes.add(q)
                        inGooNodesFlag = True
                        break
    #print (goodNodes)
    return goodNodes


def createDelta(nba, reachAbleQ):
    newDelta = set()
    for delta in nba["delta"]:
        if(delta[0] in reachAbleQ and delta[2] in reachAbleQ):
            newDelta.add(delta)

    return newDelta


def createAlive(nba, a_safe):
    first = nba.copy()
    second = transformation(a_safe)
    # print(second["delta"])
    aLive = makeGNBA(first, second)
    return aLive


def transformation(a_safe):
    a_SafeT = dict()
    a_SafeT["sigma"] = a_safe["sigma"]
    a_SafeT["q0"] = a_safe["q0"]
    tempQ = a_safe["q"].copy()
    tempQ.add('___qfinal___')
    a_SafeT["q"] = tempQ
    a_SafeT["f"] = {'___qfinal___'}
    tempDelta = a_safe["delta"].copy()
    for q in a_safe["q"]:
        newCondition = ""
        for delta in a_safe["delta"]:
            if(delta[0] == q):
                if (newCondition == ""):
                    newCondition = "("+delta[1]+")"
                else:
                    newCondition = newCondition + " or " + "("+delta[1]+")"
        if(newCondition == ""):
            tempDelta.add((q, "true", '___qfinal___'))
        else:
            newCondition = "not("+newCondition+")"
            tempDelta.add((q, newCondition, '___qfinal___'))
    tempDelta.add(('___qfinal___', 'True', '___qfinal___'))
    #print("temp delta")
    # print(tempDelta)
    a_SafeT["delta"] = tempDelta
    return a_SafeT


def makeGNBA(first, second):
    gnba = dict()
    gnba["sigma"] = first["sigma"]
    q0First = set(itertools.product(first["q0"], range(1, 2)))
    q0Second = set(itertools.product(second["q0"], range(2, 3)))
    gnba["q0"] = q0First.union(q0Second)
    gnbaF = set()
    for f in first["f"]:
        gnbaF.add((f, 1))
    for f in second["f"]:
        gnbaF.add((f, 2))
    gnba["f"] = gnbaF

    gnbaQ = set()
    for q in first["q"]:
        gnbaQ.add((q, 1))
    for q in second["q"]:
        gnbaQ.add((q, 2))
    gnba["q"] = gnbaQ

    gnbaDelta = set()
    # for deltaFirst in first["delta"]:
    # for deltaSecond in second["delta"]:
    # if (deltaFirst[1] == deltaSecond[1]):
    # gnbaDelta.add(((deltaFirst[0],deltaSecond[0]),deltaFirst[1],(deltaFirst[2],deltaSecond[2])))
    # print(((deltaFirst[0],deltaSecond[0]),deltaFirst[1],(deltaFirst[2],deltaSecond[2])))
    for deltaFirst in first["delta"]:
        gnbaDelta.add(((deltaFirst[0], 1), deltaFirst[1], (deltaFirst[2], 1)))
    for deltaSecond in second["delta"]:
        gnbaDelta.add(
            ((deltaSecond[0], 2), deltaSecond[1], (deltaSecond[2], 2)))
        # print(((deltaFirst[0],deltaSecond[0]),deltaFirst[1],(deltaFirst[2],deltaSecond[2])))
    gnba["delta"] = gnbaDelta

    return gnba


a = {'q': {'s1', 's0', 's4', 's3', 's2'},
     'sigma': {'q', 'p'},
     'delta': {('s0', 'p and not q', 's1'), ('s0', 'not p and not q', 's0'), ('s1', 'not p and q', 's2'), ('s2', 'not p and q', 's2'), ('s1', 'p', 's3'), ('s3', 'q', 's4'), ('s2', 'not p and not q', 's0'), ('s0', 'not p and q', 's2'), ('s1', 'not q', 's1'), ('s4', 'True', 's4'), ('s2', 'q', 's3')},
     'q0': {'s0'},
     'f': {'s0', 's3'}}

a_safe = {'q': {'s0', 's1', 's2'},
          'sigma': {'q', 'p'},
          'delta': {('s0', 'p and not q', 's1'), ('s0', 'not p and not q', 's0'), ('s1', 'not p and q', 's2'), ('s2', 'not p and q', 's2'), ('s2', 'not p and not q', 's0'), ('s0', 'not p and q', 's2'), ('s1', 'not q', 's1')},
          'q0': {'s0'},
          'f': {'s0', 's1', 's2'}}

a_live = {'q': {('s2', 2), ('s1', 2), ('s3', 1), ('s2', 1), ('s0', 2), ('s1', 1), ('s0', 1), ('___qfinal___', 2), ('s4', 1)},
          'sigma': {'q', 'p'},
          'delta': {(('s0', 2), 'not p and not q', ('s0', 2)), (('s1', 2), 'not((not p and q) or (not q))', ('___qfinal___', 2)), (('___qfinal___', 2), 'True', ('___qfinal___', 2)), (('s0', 2), 'not p and q', ('s2', 2)), (('s1', 1), 'not q', ('s1', 1)), (('s0', 2), 'p and not q', ('s1', 2)), (('s2', 1), 'not p and not q', ('s0', 1)), (('s1', 1), 'not p and q', ('s2', 1)), (('s4', 1), 'True', ('s4', 1)), (('s1', 1), 'p', ('s3', 1)), (('s1', 2), 'not p and q', ('s2', 2)), (('s2', 2), 'not p and not q', ('s0', 2)), (('s2', 2), 'not p and q', ('s2', 2)), (('s1', 2), 'not q', ('s1', 2)), (('s0', 2), 'not((not p and q) or (not p and not q) or (p and not q))', ('___qfinal___', 2)), (('s0', 1), 'not p and not q', ('s0', 1)), (('s2', 1), 'q', ('s3', 1)), (('s2', 2), 'not((not p and q) or (not p and not q))', ('___qfinal___', 2)), (('s2', 1), 'not p and q', ('s2', 1)), (('s3', 1), 'q', ('s4', 1)), (('s0', 1), 'not p and q', ('s2', 1)), (('s0', 1), 'p and not q', ('s1', 1))},
          'q0': {('s0', 1), ('s0', 2)},
          'f': {('s0', 1), ('___qfinal___', 2), ('s3', 1)}}

safe, live = decompose(a)
# print(safe == a_safe) # True


# print(safe==a_safe)
# print(safe["sigma"]==a_safe["sigma"])
# print(safe["delta"]==a_safe["delta"])
# print(safe["q0"]==a_safe["q0"])
# print(safe["q"]==a_safe["q"])
# print(safe["f"]==a_safe["f"])

# print(live == a_live) # True
# print(live["sigma"]==a_live["sigma"])
# print(live["delta"]==a_live["delta"])
# print(live["q0"]==a_live["q0"])
# print(live["q"]==a_live["q"])
# print(live["f"]==a_live["f"])
# print(len(live["delta"]))
# print(len(a_live["delta"]))
# print(live["delta"])
# print(a_live["delta"])
# print(safe)
# print(live)
# print("diff")
# print(live["delta"].difference(a_live["delta"]))
# print(a_live["delta"].difference(live["delta"]))
