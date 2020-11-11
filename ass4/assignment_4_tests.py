from hw4 import transitionSystemFromProgramGraph


# class Hashabledict(dict):
#     def __hash__(self):
#         return hash(frozenset(self.items()))
# Instead of a dictionary, use this ^.

def evaluate(cond, eta):
    return {
        'true': lambda eta: True,
        'ncoke > 0': lambda eta: eta['ncoke'] > 0,
        'nsprite > 0': lambda eta: eta['nsprite'] > 0,
        'ncoke=0 && nsprite=0': lambda eta: eta['ncoke'] == 0 and eta['nsprite'] == 0,
        'ncoke=2 && nsprite=2': lambda eta: eta['ncoke'] == 2 and eta['nsprite'] == 2,
    }[cond](eta)


def join_dicts(d1, d2):
    d1 = d1.copy()
    d1.update(d2)
    return d1


def effect(act, eta):
    return {
        'coin': lambda eta: eta,
        'ret_coin': lambda eta: eta,
        'refill': lambda eta: {'ncoke': 2, 'nsprite': 2},
        'get_coke': lambda eta: join_dicts(eta, {'ncoke': eta['ncoke'] - 1}),
        'get_sprite': lambda eta: join_dicts(eta, {'nsprite': eta['nsprite'] - 1}),
    }[act](eta)


def evaluate_test1(cond, eta):
    return {
        'true': lambda eta: True,
        'r == 0': lambda eta: eta['r'] == 0
    }[cond](eta)


def effect_test1(act, eta):
    return {
        'a0': lambda eta: join_dicts(eta, {'r': 0, 'y': eta['r']}),
        'a1': lambda eta: join_dicts(eta, {'r': 1, 'y': 1 - eta['r']})
    }[act](eta)


def evaluate_test2(cond, eta):
    return {
        'true': lambda eta: True,
        'x > z': lambda eta: eta['x'] > eta['z'],
        'x == 1 && y == 2 && z == 0': lambda eta: eta['x'] == 1 and eta['y'] == 2 and eta['z'] == 0
    }[cond](eta)


def effect_test2(act, eta):
    return {
        'x := (x+y)%5': lambda eta: join_dicts(eta, {'x': (eta['x'] + eta['y']) % 5}),
        'z := (z-y)%5': lambda eta: join_dicts(eta, {'z': (eta['z'] - eta['y']) % 5})
    }[act](eta)


def evaluate_collatz(cond, eta):
    return {
        'true': lambda eta: True,
        'x%2 == 0': lambda eta: (eta['x'] % 2) == 0,
        'x%2 == 1 && x != 1': lambda eta: (eta['x'] % 2) == 1 and eta['x'] != 1,
        'x == 6': lambda eta: eta['x'] == 6,
        'x == 1': lambda eta: eta['x'] == 1,
        'x == 27': lambda eta: eta['x'] == 27
    }[cond](eta)


def effect_collatz(act, eta):
    return {
        'x := x/2': lambda eta: join_dicts(eta, {'x': int(eta['x'] / 2)}),
        'x := 3x + 1': lambda eta: join_dicts(eta, {'x': 3 * eta['x'] + 1}),
        'nothing': lambda eta: eta
    }[act](eta)


def evaluate_test3(cond, eta):
    return {
        'true': lambda eta: True,
        'x == 0': lambda eta: eta['x'] == 0,
        'x != 0': lambda eta: eta['x'] != 0

    }[cond](eta)


def effect_test3(act, eta):
    return {
        'x := x + 1': lambda eta: join_dicts(eta, {'x': eta['x'] + 1})
    }[act](eta)


TEST3_PG = {
    'Loc': {'l1', 'l2'},
    'Loc0': {'l1'},
    'Act': {'x := x + 1'},
    'Eval': evaluate_test3,
    'Effect': effect_test3,
    'to': {
        ('l1', 'x != 0', 'x := x + 1', 'l2')
    },
    'g0': "x == 0"
}

TEST3_TS = {'S': [('l1', {'x': 0})], 'I': [('l1', {'x': 0})], 'Act': {'x := x + 1'}, 'to': [], 'AP': {'l1', 'l2'},
            'L': None}

