from hw5 import interleave_transition_systems, interleave_program_graphs
#from ts_from_pg import transitionSystemFromProgramGraph


class hashabledict(dict):
    def __hash__(self):
        return hash(frozenset(self.items()))


TS1 = {
    'S': {'l1', 'l2', 'l3'},
    'I': {'l1'},
    'Act': {'a', 'b'},
    'to': {('l1', 'a', 'l2'), ('l1', 'b', 'l3'), ('l3', 'a', 'l1')},
    'AP': {'first'},
    'L': lambda s: {'first'}
}

TS2 = {
    'S': {'q1', 'q2'},
    'I': {'q1'},
    'Act': {'a', 'b'},
    'to': {('q1', 'a', 'q2'), ('q2', 'b', 'q1')},
    'AP': {'second'},
    'L': lambda s: {'second'}
}

TS_INTERLEAVED1 = {
    'S': {('l1', 'q1'), ('l1', 'q2'), ('l3', 'q1'), ('l3', 'q2'), ('l2', 'q1'), ('l2', 'q2')},
    'I': {('l1', 'q1')},
    'Act': {'a', 'b'},
    'to': {(('l1', 'q1'), 'b', ('l3', 'q1')), (('l1', 'q1'), 'a', ('l1', 'q2')), (('l1', 'q1'), 'a', ('l2', 'q1')),
           (('l1', 'q2'), 'b', ('l1', 'q1')), (('l1', 'q2'), 'a', ('l2', 'q2')), (('l2', 'q1'), 'a', ('l2', 'q2')),
           (('l3', 'q1'), 'a', ('l3', 'q2')), (('l3', 'q1'), 'a', ('l1', 'q1')), (('l2', 'q2'), 'b', ('l2', 'q1')),
           (('l3', 'q2'), 'a', ('l1', 'q2')), (('l3', 'q2'), 'b', ('l3', 'q1')), (('l1', 'q2'), 'b', ('l3', 'q2'))},
    'AP': {'second', 'first'},
    'L': {('l1', 'q1'): {'second', 'first'}, ('l1', 'q2'): {'second', 'first'},
          ('l3', 'q1'): {'second', 'first'}, ('l3', 'q2'): {'second', 'first'},
          ('l2', 'q1'): {'second', 'first'}, ('l2', 'q2'): {'second', 'first'}},
}

TS3 = {
    'S': {'s1', 's2', 's3'},
    'I': {'s1'},
    'Act': {'a', 'b'},
    'to': {('s1', 'a', 's2'), ('s1', 'b', 's3')},
    'AP': {'s1', 's2', 's3'},
    'L': lambda s: {s}
}

TS4 = {
    'S': {'t1', 't2'},
    'I': {'t1'},
    'Act': {'c'},
    'to': {('t1', 'c', 't2')},
    'AP': {'t1', 't2'},
    'L': lambda s: {s}
}

TS_INTERLEAVED2 = {
    'S': {('s1', 't1'), ('s1', 't2'),
          ('s2', 't1'), ('s2', 't2'),
          ('s3', 't1'), ('s3', 't2')},
    'I': {('s1', 't1')},
    'Act': {'a', 'b', 'c'},
    'to': {(('s1', 't1'), 'a', ('s2', 't1')), (('s1', 't1'), 'b', ('s3', 't1')), (('s1', 't1'), 'c', ('s1', 't2')),
           (('s2', 't1'), 'c', ('s2', 't2')), (('s3', 't1'), 'c', ('s3', 't2')), (('s1', 't2'), 'a', ('s2', 't2')),
           (('s1', 't2'), 'b', ('s3', 't2'))},
    'AP': {'s1', 's2', 's3', 't1', 't2'},
    'L': {('s1', 't1'): {'s1', 't1'}, ('s1', 't2'): {'s1', 't2'},
          ('s2', 't1'): {'s2', 't1'}, ('s2', 't2'): {'s2', 't2'},
          ('s3', 't1'): {'s3', 't1'}, ('s3', 't2'): {'s3', 't2'}},
}

TS_HANDSHAKE1 = {'S': {'s1', 's3', 's2'},
                 'Act': {'b', 'd', 'a'},
                 'to': {('s2', 'd', 's3'), ('s1', 'a', 's2'), ('s2', 'b', 's1')},
                 'I': {'s1'}, 'AP': {'b', 'a'},
                 'L': lambda s: {s}}

