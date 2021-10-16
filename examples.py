import automata 

t = {
    (1,'a'): 2,
    (2, 'b'): 1
}

fa = automata.FiniteAutomaton([1,2], t, 1, [1])

print(fa.process("ababa"))