COLLATZ_PG = {
    'Loc': {'l1', 'l2'},
    'Loc0': {'l1'},
    'Act': {'x := x/2', 'x := 3x + 1', 'nothing'},
    'Eval': evaluate_collatz,
    'Effect': effect_collatz,
    'to': {
        ('l1', 'x%2 == 0', 'x := x/2', 'l1'),
        ('l1', 'x%2 == 1 && x != 1', 'x := 3x + 1', 'l1'),
        ('l1', 'x == 1', 'nothing', 'l2')
    },
    'g0': "x == 6"
}

LONG_COLLATZ_PG = {
    'Loc': {'l1', 'l2'},
    'Loc0': {'l1'},
    'Act': {'x := x/2', 'x := 3x + 1', 'nothing'},
    'Eval': evaluate_collatz,
    'Effect': effect_collatz,
    'to': {
        ('l1', 'x%2 == 0', 'x := x/2', 'l1'),
        ('l1', 'x%2 == 1 && x != 1', 'x := 3x + 1', 'l1'),
        ('l1', 'x == 1', 'nothing', 'l2')
    },
    'g0': "x == 27"
}

LONG_COLLATZ_TS = {
    'S': [('l1', {'x': 27}), ('l1', {'x': 577}), ('l1', {'x': 251}), ('l1', {'x': 137}), ('l1', {'x': 3077}),
          ('l1', {'x': 700}), ('l1', {'x': 242}), ('l1', {'x': 2308}), ('l1', {'x': 5}), ('l1', {'x': 82}),
          ('l1', {'x': 1}), ('l1', {'x': 167}), ('l1', {'x': 40}), ('l1', {'x': 911}), ('l1', {'x': 206}),
          ('l1', {'x': 4102}), ('l1', {'x': 1132}), ('l1', {'x': 433}), ('l1', {'x': 3644}), ('l1', {'x': 71}),
          ('l1', {'x': 16}), ('l1', {'x': 3238}), ('l1', {'x': 244}), ('l1', {'x': 80}), ('l1', {'x': 566}),
          ('l1', {'x': 62}), ('l1', {'x': 488}), ('l1', {'x': 790}), ('l1', {'x': 1619}), ('l1', {'x': 8}),
          ('l1', {'x': 233}), ('l1', {'x': 310}), ('l1', {'x': 319}), ('l1', {'x': 2429}), ('l1', {'x': 31}),
          ('l1', {'x': 161}), ('l1', {'x': 502}), ('l1', {'x': 325}), ('l1', {'x': 650}), ('l1', {'x': 122}),
          ('l1', {'x': 124}), ('l1', {'x': 466}), ('l1', {'x': 2734}), ('l1', {'x': 23}), ('l1', {'x': 106}),
          ('l1', {'x': 850}), ('l1', {'x': 4}), ('l1', {'x': 593}), ('l1', {'x': 334}), ('l1', {'x': 4616}),
          ('l1', {'x': 10}), ('l1', {'x': 160}), ('l1', {'x': 47}), ('l1', {'x': 121}), ('l1', {'x': 445}),
          ('l1', {'x': 2}), ('l1', {'x': 479}), ('l1', {'x': 214}), ('l1', {'x': 350}), ('l1', {'x': 94}),
          ('l1', {'x': 175}), ('l1', {'x': 155}), ('l1', {'x': 1780}), ('l1', {'x': 1276}), ('l1', {'x': 1186}),
          ('l1', {'x': 142}), ('l1', {'x': 484}), ('l1', {'x': 41}), ('l1', {'x': 526}), ('l1', {'x': 103}),
          ('l1', {'x': 91}), ('l1', {'x': 425}), ('l1', {'x': 412}), ('l1', {'x': 668}), ('l1', {'x': 6154}),
          ('l1', {'x': 46}), ('l1', {'x': 1300}), ('l1', {'x': 1822}), ('l1', {'x': 92}), ('l1', {'x': 1438}),
          ('l1', {'x': 4858}), ('l1', {'x': 7288}), ('l1', {'x': 377}), ('l1', {'x': 719}), ('l1', {'x': 958}),
          ('l1', {'x': 866}), ('l1', {'x': 184}), ('l1', {'x': 20}), ('l1', {'x': 364}), ('l1', {'x': 2051}),
          ('l1', {'x': 322}), ('l1', {'x': 61}), ('l1', {'x': 70}), ('l1', {'x': 890}), ('l1', {'x': 395}),
          ('l1', {'x': 1732}), ('l1', {'x': 1154}), ('l1', {'x': 107}), ('l1', {'x': 2158}), ('l1', {'x': 638}),
          ('l1', {'x': 976}), ('l2', {'x': 1}), ('l1', {'x': 754}), ('l1', {'x': 1079}), ('l1', {'x': 9232}),
          ('l1', {'x': 35}), ('l1', {'x': 274}), ('l1', {'x': 283}), ('l1', {'x': 182}), ('l1', {'x': 263}),
          ('l1', {'x': 1367}), ('l1', {'x': 1336}), ('l1', {'x': 53})], 'I': [('l1', {'x': 27})],
    'Act': {'nothing', 'x := x/2', 'x := 3x + 1'},
    'to': [(('l1', {'x': 433}), 'x := 3x + 1', ('l1', {'x': 1300})), (('l1', {'x': 20}), 'x := x/2', ('l1', {'x': 10})),
           (('l1', {'x': 80}), 'x := x/2', ('l1', {'x': 40})), (('l1', {'x': 577}), 'x := 3x + 1', ('l1', {'x': 1732})),
           (('l1', {'x': 4616}), 'x := x/2', ('l1', {'x': 2308})),
           (('l1', {'x': 23}), 'x := 3x + 1', ('l1', {'x': 70})),
           (('l1', {'x': 4858}), 'x := x/2', ('l1', {'x': 2429})),
           (('l1', {'x': 233}), 'x := 3x + 1', ('l1', {'x': 700})), (('l1', {'x': 46}), 'x := x/2', ('l1', {'x': 23})),
           (('l1', {'x': 4}), 'x := x/2', ('l1', {'x': 2})), (('l1', {'x': 502}), 'x := x/2', ('l1', {'x': 251})),
           (('l1', {'x': 1336}), 'x := x/2', ('l1', {'x': 668})), (('l1', {'x': 526}), 'x := x/2', ('l1', {'x': 263})),
           (('l1', {'x': 1154}), 'x := x/2', ('l1', {'x': 577})),
           (('l1', {'x': 121}), 'x := 3x + 1', ('l1', {'x': 364})),
           (('l1', {'x': 214}), 'x := x/2', ('l1', {'x': 107})), (('l1', {'x': 82}), 'x := x/2', ('l1', {'x': 41})),
           (('l1', {'x': 566}), 'x := x/2', ('l1', {'x': 283})),
           (('l1', {'x': 3077}), 'x := 3x + 1', ('l1', {'x': 9232})),
           (('l1', {'x': 377}), 'x := 3x + 1', ('l1', {'x': 1132})),
           (('l1', {'x': 61}), 'x := 3x + 1', ('l1', {'x': 184})),
           (('l1', {'x': 2308}), 'x := x/2', ('l1', {'x': 1154})), (('l1', {'x': 350}), 'x := x/2', ('l1', {'x': 175})),
           (('l1', {'x': 263}), 'x := 3x + 1', ('l1', {'x': 790})),
           (('l1', {'x': 27}), 'x := 3x + 1', ('l1', {'x': 82})),
           (('l1', {'x': 1619}), 'x := 3x + 1', ('l1', {'x': 4858})),
           (('l1', {'x': 160}), 'x := x/2', ('l1', {'x': 80})), (('l1', {'x': 137}), 'x := 3x + 1', ('l1', {'x': 412})),
           (('l1', {'x': 719}), 'x := 3x + 1', ('l1', {'x': 2158})), (('l1', {'x': 92}), 'x := x/2', ('l1', {'x': 46})),
           (('l1', {'x': 167}), 'x := 3x + 1', ('l1', {'x': 502})),
           (('l1', {'x': 593}), 'x := 3x + 1', ('l1', {'x': 1780})),
           (('l1', {'x': 310}), 'x := x/2', ('l1', {'x': 155})), (('l1', {'x': 274}), 'x := x/2', ('l1', {'x': 137})),
           (('l1', {'x': 1300}), 'x := x/2', ('l1', {'x': 650})), (('l1', {'x': 700}), 'x := x/2', ('l1', {'x': 350})),
           (('l1', {'x': 70}), 'x := x/2', ('l1', {'x': 35})), (('l1', {'x': 395}), 'x := 3x + 1', ('l1', {'x': 1186})),
           (('l1', {'x': 47}), 'x := 3x + 1', ('l1', {'x': 142})),
           (('l1', {'x': 155}), 'x := 3x + 1', ('l1', {'x': 466})),
           (('l1', {'x': 319}), 'x := 3x + 1', ('l1', {'x': 958})), (('l1', {'x': 142}), 'x := x/2', ('l1', {'x': 71})),
           (('l1', {'x': 1438}), 'x := x/2', ('l1', {'x': 719})), (('l1', {'x': 1780}), 'x := x/2', ('l1', {'x': 890})),
           (('l1', {'x': 7288}), 'x := x/2', ('l1', {'x': 3644})), (('l1', {'x': 754}), 'x := x/2', ('l1', {'x': 377})),
           (('l1', {'x': 53}), 'x := 3x + 1', ('l1', {'x': 160})), (('l1', {'x': 8}), 'x := x/2', ('l1', {'x': 4})),
           (('l1', {'x': 182}), 'x := x/2', ('l1', {'x': 91})), (('l1', {'x': 2734}), 'x := x/2', ('l1', {'x': 1367})),
           (('l1', {'x': 334}), 'x := x/2', ('l1', {'x': 167})), (('l1', {'x': 5}), 'x := 3x + 1', ('l1', {'x': 16})),
           (('l1', {'x': 866}), 'x := x/2', ('l1', {'x': 433})), (('l1', {'x': 850}), 'x := x/2', ('l1', {'x': 425})),
           (('l1', {'x': 425}), 'x := 3x + 1', ('l1', {'x': 1276})),
           (('l1', {'x': 161}), 'x := 3x + 1', ('l1', {'x': 484})),
           (('l1', {'x': 958}), 'x := x/2', ('l1', {'x': 479})),
           (('l1', {'x': 2051}), 'x := 3x + 1', ('l1', {'x': 6154})),
           (('l1', {'x': 62}), 'x := x/2', ('l1', {'x': 31})), (('l1', {'x': 10}), 'x := x/2', ('l1', {'x': 5})),
           (('l1', {'x': 1822}), 'x := x/2', ('l1', {'x': 911})), (('l1', {'x': 484}), 'x := x/2', ('l1', {'x': 242})),
           (('l1', {'x': 1132}), 'x := x/2', ('l1', {'x': 566})),
           (('l1', {'x': 3238}), 'x := x/2', ('l1', {'x': 1619})),
           (('l1', {'x': 9232}), 'x := x/2', ('l1', {'x': 4616})), (('l1', {'x': 106}), 'x := x/2', ('l1', {'x': 53})),
           (('l1', {'x': 175}), 'x := 3x + 1', ('l1', {'x': 526})),
           (('l1', {'x': 91}), 'x := 3x + 1', ('l1', {'x': 274})), (('l1', {'x': 976}), 'x := x/2', ('l1', {'x': 488})),
           (('l1', {'x': 124}), 'x := x/2', ('l1', {'x': 62})), (('l1', {'x': 184}), 'x := x/2', ('l1', {'x': 92})),
           (('l1', {'x': 244}), 'x := x/2', ('l1', {'x': 122})), (('l1', {'x': 466}), 'x := x/2', ('l1', {'x': 233})),
           (('l1', {'x': 283}), 'x := 3x + 1', ('l1', {'x': 850})),
           (('l1', {'x': 206}), 'x := x/2', ('l1', {'x': 103})), (('l1', {'x': 35}), 'x := 3x + 1', ('l1', {'x': 106})),
           (('l1', {'x': 71}), 'x := 3x + 1', ('l1', {'x': 214})),
           (('l1', {'x': 2429}), 'x := 3x + 1', ('l1', {'x': 7288})),
           (('l1', {'x': 6154}), 'x := x/2', ('l1', {'x': 3077})), (('l1', {'x': 364}), 'x := x/2', ('l1', {'x': 182})),
           (('l1', {'x': 412}), 'x := x/2', ('l1', {'x': 206})), (('l1', {'x': 668}), 'x := x/2', ('l1', {'x': 334})),
           (('l1', {'x': 41}), 'x := 3x + 1', ('l1', {'x': 124})), (('l1', {'x': 650}), 'x := x/2', ('l1', {'x': 325})),
           (('l1', {'x': 251}), 'x := 3x + 1', ('l1', {'x': 754})),
           (('l1', {'x': 911}), 'x := 3x + 1', ('l1', {'x': 2734})),
           (('l1', {'x': 4102}), 'x := x/2', ('l1', {'x': 2051})), (('l1', {'x': 890}), 'x := x/2', ('l1', {'x': 445})),
           (('l1', {'x': 1276}), 'x := x/2', ('l1', {'x': 638})),
           (('l1', {'x': 103}), 'x := 3x + 1', ('l1', {'x': 310})),
           (('l1', {'x': 445}), 'x := 3x + 1', ('l1', {'x': 1336})),
           (('l1', {'x': 1186}), 'x := x/2', ('l1', {'x': 593})), (('l1', {'x': 2}), 'x := x/2', ('l1', {'x': 1})),
           (('l1', {'x': 322}), 'x := x/2', ('l1', {'x': 161})),
           (('l1', {'x': 325}), 'x := 3x + 1', ('l1', {'x': 976})),
           (('l1', {'x': 1367}), 'x := 3x + 1', ('l1', {'x': 4102})),
           (('l1', {'x': 31}), 'x := 3x + 1', ('l1', {'x': 94})), (('l1', {'x': 122}), 'x := x/2', ('l1', {'x': 61})),
           (('l1', {'x': 790}), 'x := x/2', ('l1', {'x': 395})), (('l1', {'x': 488}), 'x := x/2', ('l1', {'x': 244})),
           (('l1', {'x': 40}), 'x := x/2', ('l1', {'x': 20})), (('l1', {'x': 107}), 'x := 3x + 1', ('l1', {'x': 322})),
           (('l1', {'x': 3644}), 'x := x/2', ('l1', {'x': 1822})), (('l1', {'x': 16}), 'x := x/2', ('l1', {'x': 8})),
           (('l1', {'x': 94}), 'x := x/2', ('l1', {'x': 47})), (('l1', {'x': 242}), 'x := x/2', ('l1', {'x': 121})),
           (('l1', {'x': 1}), 'nothing', ('l2', {'x': 1})), (('l1', {'x': 1732}), 'x := x/2', ('l1', {'x': 866})),
           (('l1', {'x': 2158}), 'x := x/2', ('l1', {'x': 1079})),
           (('l1', {'x': 1079}), 'x := 3x + 1', ('l1', {'x': 3238})),
           (('l1', {'x': 638}), 'x := x/2', ('l1', {'x': 319})),
           (('l1', {'x': 479}), 'x := 3x + 1', ('l1', {'x': 1438}))], 'AP': {'l1', 'l2'}, 'L': None}