TS_HANDSHAKE2 = {'S': {'s4', 's5'},
                 'Act': {'b', 'a', 'c'},
                 'to': {('s4', 'a', 's5'), ('s5', 'b', 's5'), ('s5', 'c', 's4')},
                 'I': {'s4'}, 'AP': {'b', 'a'},
                 'L': lambda s: {s}}

TS_HANDSHAKE_INTERLEAVED = {'S': {('s1', 's4'), ('s1', 's5'), ('s3', 's4'), ('s2', 's4'), ('s3', 's5'), ('s2', 's5')},
                            'Act': {'a', 'b', 'c', 'd'},
                            'to': {(('s2', 's5'), 'c', ('s2', 's4')), (('s1', 's5'), 'c', ('s1', 's4')),
                                   (('s1', 's4'), 'a', ('s2', 's5')), ((
                                       's2', 's4'), 'd', ('s3', 's4')),
                                   (('s2', 's5'), 'd', ('s3', 's5')), ((
                                       's3', 's5'), 'c', ('s3', 's4')),
                                   (('s2', 's5'), 'b', ('s1', 's5'))},
                            'I': {('s1', 's4')}, 'AP': {'b', 'a'},
                            'L': {('s1', 's4'): {'s1', 's4'},
                                  ('s1', 's5'): {'s1', 's5'},
                                  ('s3', 's4'): {'s3', 's4'},
                                  ('s2', 's4'): {'s2', 's4'},
                                  ('s3', 's5'): {'s3', 's5'},
                                  ('s2', 's5'): {'s2', 's5'}}
                            }

TS_NON_REACH1 = {'S': {'s1', 's3', 's2'},
                 'Act': {'b', 'd', 'a'},
                 'to': {('s1', 'a', 's2'), ('s2', 'b', 's1'), ('s3', 'd', 's2')},
                 'I': {'s1'}, 'AP': {'b', 'a'},
                 'L': lambda s: {s}}

TS_NON_REACH2 = {'S': {'s4', 's5'},
                 'Act': {'b', 'a', 'c'},
                 'to': {('s4', 'a', 's5'), ('s5', 'b', 's5'), ('s5', 'c', 's4')},
                 'I': {'s4'}, 'AP': {'b', 'a'},
                 'L': lambda s: {s}}

TS_NON_REACH_INTERLEAVED = {'S': {('s2', 's4'), ('s1', 's5'), ('s2', 's5'), ('s1', 's4')},
                            'I': {('s1', 's4')}, 'Act': {'b', 'c', 'd', 'a'},
                            'to': {(('s1', 's4'), 'a', ('s1', 's5')), (('s2', 's5'), 'b', ('s2', 's5')),
                                   (('s2', 's5'), 'c', ('s2', 's4')), ((
                                       's2', 's4'), 'b', ('s1', 's4')),
                                   (('s1', 's4'), 'a', ('s2', 's4')), ((
                                       's1', 's5'), 'b', ('s1', 's5')),
                                   (('s1', 's5'), 'c', ('s1', 's4')), ((
                                       's2', 's4'), 'a', ('s2', 's5')),
                                   (('s1', 's5'), 'a', ('s2', 's5')), (('s2', 's5'), 'b', ('s1', 's5'))},
                            'AP': {'a', 'b'},
                            'L': {('s1', 's4'): {'s1', 's4'},
                                  ('s1', 's5'): {'s1', 's5'},
                                  ('s2', 's4'): {'s2', 's4'},
                                  ('s2', 's5'): {'s2', 's5'}}
                            }


def compare_ts(generated_ts, real_ts):
    return all([generated_ts[key] == real_ts[key] for key in generated_ts if key != 'L'])


def compare_labels(generated_ts, real_ts):
    return all([generated_ts['L'](state) == real_ts['L'][state] for state in generated_ts['S']])


print("-- TESTING TRANSITION SYSTEM INTERLEAVING --")

assert compare_ts(interleave_transition_systems(
    TS1, TS2, set()), TS_INTERLEAVED1)
assert compare_labels(interleave_transition_systems(
    TS1, TS2, set()), TS_INTERLEAVED1)

assert compare_ts(interleave_transition_systems(
    TS3, TS4, set()), TS_INTERLEAVED2)
assert compare_labels(interleave_transition_systems(
    TS3, TS4, set()), TS_INTERLEAVED2)

assert compare_ts(interleave_transition_systems(
    TS_HANDSHAKE1, TS_HANDSHAKE2, {'a', 'b'}), TS_HANDSHAKE_INTERLEAVED)
