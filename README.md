# automata
A variety of solutions to problems using Finite Automata, Pushdown Automata and more...

For now all 'process' methods are implemented deterministically, since nondeterminism introduces to much time complexity to be useful in my applications personally.
You can still design and visualize nondeterminstic machines, but dont expect to be able to use them to process input just yet.

# Usage

See ```examples.py```.

```python
import automata
```

### Finite Automata

```python
fa = automata.FiniteAutomaton(states, transitions, starting_state, accepting_states)
fa.process("input string")
```

### Pushdown Automata

```python
pda = automata.PushdownAutomaton(states, transitions, starting_state)
pda.process("input string")
```