COLLATZ_TS = {
    'S': [('l1', {'x': 1}), ('l1', {'x': 6}), ('l1', {'x': 10}), ('l1', {'x': 5}), ('l1', {'x': 3}), ('l2', {'x': 1}),
          ('l1', {'x': 16}), ('l1', {'x': 2}), ('l1', {'x': 4}), ('l1', {'x': 8})], 'I': [('l1', {'x': 6})],
    'Act': {'nothing', 'x := 3x + 1', 'x := x/2'},
    'to': [(('l1', {'x': 6}), 'x := x/2', ('l1', {'x': 3})), (('l1', {'x': 16}), 'x := x/2', ('l1', {'x': 8})),
           (('l1', {'x': 1}), 'nothing', ('l2', {'x': 1})), (('l1', {'x': 8}), 'x := x/2', ('l1', {'x': 4})),
           (('l1', {'x': 2}), 'x := x/2', ('l1', {'x': 1})), (('l1', {'x': 10}), 'x := x/2', ('l1', {'x': 5})),
           (('l1', {'x': 4}), 'x := x/2', ('l1', {'x': 2})), (('l1', {'x': 5}), 'x := 3x + 1', ('l1', {'x': 16})),
           (('l1', {'x': 3}), 'x := 3x + 1', ('l1', {'x': 10}))], 'AP': {'l1', 'l2'}, 'L': None}