assert compare_labels(interleave_transition_systems(
    TS_HANDSHAKE1, TS_HANDSHAKE2, {'a', 'b'}), TS_HANDSHAKE_INTERLEAVED)

assert compare_ts(interleave_transition_systems(
    TS_NON_REACH1, TS_NON_REACH2, set()), TS_NON_REACH_INTERLEAVED)
assert compare_labels(interleave_transition_systems(
    TS_NON_REACH1, TS_NON_REACH2, set()), TS_NON_REACH_INTERLEAVED)

print("PASSED\n")


def effect(act, eta):
    eta = hashabledict(eta)
    exec(act, None, eta)
    return eta


def evaluate(cond, eta):
    return eval(cond, None, eta)


peterson0 = {'Loc': {'crit', 'noncrit', 'wait'},
             'Act': {'', 'b0=True;x=1', 'b0=False'},
             'Eval': evaluate,
             'Effect': effect,
             'to': {('noncrit', 'True', 'b0=True;x=1', 'wait'), ('wait', 'x==0 or not b1', '', 'crit'), ('crit', 'True', 'b0=False', 'noncrit')},
             'Loc0': {'noncrit'},
             'g0': 'not b0'}


peterson1 = {'Loc': {'crit', 'noncrit', 'wait'},
             'Act': {'', 'b1=True;x=0', 'b1=False'},
             'Eval': evaluate,
             'Effect': effect,
             'to': {('noncrit', 'True', 'b1=True;x=0', 'wait'), ('crit', 'True', 'b1=False', 'noncrit'), ('wait', 'x==1 or not b0', '', 'crit')},
             'Loc0': {'noncrit'},
             'g0': 'not b1'}

interleaved_peterson = {'Loc': {('crit', 'noncrit'), ('wait', 'noncrit'), ('noncrit', 'crit'), ('noncrit', 'wait'), ('crit', 'crit'), ('crit', 'wait'), ('wait', 'crit'), ('wait', 'wait'), ('noncrit', 'noncrit')},
                        'Act': {'', 'b0=False', 'b1=True;x=0', 'b0=True;x=1', 'b1=False'},
                        'to': {(('crit', 'crit'), 'True', 'b1=False', ('crit', 'noncrit')), (('crit', 'noncrit'), 'True', 'b0=False', ('noncrit', 'noncrit')),
                               (('wait', 'noncrit'), 'x==0 or not b1', '', ('crit', 'noncrit')
                                ), (('wait', 'crit'), 'x==0 or not b1', '', ('crit', 'crit')),
                               (('crit', 'wait'), 'x==1 or not b0', '', ('crit', 'crit')), ((
                                   'crit', 'wait'), 'True', 'b0=False', ('noncrit', 'wait')),
                               (('wait', 'noncrit'), 'True', 'b1=True;x=0', ('wait', 'wait')
                                ), (('wait', 'wait'), 'x==1 or not b0', '', ('wait', 'crit')),
                               (('noncrit', 'crit'), 'True', 'b0=True;x=1', ('wait', 'crit')
                                ), (('wait', 'crit'), 'True', 'b1=False', ('wait', 'noncrit')),
                               (('wait', 'wait'), 'x==0 or not b1', '', ('crit', 'wait')), ((
                                   'noncrit', 'noncrit'), 'True', 'b0=True;x=1', ('wait', 'noncrit')),
                               (('crit', 'noncrit'), 'True', 'b1=True;x=0', ('crit', 'wait')
                                ), (('crit', 'crit'), 'True', 'b0=False', ('noncrit', 'crit')),
                               (('noncrit', 'wait'), 'True', 'b0=True;x=1', ('wait', 'wait')), ((
                                   'noncrit', 'wait'), 'x==1 or not b0', '', ('noncrit', 'crit')),
                               (('noncrit', 'noncrit'), 'True', 'b1=True;x=0', ('noncrit', 'wait')), (('noncrit', 'crit'), 'True', 'b1=False', ('noncrit', 'noncrit'))},
                        'Loc0': {('noncrit', 'noncrit')},
                        'g0': 'not b0 and not b1'}

