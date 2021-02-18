from bonus import transition_system_nba_product, gnba_to_nba

test0 = {'q': {'q2', 'q1', 'q0'},
         'sigma': {'true', 'not a', 'a'},
         'delta': {('q1', 'a', 'q0'), ('q1', 'not a', 'q2'), ('q0', 'true', 'q1'), ('q1', 'true', 'q1'),
                   ('q2', 'true', 'q1')},
         'q0': {'q1'},
         'f': [{'q0'}, {'q2'}]
         }
res0 = {'q': {('q2', 2), ('q0', 2), ('q2', 1), ('q1', 1), ('q0', 1), ('q1', 2)},
        'sigma': {'a', 'true', 'not a'},
        'delta': {(('q1', 2), 'a', ('q0', 2)), (('q0', 1), 'true', ('q1', 2)), (('q1', 1), 'a', ('q0', 1)),
                  (('q2', 2), 'true', ('q1', 1)), (('q1', 1), 'not a', ('q2', 1)), (('q0', 2), 'true', ('q1', 2)),
                  (('q1', 1), 'true', ('q1', 1)),
                  (('q2', 1), 'true', ('q1', 1)), (('q1', 2), 'not a', ('q2', 2)), (('q1', 2), 'true', ('q1', 2))},
        'q0': {('q1', 1)},
        'f': {('q0', 1)}}

test1 = {
    'q': {f'q{i}' for i in range(3)},
    'sigma': {'crit1', 'crit2', 'true'},
    'delta': {('q0', 'true', 'q0'), ('q0', 'crit2', 'q2'), ('q0', 'crit1', 'q1'), ('q1', 'true', 'q0'),
              ('q2', 'true', 'q0')},
    'q0': {'q0'},
    'f': [{'q1'}, {'q2'}]
}

res1 = {'q': {('q0', 2), ('q2', 1), ('q0', 1), ('q1', 2), ('q2', 2), ('q1', 1)}, 'sigma': {'crit2', 'crit1', 'true'},
        'delta': {(('q2', 1), 'true', ('q0', 1)), (('q1', 1), 'true', ('q0', 2)), (('q2', 2), 'true', ('q0', 1)),
                  (('q0', 2), 'true', ('q0', 2)), (('q0', 1), 'crit2', ('q2', 1)), (('q0', 1), 'true', ('q0', 1)),
                  (('q0', 2), 'crit1', ('q1', 2)), (('q1', 2), 'true', ('q0', 2)), (('q0', 1), 'crit1', ('q1', 1)),
                  (('q0', 2), 'crit2', ('q2', 2))}, 'q0': {('q0', 1)}, 'f': {('q1', 1)}}

test2 = {
    'q': {f's{i}' for i in range(6)},
    'sigma': {'a', 'b', 'a and b', 'true'},
    'delta': {('s1', 'a', 's1'), ('s1', 'a and b', 's2'), ('s2', 'a and b', 's5'), ('s5', 'a', 's5'),
              ('s3', 'true', 's3'), ('s3', 'a', 's1'), ('s3', 'a and b', 's2'), ('s3', 'b', 's0'),
              ('s0', 'a and b', 's5'), ('s0', 'b', 's4'), ('s4', 'a', 's5'), ('s4', 'true', 's4')},
    'q0': {'s3'},
    'f': [{'s0', 's2', 's4', 's5'}, {'s1', 's2', 's5'}]

}

res3 = {
    'q': {('s3', 2), ('s1', 1), ('s5', 1), ('s3', 1), ('s2', 2), ('s1', 2), ('s4', 2), ('s4', 1), ('s5', 2), ('s2', 1),
          ('s0', 2), ('s0', 1)}, 'sigma': {'a and b', 'a', 'b', 'true'},
    'delta': {(('s2', 1), 'a and b', ('s5', 2)), (('s3', 1), 'true', ('s3', 1)), (('s5', 2), 'a', ('s5', 1)),
              (('s4', 1), 'true', ('s4', 2)), (('s3', 2), 'a and b', ('s2', 2)), (('s1', 2), 'a', ('s1', 1)),
              (('s0', 1), 'a and b', ('s5', 2)), (('s1', 1), 'a', ('s1', 1)), (('s3', 1), 'a and b', ('s2', 1)),
              (('s3', 2), 'b', ('s0', 2)), (('s3', 1), 'a', ('s1', 1)), (('s1', 1), 'a and b', ('s2', 1)),
              (('s3', 1), 'b', ('s0', 1)), (('s3', 2), 'a', ('s1', 2)), (('s4', 2), 'true', ('s4', 2)),
              (('s3', 2), 'true', ('s3', 2)), (('s0', 2), 'b', ('s4', 2)), (('s5', 1), 'a', ('s5', 2)),
              (('s0', 2), 'a and b', ('s5', 2)), (('s4', 2), 'a', ('s5', 2)), (('s2', 2), 'a and b', ('s5', 1)),
              (('s1', 2), 'a and b', ('s2', 1)), (('s0', 1), 'b', ('s4', 2)), (('s4', 1), 'a', ('s5', 2))},
    'q0': {('s3', 1)}, 'f': {('s4', 1), ('s2', 1), ('s5', 1), ('s0', 1)}}