TEST2_PG = {
    'Loc': {'l1', 'l2'},
    'Loc0': {'l1'},
    'Act': {'x := (x+y)%5', 'z := (z-y)%5'},
    'Eval': evaluate_test2,
    'Effect': effect_test2,
    'to': {
        ('l1', 'x > z', 'x := (x+y)%5', 'l2'),
        ('l2', 'true', 'z := (z-y)%5', 'l1'),
    },
    'g0': "x == 1 && y == 2 && z == 0"
}

TEST2_TS = {'S': [('l2', {'x': 3, 'y': 2, 'z': 0}), ('l1', {'x': 3, 'y': 2, 'z': 3}), ('l1', {'x': 1, 'y': 2, 'z': 0})],
            'I': [('l1', {'x': 1, 'y': 2, 'z': 0})], 'Act': {'x := (x+y)%5', 'z := (z-y)%5'},
            'to': [(('l2', {'x': 3, 'y': 2, 'z': 0}), 'z := (z-y)%5', ('l1', {'x': 3, 'y': 2, 'z': 3})),
                   (('l1', {'x': 1, 'y': 2, 'z': 0}), 'x := (x+y)%5', ('l2', {'x': 3, 'y': 2, 'z': 0}))],
            'AP': {'l2', 'l1'}, 'L': None}