ts_interleaved_peterson = {'S': {(('wait', 'crit'), hashabledict({'x': 1, 'b0': True, 'b1': True})),
                                 (('wait', 'noncrit'), hashabledict(
                                     {'x': 1, 'b0': True, 'b1': False})),
                                 (('noncrit', 'noncrit'), hashabledict(
                                     {'x': 0, 'b0': False, 'b1': False})),
                                 (('wait', 'wait'), hashabledict(
                                     {'x': 1, 'b0': True, 'b1': True})),
                                 (('crit', 'noncrit'), hashabledict(
                                     {'x': 1, 'b0': True, 'b1': False})),
                                 (('wait', 'wait'), hashabledict(
                                     {'x': 0, 'b0': True, 'b1': True})),
                                 (('noncrit', 'crit'), hashabledict(
                                     {'x': 0, 'b0': False, 'b1': True})),
                                 (('noncrit', 'noncrit'), hashabledict(
                                     {'x': 1, 'b0': False, 'b1': False})),
                                 (('noncrit', 'wait'), hashabledict(
                                     {'x': 0, 'b0': False, 'b1': True})),
                                 (('crit', 'wait'), hashabledict({'x': 0, 'b0': True, 'b1': True}))},
                           'Act': {'', 'b0=False', 'b1=True;x=0', 'b0=True;x=1', 'b1=False'},
                           'to': {((('wait', 'noncrit'), hashabledict({'x': 1, 'b0': True, 'b1': False})), '', (('crit', 'noncrit'), hashabledict({'x': 1, 'b0': True, 'b1': False}))),
                                  ((('noncrit', 'wait'), hashabledict({'x': 0, 'b0': False, 'b1': True})),
                                   'b0=True;x=1', (('wait', 'wait'), hashabledict({'x': 1, 'b0': True, 'b1': True}))),
                                  ((('noncrit', 'noncrit'), hashabledict({'x': 1, 'b0': False, 'b1': False})),
                                   'b0=True;x=1', (('wait', 'noncrit'), hashabledict({'x': 1, 'b0': True, 'b1': False}))),
                                  ((('crit', 'noncrit'), hashabledict({'x': 1, 'b0': True, 'b1': False})),
                                   'b1=True;x=0', (('crit', 'wait'), hashabledict({'x': 0, 'b0': True, 'b1': True}))),
                                  ((('crit', 'noncrit'), hashabledict({'x': 1, 'b0': True, 'b1': False})), 'b0=False',
                                   (('noncrit', 'noncrit'), hashabledict({'x': 1, 'b0': False, 'b1': False}))),
                                  ((('noncrit', 'noncrit'), hashabledict({'x': 0, 'b0': False, 'b1': False})),
                                   'b0=True;x=1', (('wait', 'noncrit'), hashabledict({'x': 1, 'b0': True, 'b1': False}))),
                                  ((('wait', 'wait'), hashabledict({'x': 1, 'b0': True, 'b1': True})), '',
                                   (('wait', 'crit'), hashabledict({'x': 1, 'b0': True, 'b1': True}))),
                                  ((('noncrit', 'crit'), hashabledict({'x': 0, 'b0': False, 'b1': True})),
                                   'b0=True;x=1', (('wait', 'crit'), hashabledict({'x': 1, 'b0': True, 'b1': True}))),
                                  ((('wait', 'noncrit'), hashabledict({'x': 1, 'b0': True, 'b1': False})),
                                   'b1=True;x=0', (('wait', 'wait'), hashabledict({'x': 0, 'b0': True, 'b1': True}))),
                                  ((('wait', 'wait'), hashabledict({'x': 0, 'b0': True, 'b1': True})), '',
                                   (('crit', 'wait'), hashabledict({'x': 0, 'b0': True, 'b1': True}))),
                                  ((('noncrit', 'noncrit'), hashabledict({'x': 0, 'b0': False, 'b1': False})),
                                   'b1=True;x=0', (('noncrit', 'wait'), hashabledict({'x': 0, 'b0': False, 'b1': True}))),
                                  ((('noncrit', 'noncrit'), hashabledict({'x': 1, 'b0': False, 'b1': False})),
                                   'b1=True;x=0', (('noncrit', 'wait'), hashabledict({'x': 0, 'b0': False, 'b1': True}))),
                                  ((('noncrit', 'crit'), hashabledict({'x': 0, 'b0': False, 'b1': True})), 'b1=False',
                                   (('noncrit', 'noncrit'), hashabledict({'x': 0, 'b0': False, 'b1': False}))),
                                  ((('noncrit', 'wait'), hashabledict({'x': 0, 'b0': False, 'b1': True})), '',
                                   (('noncrit', 'crit'), hashabledict({'x': 0, 'b0': False, 'b1': True}))),
                                  ((('crit', 'wait'), hashabledict({'x': 0, 'b0': True, 'b1': True})), 'b0=False',
                                   (('noncrit', 'wait'), hashabledict({'x': 0, 'b0': False, 'b1': True}))),
                                  ((('wait', 'crit'), hashabledict({'x': 1, 'b0': True, 'b1': True})), 'b1=False', (('wait', 'noncrit'), hashabledict(hashabledict({'x': 1, 'b0': True, 'b1': False}))))},
                           'I': {
    (('noncrit', 'noncrit'), hashabledict({'x': 0, 'b0': False, 'b1': False})),
    (('noncrit', 'noncrit'), hashabledict({'x': 1, 'b0': False, 'b1': False})),
},
    'AP': {('crit', 'noncrit'), ('wait', 'noncrit'), ('noncrit', 'crit'), ('noncrit', 'wait'), ('crit', 'crit'), ('crit', 'wait'), ('wait', 'crit'), ('wait', 'wait'), ('noncrit', 'noncrit')}, }


