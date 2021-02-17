
from itertools import product
from re import findall

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
				i.add((s0,delta[2]))

	def L(tup):
		return tup[1]
	
	TSxA['Act'] = ts['Act']
	TSxA['AP'] = a['q']
	TSxA['L'] = L
	TSxA['I'] = i
	TSxA['to'] = set()
	
	bfsCreateTo(TSxA, ts, a)

	return TSxA


# # Transition System
# ts = {'S': {'s0', 's1', 's2', 's3', 's5', 's4'},
#       'Act': {'beta', 'alpha', 'gamma'},
#       'to': {('s5', 'alpha', 's2'), ('s3', 'gamma', 's1'), ('s5', 'beta', 's1'), ('s1', 'alpha', 's4'), ('s4', 'gamma', 's1'), ('s0', 'alpha', 's3'), ('s4', 'beta', 's5'), ('s2', 'gamma', 's1'), ('s0', 'beta', 's1')}, 
# 	  'I': {'s0'},
#       'AP': {'b', 'c', 'a'},
#       'L': lambda s: {'s0': {'a', 'b'}, 's1': {'a', 'b', 'c'}, 's2': {'b', 'c'}, 's3': {'a', 'c'}, 's4': {'a', 'c'}, 's5': {'a', 'c'}}[s]}

# # NBA
# a = {'q': {'q3', 'q2', 'q0', 'q1'},
#      'sigma': {'a', 'b and not c', 'not(b and not c) and not a', 'b and not c and not a', '(a or b) and not c', 'c', 'not(b and not c)', 'not(a or b) and not c'},
#      'delta': {('q1', 'b and not c and not a', 'q1'), ('q2', 'c', 'q0'), ('q1', 'a', 'q2'), ('q0', 'not(b and not c)', 'q0'), ('q1', 'not(b and not c) and not a', 'q0'), ('q0', 'b and not c', 'q1'), ('q2', '(a or b) and not c', 'q3'), ('q2', 'not(a or b) and not c', 'q2')},
#      'q0': {'q0'},
#      'f': {'q3'}}

# # TS x A
# tsXa = {'S': {('s2', 'q0'), ('s0', 'q1'), ('s1', 'q0'), ('s1', 'q2'), ('s5', 'q0'), ('s3', 'q2'), ('s4', 'q0')},
#         'Act': {'beta', 'alpha', 'gamma'},
#         'to': {(('s1', 'q2'), 'alpha', ('s4', 'q0')), (('s5', 'q0'), 'alpha', ('s2', 'q0')), (('s1', 'q0'), 'alpha', ('s4', 'q0')), (('s2', 'q0'), 'gamma', ('s1', 'q0')), (('s4', 'q0'), 'beta', ('s5', 'q0')), (('s3', 'q2'), 'gamma', ('s1', 'q0')), (('s0', 'q1'), 'alpha', ('s3', 'q2')), (('s4', 'q0'), 'gamma', ('s1', 'q0')), (('s5', 'q0'), 'beta', ('s1', 'q0')), (('s0', 'q1'), 'beta', ('s1', 'q2'))},
#         'I': {('s0', 'q1')},
#         'AP': {'q3', 'q1', 'q2', 'q0'},
#         'L': lambda s: s[1]}

# print(transition_system_nba_product(ts, a)['S'])

# if tsXa == transition_system_nba_product(ts, a):
# 	print('success')


# if tsXa['S'] == transition_system_nba_product(ts, a)['S']:
# 	print('S')

# if tsXa['Act'] == transition_system_nba_product(ts, a)['Act']:
# 	print('Act')

# if tsXa['to'] == transition_system_nba_product(ts, a)['to']:
# 	print('to')

# if tsXa['I'] == transition_system_nba_product(ts, a)['I']:
# 	print('I')

# if tsXa['AP'] == transition_system_nba_product(ts, a)['AP']:
# 	print('AP')