TEST1_PG = {
    'Loc': {'l0'},
    'Loc0': {'l0'},
    'Act': {'a1', 'a0'},
    'Eval': evaluate_test1,
    'Effect': effect_test1,
    'to': {
        ('l0', 'true', 'a0', 'l0'),
        ('l0', 'r == 0', 'a1', 'l0'),
    },
    'g0': "r == 0"
}

TEST1_TS = {'S': [('l0', {'r': 0, 'y': 0}), ('l0', {'r': 0, 'y': 1}), ('l0', {'r': 1, 'y': 1})],
            'I': [('l0', {'r': 0, 'y': 0}), ('l0', {'r': 0, 'y': 1})], 'Act': {'a0', 'a1'},
            'to': [(('l0', {'r': 0, 'y': 1}), 'a0', ('l0', {'r': 0, 'y': 0})),
                   (('l0', {'r': 0, 'y': 1}), 'a1', ('l0', {'r': 1, 'y': 1})),
                   (('l0', {'r': 0, 'y': 0}), 'a0', ('l0', {'r': 0, 'y': 0})),
                   (('l0', {'r': 0, 'y': 0}), 'a1', ('l0', {'r': 1, 'y': 1})),
                   (('l0', {'r': 1, 'y': 1}), 'a0', ('l0', {'r': 0, 'y': 1}))], 'AP': {'l0', 'r == 0'}, 'L': None}