# Transition System
ts_test4 = {'S': {'s0', 's1', 's2', 's3', 's5', 's4'},
            'Act': {'beta', 'alpha', 'gamma'},
            'to': {('s5', 'alpha', 's2'), ('s3', 'gamma', 's1'), ('s5', 'beta', 's1'), ('s1', 'alpha', 's4'),
                   ('s4', 'gamma', 's1'), ('s0', 'alpha', 's3'), ('s4', 'beta', 's5'), ('s2', 'gamma', 's1'),
                   ('s0', 'beta', 's1')}, 'I': {'s0'},
            'AP': {'b', 'c', 'a'},
            'L': lambda s:
            {'s0': {'a', 'b'}, 's1': {'a', 'b', 'c'}, 's2': {'b', 'c'}, 's3': {'a', 'c'}, 's4': {'a', 'c'},
             's5': {'a', 'c'}}[
                s]}

# NBA
a_test4 = {'q': {'q3', 'q2', 'q0', 'q1'},
           'sigma': {'a', 'b and not c', 'not(b and not c) and not a', 'b and not c and not a', '(a or b) and not c',
                     'c',
                     'not(b and not c)', 'not(a or b) and not c'},
           'delta': {('q1', 'b and not c and not a', 'q1'), ('q2', 'c', 'q0'), ('q1', 'a', 'q2'),
                     ('q0', 'not(b and not c)', 'q0'), ('q1', 'not(b and not c) and not a', 'q0'),
                     ('q0', 'b and not c', 'q1'), ('q2', '(a or b) and not c', 'q3'),
                     ('q2', 'not(a or b) and not c', 'q2')},
           'q0': {'q0'},
           'f': {'q3'}}

# TS x A
tsXa_test4 = {'S': {('s2', 'q0'), ('s0', 'q1'), ('s1', 'q0'), ('s1', 'q2'), ('s5', 'q0'), ('s3', 'q2'), ('s4', 'q0')},
              'Act': {'beta', 'alpha', 'gamma'},
              'to': {(('s1', 'q2'), 'alpha', ('s4', 'q0')), (('s5', 'q0'), 'alpha', ('s2', 'q0')),
                     (('s1', 'q0'), 'alpha', ('s4', 'q0')), (('s2', 'q0'), 'gamma', ('s1', 'q0')),
                     (('s4', 'q0'), 'beta', ('s5', 'q0')), (('s3', 'q2'), 'gamma', ('s1', 'q0')),
                     (('s0', 'q1'), 'alpha', ('s3', 'q2')), (('s4', 'q0'), 'gamma', ('s1', 'q0')),
                     (('s5', 'q0'), 'beta', ('s1', 'q0')), (('s0', 'q1'), 'beta', ('s1', 'q2'))},
              'I': {('s0', 'q1')},
              'AP': {'q3', 'q1', 'q2', 'q0'},
              'L': lambda s: s[1]}

ts_test5 = {'S': {'s0', 's1', 's2'},
            'Act': {'true'},
            'to': {('s0', 'true', 's1'), ('s1', 'true', 's0'), ('s1', 'true', 's2'), ('s2', 'true', 's0'),
                   ('s2', 'true', 's1')}, 'I': {'s0'},
            'AP': {'r'},
            'L': lambda s:
            {'s0': set(), 's1': {'r'}, 's2': set()}[
                s]}

# NBA
a_test5 = {'q': {'q3', 'q2', 'q0', 'q1'},
           'sigma': {'r', 'not r', 'true'},
           'delta': {('q0', 'r', 'q0'), ('q0', 'not r', 'q1'), ('q1', 'not r', 'q2'), ('q1', 'r', 'q0'),
                     ('q2', 'r', 'q0'), ('q2', 'not r', 'q3'), ('q3', 'true', 'q3')},
           'q0': {'q0'},
           'f': {'q3'}}

tsXa_test5 = {'S': {('s2', 'q1'), ('s1', 'q0'), ('s0', 'q1'), ('s0', 'q2')}, 'Act': {'true'},
              'to': {(('s2', 'q1'), 'true', ('s1', 'q0')), (('s2', 'q1'), 'true', ('s0', 'q2')),
                     (('s0', 'q2'), 'true', ('s1', 'q0')), (('s0', 'q1'), 'true', ('s1', 'q0')),
                     (('s1', 'q0'), 'true', ('s2', 'q1')), (('s1', 'q0'), 'true', ('s0', 'q1'))}, 'I': {('s0', 'q1')},
              'AP': {'q2', 'q3', 'q1', 'q0'}, 'L': lambda s: s[1]}


def compare_ts(ts1, ts2):
    return all(ts1[key] == ts2[key] for key in ts1 if key != 'L')


assert gnba_to_nba(test0) == res0
assert gnba_to_nba(test1) == res1
assert gnba_to_nba(test2) == res3
assert compare_ts(transition_system_nba_product(ts_test4, a_test4), tsXa_test4)
assert compare_ts(transition_system_nba_product(ts_test5, a_test5), tsXa_test5)
