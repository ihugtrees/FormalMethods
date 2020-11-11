
TS_prop0_1 = {
	'S': {'s1'},
	'I': {'s1'},
	'Act': {},
	'to': {},
	'AP': {'crit1', 'crit2'},
	'L': lambda s: {'crit1', 'crit2'}
}

TS_prop0_2 = {
	'S': {'s1', 's2'},
	'I': {'s1'},
	'Act': {},
	'to': {},
	'AP': {'crit1', 'crit2'},
	'L': lambda s: {'crit1', 'crit2'} if s == 's2' else {}
}

TS_prop0_3 = {
	'S': {f's{i}' for i in range(200)} | {f's_{i}' for i in range(200)},
	'I': {'s1', 's199'},
	'Act': {'a'},
	'to': {(f's{i}', 'a', f's{(i + 1) % 200}') for i in range(200)} | {('s100', 'a', 's_0')} | {
		(f's_{i}', 'a', f's_{(i + 1) % 200}') for i in range(200)},
	'AP': {'crit1', 'crit2'},
	'L': lambda s: {'crit1', 'crit2'} if s == 's_199' else {}
}

TS_prop0_4 = {
	'S': {'s1', 's2'},
	'I': {'s1', 's2'},
	'Act': {},
	'to': {},
	'AP': {'crit1', 'crit2'},
	'L': lambda s: {'crit1'} if s == 's1' else {'crit2'}
}

TS_prop0_5 = {
	'S': {f's{i}' for i in range(200)} | {f's_{i}' for i in range(200)},
	'I': {'s1'},
	'Act': {'a'},
	'to': {(f's{i}', 'a', f's{(i + 1) % 200}') for i in range(200)} | {('s100', 'a', 's_0')} | {
		(f's_{i}', 'a', f's_{(i + 1) % 200}') for i in range(200)},
	'AP': {'crit1', 'crit2'},
	'L': lambda s: {'crit1', 'crit2'} if s == 's_199' else {}
}

TS_prop0_6 = {
	'S': {f's{i}' for i in range(200)} | {f's_{i}' for i in range(200)},
	'I': {'s1', 's99'},
	'Act': {'a'},
	'to': ({(f's{i}', 'a', f's{(i + 1) % 200}') for i in range(200)} - {('s1', 'a', 's2')}) | {('s100', 'a', 's_0')} | {
		(f's_{i}', 'a', f's_{(i + 1) % 200}') for i in range(200)},
	'AP': {'crit1', 'crit2'},
	'L': lambda s: {'crit1', 'crit2'} if s == 's_199' else {}
}

# -------------- PROP-1 --------------
TS_prop1_1 = {
	'S': {'s1', 's2'},
	'I': {'s1', 's2'},
	'Act': {'a'},
	'to': {('s1', 'a', 's2')},
	'AP': {'crit1', 'crit2'},
	'L': lambda s: {'some'} if s == 's1' else {'thing'}
}

TS_prop1_2 = {
	'S': {f's{i}' for i in range(200)} | {f's_{i}' for i in range(200)},
	'I': {'s1', 's199'},
	'Act': {'a'},
	'to': {(f's{i}', 'a', f's{(i + 1) % 200}') for i in range(200)} | {('s100', 'a', 's_0')} | {
		(f's_{i}', 'a', f's_{(i + 1) % 200}') for i in range(200)},
	'AP': {'even', 'prime'},
	'L': lambda s: {'even'} if s not in ['s_0'] else {'prime'}
}

TS_prop1_3 = {
	'S': {'s1', 's2', 's3'},
	'I': {'s1'},
	'Act': {'a'},
	'to': {('s2', 'a', 's3'), ('s1', 'a', 's1')},
	'AP': {'even', 'prime'},
	'L': lambda s: {'even'} if s not in {'s3'} else {'prime'}
}

TS_prop1_4 = {
	'S': {'s1', 's2', 's3'},
	'I': {'s1', 's2'},
	'Act': {'a'},
	'to': {('s2', 'a', 's3'), ('s1', 'a', 's1')},
	'AP': {'even', 'prime'},
	'L': lambda s: {'even'} if s not in {'s3'} else {'prime'}
}

# -------------- PROP-2 --------------
TS_prop2_1 = {
	'S': {'s1', 's2', 's3', 's4'},
	'I': {'s1'},
	'Act': {'a'},
	'to': {('s1', 'a', 's2'), ('s2', 'a', 's1'), ('s2', 'a', 's3'), ('s3', 'a', 's1'), ('s3', 'a', 's4'),
		   ('s4', 'a', 's3'), },
	'AP': {'tick', 'tok'},
	'L': lambda s: {'tick'} if s in ['s1', 's2'] else {'tok'}
}