VENDING_PG = {
    'Loc': {'start', 'select'},
    'Loc0': {'start'},
    'Act': {'coin', 'refill', 'get_coke', 'get_sprite', 'ret_coin'},
    'Eval': evaluate,
    'Effect': effect,
    'to': {
        ('start', 'true', 'coin', 'select'),
        ('start', 'true', 'refill', 'start'),
        ('select', 'ncoke > 0', 'get_coke', 'start'),
        ('select', 'nsprite > 0', 'get_sprite', 'start'),
        ('select', 'ncoke=0 && nsprite=0', 'ret_coin', 'start')
    },
    'g0': "ncoke=2 && nsprite=2",
}

VENDING_TS = {'S': [('select', {'ncoke': 1, 'nsprite': 2}), ('start', {'ncoke': 2, 'nsprite': 0}),
                    ('start', {'ncoke': 1, 'nsprite': 2}), ('select', {'ncoke': 0, 'nsprite': 0}),
                    ('select', {'ncoke': 0, 'nsprite': 1}), ('select', {'ncoke': 2, 'nsprite': 1}),
                    ('start', {'ncoke': 0, 'nsprite': 1}), ('start', {'ncoke': 2, 'nsprite': 1}),
                    ('start', {'ncoke': 0, 'nsprite': 0}), ('select', {'ncoke': 2, 'nsprite': 2}),
                    ('select', {'ncoke': 1, 'nsprite': 1}), ('start', {'ncoke': 2, 'nsprite': 2}),
                    ('start', {'ncoke': 1, 'nsprite': 1}), ('select', {'ncoke': 1, 'nsprite': 0}),
                    ('start', {'ncoke': 1, 'nsprite': 0}), ('select', {'ncoke': 2, 'nsprite': 0}),
                    ('select', {'ncoke': 0, 'nsprite': 2}), ('start', {'ncoke': 0, 'nsprite': 2})],
              'I': [('start', {'ncoke': 2, 'nsprite': 2})],
              'Act': {'get_coke', 'coin', 'refill', 'ret_coin', 'get_sprite'},
              'to': [(('select', {'ncoke': 0, 'nsprite': 2}), 'get_sprite', ('start', {'ncoke': 0, 'nsprite': 1})),
                     (('start', {'ncoke': 0, 'nsprite': 0}), 'coin', ('select', {'ncoke': 0, 'nsprite': 0})),
                     (('select', {'ncoke': 1, 'nsprite': 2}), 'get_coke', ('start', {'ncoke': 0, 'nsprite': 2})),
                     (('select', {'ncoke': 2, 'nsprite': 1}), 'get_sprite', ('start', {'ncoke': 2, 'nsprite': 0})),
                     (('start', {'ncoke': 0, 'nsprite': 2}), 'coin', ('select', {'ncoke': 0, 'nsprite': 2})),
                     (('start', {'ncoke': 2, 'nsprite': 1}), 'coin', ('select', {'ncoke': 2, 'nsprite': 1})),
                     (('select', {'ncoke': 1, 'nsprite': 2}), 'get_sprite', ('start', {'ncoke': 1, 'nsprite': 1})),
                     (('start', {'ncoke': 1, 'nsprite': 1}), 'refill', ('start', {'ncoke': 2, 'nsprite': 2})),
                     (('start', {'ncoke': 1, 'nsprite': 1}), 'coin', ('select', {'ncoke': 1, 'nsprite': 1})),
                     (('start', {'ncoke': 2, 'nsprite': 0}), 'coin', ('select', {'ncoke': 2, 'nsprite': 0})),
                     (('start', {'ncoke': 1, 'nsprite': 0}), 'coin', ('select', {'ncoke': 1, 'nsprite': 0})),
                     (('start', {'ncoke': 0, 'nsprite': 1}), 'refill', ('start', {'ncoke': 2, 'nsprite': 2})),
                     (('start', {'ncoke': 0, 'nsprite': 0}), 'refill', ('start', {'ncoke': 2, 'nsprite': 2})),
                     (('start', {'ncoke': 0, 'nsprite': 2}), 'refill', ('start', {'ncoke': 2, 'nsprite': 2})),
                     (('select', {'ncoke': 2, 'nsprite': 2}), 'get_coke', ('start', {'ncoke': 1, 'nsprite': 2})),
                     (('select', {'ncoke': 2, 'nsprite': 2}), 'get_sprite', ('start', {'ncoke': 2, 'nsprite': 1})),
                     (('select', {'ncoke': 2, 'nsprite': 0}), 'get_coke', ('start', {'ncoke': 1, 'nsprite': 0})),
                     (('start', {'ncoke': 2, 'nsprite': 2}), 'refill', ('start', {'ncoke': 2, 'nsprite': 2})),
                     (('select', {'ncoke': 0, 'nsprite': 0}), 'ret_coin', ('start', {'ncoke': 0, 'nsprite': 0})),
                     (('start', {'ncoke': 1, 'nsprite': 2}), 'refill', ('start', {'ncoke': 2, 'nsprite': 2})),
                     (('start', {'ncoke': 2, 'nsprite': 2}), 'coin', ('select', {'ncoke': 2, 'nsprite': 2})),
                     (('start', {'ncoke': 2, 'nsprite': 1}), 'refill', ('start', {'ncoke': 2, 'nsprite': 2})),
                     (('start', {'ncoke': 1, 'nsprite': 0}), 'refill', ('start', {'ncoke': 2, 'nsprite': 2})),
                     (('select', {'ncoke': 1, 'nsprite': 1}), 'get_sprite', ('start', {'ncoke': 1, 'nsprite': 0})),
                     (('select', {'ncoke': 1, 'nsprite': 1}), 'get_coke', ('start', {'ncoke': 0, 'nsprite': 1})),
                     (('select', {'ncoke': 2, 'nsprite': 1}), 'get_coke', ('start', {'ncoke': 1, 'nsprite': 1})),
                     (('select', {'ncoke': 1, 'nsprite': 0}), 'get_coke', ('start', {'ncoke': 0, 'nsprite': 0})),
                     (('start', {'ncoke': 0, 'nsprite': 1}), 'coin', ('select', {'ncoke': 0, 'nsprite': 1})),
                     (('select', {'ncoke': 0, 'nsprite': 1}), 'get_sprite', ('start', {'ncoke': 0, 'nsprite': 0})),
                     (('start', {'ncoke': 2, 'nsprite': 0}), 'refill', ('start', {'ncoke': 2, 'nsprite': 2})),
                     (('start', {'ncoke': 1, 'nsprite': 2}), 'coin', ('select', {'ncoke': 1, 'nsprite': 2}))],
              'AP': {'ncoke > 0', 'start', 'nsprite > 0', 'select'}, 'L': None}