pg1 = {'Loc': {'l1', 'l2'},
       'Act': {'x = x + 1'},
       'Eval': evaluate,
       'Effect': effect,
       'to': {('l1', 'True', 'x = x + 1', 'l2')},
       'Loc0': {'l1'},
       'g0': 'x == 3'}


pg2 = {'Loc': {'l1', 'l2'},
       'Act': {'x = 2 * x'},
       'Eval': evaluate,
       'Effect': effect,
       'to': {('l1', 'True', 'x = 2 * x', 'l2')},
       'Loc0': {'l1'},
       'g0': 'x == 3'}

pg1_2_interleaved = {'Loc': {('l2', 'l1'), ('l1', 'l2'), ('l2', 'l2'), ('l1', 'l1')}, 'Loc0': {('l1', 'l1')},
                     'Act': {'x = 2 * x', 'x = x + 1'},
                     'to': {(('l2', 'l1'), 'True', 'x = 2 * x', ('l2', 'l2')),
                            (('l1', 'l1'), 'True', 'x = x + 1', ('l2', 'l1')),
                            (('l1', 'l2'), 'True', 'x = x + 1', ('l2', 'l2')),
                            (('l1', 'l1'), 'True', 'x = 2 * x', ('l1', 'l2'))},
                     'g0': 'x == 3 and x == 3'}

ts1_2_interleaved = {'S': {(('l2', 'l2'), hashabledict({'x': 8})), (('l2', 'l1'), hashabledict({'x': 4})),
                           (('l1', 'l1'), hashabledict({'x': 3})), ((
                               'l2', 'l2'), hashabledict({'x': 7})),
                           (('l1', 'l2'), hashabledict({'x': 6}))},
                     'I': {(('l1', 'l1'), hashabledict({'x': 3}))},
                     'Act': {'x = 2 * x', 'x = x + 1'},
                     'to': {((('l1', 'l1'), hashabledict({'x': 3})), 'x = 2 * x', (('l1', 'l2'), hashabledict({'x': 6}))),
                            ((('l1', 'l2'), hashabledict({'x': 6})), 'x = x + 1',
                             (('l2', 'l2'), hashabledict({'x': 7}))),
                            ((('l2', 'l1'), hashabledict({'x': 4})), 'x = 2 * x',
                             (('l2', 'l2'), hashabledict({'x': 8}))),
                            ((('l1', 'l1'), hashabledict({'x': 3})), 'x = x + 1', (('l2', 'l1'), hashabledict({'x': 4})))},
                     'AP': {('l2', 'l2'), ('l1', 'l1'), ('l1', 'l2'), ('l2', 'l1')}}


def compare_pg(generated_ts, real_ts):
    return all([generated_ts[key] == real_ts[key] for key in generated_ts if key != 'Eval' and key != 'Effect'])


print("-- TESTING TRANSITION SYSTEM INTERLEAVING --")

assert compare_pg(interleave_program_graphs(
    peterson0, peterson1), interleaved_peterson)
assert compare_ts(transitionSystemFromProgramGraph(interleave_program_graphs(peterson0, peterson1),
                                                   vars={'x': range(2), 'b0': {True, False}, 'b1': {True, False}}, labels=set()), ts_interleaved_peterson)

assert compare_pg(interleave_program_graphs(pg1, pg2), pg1_2_interleaved)
assert compare_ts(transitionSystemFromProgramGraph(interleave_program_graphs(pg1, pg2),
                                                   vars={'x': range(3, 9)}, labels=set()), ts1_2_interleaved)

print("PASSED\n")