TS_prop2_2 = {
	'S': {'s1', 's2', 's3', 's4'},
	'I': {'s1'},
	'Act': {'a'},
	'to': {('s1', 'a', 's2'), ('s2', 'a', 's1'), ('s2', 'a', 's3'), ('s3', 'a', 's1'), ('s3', 'a', 's4'),
		   ('s4', 'a', 's3'), },
	'AP': {'tick', 'tok'},
	'L': lambda s: {'tick'} if s in ['s1', 's2', 's4'] else {'tok'}
}

TS_prop2_3 = {
	'S': {'s1', 's2', 's3', 's4'},
	'I': {'s1'},
	'Act': {'a'},
	'to': {('s1', 'a', 's2'), ('s2', 'a', 's1'), ('s2', 'a', 's3'), ('s3', 'a', 's1'), ('s3', 'a', 's4')},
	'AP': {'tick', 'tok'},
	'L': lambda s: {'tick'} if s in ['s1', 's2'] else {'tok'}
}

TS_prop2_4 = {
	'S': {'s1', 's2'},
	'I': {'s1'},
	'Act': {'a'},
	'to': {('s1', 'a', 's1'), ('s1', 'a', 's2'), ('s2', 'a', 's2')},
	'AP': {'tick', 'tok'},
	'L': lambda s: {'tick'} if s in ['s1'] else {'tok'}
}

TS_prop2_5 = {
	'S': {'s1', 's2', 's3'},
	'I': {'s1'},
	'Act': {'a'},
	'to': {('s1', 'a', 's2'), ('s2', 'a', 's3'), ('s3', 'a', 's1')},
	'AP': {'tick', 'tok'},
	'L': lambda s: {'tick'} if s in ['s1', 's3'] else {'tok'}
}

TS_prop2_6 = {
	'S': {f's{i}' for i in range(100)},
	'I': {'s1'},
	'Act': {'a'},
	'to': {(f's{i}', 'a', f's{(i + 1) % 100}') for i in range(100)},
	'AP': {'tick', 'tok'},
	'L': lambda s: {'tick'} if s not in ['s55', 's66'] else {'tok'}
}

TS_prop2_7 = {
	'S': {f's{i}' for i in range(100)},
	'I': {'s1'},
	'Act': {'a'},
	'to': {(f's{i}', 'a', f's{(i + 1) % 100}') for i in range(100)} | {('s22', 'a', 's88'), ('s88', 'a', 's22')},
	'AP': {'tick', 'tok'},
	'L': lambda s: {'tick'} if s not in ['s22', 's88'] else {'tok'}
}

TS_prop2_8 = {
	'S': {'s1', 's2', 's3', 's4', 's5'},
	'I': {'s1'},
	'Act': {'a'},
	'to': {('s1', 'a', 's1'), ('s2', 'a', 's3'), ('s3', 'a', 's2'), ('s5', 'a', 's5')},
	'AP': {'tick', 'tok'},
	'L': lambda s: {'tick'} if s in ['s1'] else {'tok'}
}

TS_prop2_9 = {
	'S': {'s1', 's2', 's3'},
	'I': {'s1'},
	'Act': {'a'},
	'to': {('s1', 'a', 's2'), ('s1', 'a', 's3'),
		   ('s2', 'a', 's3'), ('s3', 'a', 's2')},
	'AP': {'tick'},
	'L': lambda s: {'tick'} if (s == 's1') else {}
}

print("PROPERTY-0 TESTS")
assert property0(TS_prop0_1)
assert not property0(TS_prop0_2)
assert property0(TS_prop0_3)
assert not property0(TS_prop0_4)
assert property0(TS_prop0_5)
assert property0(TS_prop0_6)

print("PROPERTY-0 : ALL PASSED\n")

print("PROPERTY-1 TESTS")
assert property1(TS_prop0_1)
assert property1(TS_prop0_3)
assert property1(TS_prop1_1)
assert not property1(
	TS_prop1_2), 's1->s2->...s100->s_0->...s_199->s_0 (bad path)'
assert property1(TS_prop1_3)
assert not property1(TS_prop1_4)
print("PROPERTY-1 : ALL PASSED\n")

print("PROPERTY-2 TESTS")
assert not property2(
	TS_prop2_1), 's1->s2->s3->s4->s3->s4->s3 (example for a bad path)'
assert property2(TS_prop2_2)
assert not property2(TS_prop2_3), 's1->s2->s3->s4 (example for a bad path)'
assert not property2(
	TS_prop2_4), 's1->s2->s2->s2->s2->s2... (example for a bad path)'
assert property2(TS_prop2_5)
assert property2(TS_prop2_6)
assert not property2(
	TS_prop2_7), 's0->s1->...s22->s23->...s88->s22->s88->s22..'
assert property2(TS_prop2_8)
assert not property2(TS_prop2_9)
print("PROPERTY-2 : ALL PASSED\n")