EMPTY_PG = {
    'Loc': {'loc0', 'loc1'},
    'Loc0': {'loc0'},
    'Act': {'coin'},
    'Eval': evaluate,
    'Effect': effect,
    'to': {
        ('loc0', 'true', 'coin', 'loc1'),
    },
    'g0': "true",
}

EMPTY_PG_TS = {'S': [('loc0', {}), ('loc1', {})], 'I': [('loc0', {})], 'Act': {'coin'},
               'to': [(('loc0', {}), 'coin', ('loc1', {}))], 'AP': {'loc0', 'loc1'}, 'L': None}


def compare_states(real_states, answer_states):
    if len(real_states) != len(answer_states):
        return False

    return all([s in answer_states for s in real_states])


def compare_transitions(real_t, answer_t):
    if len(real_t) != len(answer_t):
        return False

    return all([t in answer_t for t in real_t])


def compare_tuples(real, answer):
    if len(real) != len(answer):
        return False
    for i in range(len(real)):
        if type(real[i]) is tuple:
            if not compare_tuples(real[i], answer[i]):
                return False
        elif type(real[i]) is dict:
            answer_dict = answer[i].copy()
            if real != answer_dict:
                return False
        elif real[i] != answer[i]:
            return False
    return True


def compare_gropus(name, real, answer):
    # print('found', name, 'problem')
    if len(answer) > len(real):
        print('your ', name, 'size is larger then is should be')
        print('real', name, real[name])
        print('answer', name, answer[name])
        return False

    for a in real[name]:
        found = False
        for b in answer[name]:
            if type(a) is tuple and compare_tuples(a, b):
                found = True
                break
            elif a == b:
                found = True
                break
        if not found:
            print('your', name, 'is missing', a)
            print('real', name, real[name])
            print('answer', name, answer[name])
            return False

    for a in answer[name]:
        found = False
        for b in real[name]:
            if type(b) is tuple and compare_tuples(a, b):
                found = True
                break
            elif a == b:
                found = True
                break
        if not found:
            print('your', name, 'have to much', a)
            print('real', name, real[name])
            print('answer', name, answer[name])
            return False

    return True


