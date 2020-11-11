

test1_result = {
	'S': {(False, False, False), (True, True, False), (False, True, False), (True, False, True), (False, False, True),
		  (True, True, True), (False, True, True), (True, False, False)},
	'I': {(False, False, False), (False, False, True)}, 'Act': {(True,), (False,)},
	'to': {((False, True, False), (False,), (False, True, False)),
		   ((True, True, True), (False,), (False, False, False)),
		   ((True, True, True), (True,), (False, False, True)), ((
			   False, True, True), (False,), (True, False, False)),
		   ((True, False, False), (False,), (True, False, False)
			), ((True, True, False), (True,), (True, True, True)),
		   ((True, False, True), (True,), (True, True, True)), ((
			   True, True, False), (False,), (True, True, False)),
		   ((False, True, True), (True,), (True, False, True)), ((
			   True, False, True), (False,), (True, True, False)),
		   ((False, True, False), (True,), (False, True, True)), ((
			   False, False, False), (True,), (False, False, True)),
		   ((False, False, True), (True,), (False, True, True)), ((
			   False, False, True), (False,), (False, True, False)),
		   ((True, False, False),
			(True,), (True, False, True)), ((False, False, False), (False,), (False, False, False))},
	'AP': {'r2', 'y1', 'x1', 'r1'},
	'L': {(False, False, False): set(), (False, True, False): {'r2'}, (True, False, False): {'r1'},
		  (True, True, False): {'r1', 'r2'}, (False, False, True): {'x1'}, (False, True, True): {'r2', 'x1'}, (True, False, True): {'r1', 'x1'},
		  (True, True, True): {'r1', 'r2', 'x1', 'y1'}}

}

test2_result = {'S': {(False, False), (True, False), (True, True), (False, True)}, 'I': {(False, False), (False, True)},
				'Act': {(True,), (False,)},
				'to': {((True, True), (True,), (False, True)), ((False, True), (True,), (False, True)),
					   ((False, False), (False,), (True, False)), ((
						   True, False), (True,), (False, True)),
					   ((False, True), (False,), (False, False)), ((
						   True, False), (False,), (False, False)),
					   ((False, False), (True,), (True, True)), ((True, True), (False,), (False, False))},
				'AP': {'y1', 'x1', 'r1'},
				'L': {(False, False): set(), (True, False): {'r1', 'y1'}, (True, True): {'x1', 'r1'},
					  (False, True): {'x1', 'y1'}}}

test3_result = {'S': {(False, False, False), (True, True, False), (False, True, False), (True, False, True),
					  (False, False, True), (True, True, True), (False, True, True), (True, False, False)},
				'I': {(False, False, False), (False, False, True)}, 'Act': {(True,), (False,)},
				'to': {((True, True, True), (False,), (False, False, False)),
					   ((True, True, False), (False,),
						(False, True, False)),
					   ((True, True, True), (True,),
						(False, False, True)),
					   ((False, True, True), (False,),
						(True, False, False)),
					   ((False, True, False),
						(True,), (True, True, True)),
					   ((True, True, False), (True,),
						(False, True, True)),
					   ((True, False, True), (False,),
						(False, True, False)),
					   ((True, False, False), (False,),
						(True, False, False)),
					   ((False, False, True),
						(True,), (True, True, True)),
					   ((True, False, True), (True,),
						(False, True, True)),
					   ((False, True, True), (True,),
						(True, False, True)),
					   ((False, True, False),
						(False,), (True, True, False)),
					   ((False, False, False),
						(True,), (False, False, True)),
					   ((False, False, True),
						(False,), (True, True, False)),
					   ((True, False, False),
						(True,), (True, False, True)),
					   ((False, False, False), (False,), (False, False, False))}, 'AP': {'y1', 'r2', 'x1', 'r1'},
				'L': {(False, False, False): set(), (True, True, False): {'r1', 'r2', 'y1'},
					  (False, True, False): {'r2', 'y1'}, (True, False, True): {'r1', 'x1', 'y1'},
					  (False, False, True): {'x1', 'y1'}, (True, True, True): {'x1', 'r1', 'r2', 'y1'},
					  (False, True, True): {'x1', 'r2', 'y1'}, (True, False, False): {'r1', 'y1'}}
				}

test4_result = {
	'S': {(False, False), (False, True), (True, False), (True, True)},
	'I': {(False, False), (False, True)},
	'Act': {(True,), (False,)},
	'to': {((False, False), (True,), (True, True)),
		   ((False, False), (False,), (True, False)),
		   ((True, False), (True,), (False, True)),
		   ((True, False), (False,), (False, False)),
		   ((False, True), (True,), (False, True)),
		   ((False, True), (False,), (False, False)),
		   ((True, True), (True,), (False, True)),
		   ((True, True), (False,), (False, False))},
	'AP': {'r1', 'x1', 'y1'},
	'L': None
}


def compare_ts(generated_ts, real_ts):
	return all([generated_ts[key] == real_ts[key] for key in generated_ts if key != 'L'])


def compare_labels(generated_ts, real_ts):
	return all([generated_ts['L'](state) == real_ts['L'][state] for state in generated_ts['S']])


if __name__ == "__main__":
	assert compare_ts(transitionSystemFromCircuit(1, 2, 1, lambda s: ((s[2] and s[1]) ^ s[0], s[2] ^ s[1]),
												  lambda s: (s[0] and s[1] and s[2],)), test1_result)
	assert compare_labels(transitionSystemFromCircuit(1, 2, 1, lambda s: ((s[2] and s[1]) ^ s[0], s[2] ^ s[1]),
													  lambda s: (s[0] and s[1] and s[2],)), test1_result)

	assert compare_ts(
		transitionSystemFromCircuit(1, 1, 1, lambda s: (
			not (s[0] or s[1]),), lambda s: (s[0] ^ s[1],)),
		test2_result)

	assert compare_labels(
		transitionSystemFromCircuit(1, 1, 1, lambda s: (
			not (s[0] or s[1]),), lambda s: (s[0] ^ s[1],)),
		test2_result)

	assert compare_ts(transitionSystemFromCircuit(1, 2, 1, lambda s: tuple([s[0] ^ (s[1] or s[2]), s[2] ^ s[1]]),
												  lambda s: tuple([s[0] or s[1] or s[2]])), test3_result)

	assert compare_labels(transitionSystemFromCircuit(1, 2, 1, lambda s: tuple([s[0] ^ (s[1] or s[2]), s[2] ^ s[1]]),
													  lambda s: tuple([s[0] or s[1] or s[2]])), test3_result)

	assert compare_ts(transitionSystemFromCircuit(1, 1, 1, lambda s: (not (s[1] or s[0]),), lambda s: (s[1] ^ s[0],)),
					  test4_result)
