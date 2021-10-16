import automata 

# ababab FA

t = {
    (1,'a'): 2,
    (2, 'b'): 1
}

fa = automata.FiniteAutomaton([1,2], t, 1, [1])

print(fa.process("ababa"))

# aaabbb PDA to check if N(a) = N(b)

t2 = {
    (1, 'a', 'x'): (1, ['x','x']),
    (1, 'b', 'x'): (1, []),
    (1, 'a', None): (1, ['x']),
    (1, 'b', None): (2, [])
}

pda = automata.PushdownAutomaton([1,2], t2, 1)

print(pda.process("aaaabb"))