def compare_ts(real, answer):
    if not compare_gropus('Act', real, answer):
        return False
    if not compare_gropus('AP', real, answer):
        return False
    if not compare_gropus('S', real, answer):
        return False
    if not compare_gropus('I', real, answer):
        return False
    if not compare_gropus('to', real, answer):
        return False
    return True


assert compare_ts(VENDING_TS, transitionSystemFromProgramGraph(
    VENDING_PG, vars={'ncoke': range(3), 'nsprite': range(3)}, labels={"ncoke > 0", "nsprite > 0"}))

assert compare_ts(EMPTY_PG_TS, transitionSystemFromProgramGraph(
    EMPTY_PG, vars={}, labels=set()))

assert compare_ts(TEST1_TS, transitionSystemFromProgramGraph(
    TEST1_PG, vars={'r': range(2), 'y': range(2)}, labels={'r == 0'}))

assert compare_ts(TEST2_TS, transitionSystemFromProgramGraph(
    TEST2_PG, vars={'x': range(5), 'y': range(5), 'z': range(5)}, labels=set()))

assert compare_ts(COLLATZ_TS, transitionSystemFromProgramGraph(
    COLLATZ_PG, vars={'x': range(7)}, labels=set()))

assert compare_ts(TEST3_TS, transitionSystemFromProgramGraph(
    TEST3_PG, vars={'x': range(7)}, labels=set()))

assert compare_ts(LONG_COLLATZ_TS, transitionSystemFromProgramGraph(
    LONG_COLLATZ_PG, vars={'x': range(30)}, labels=set()))
