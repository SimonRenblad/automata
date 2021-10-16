class AbstractMachine():
    def __init__(self, states, transitions, starting_state, accepting_states):
        self.states = states
        self.transitions = transitions
        self.starting_state = starting_state
        self.accepting_states = accepting_states

### FA
        
class FiniteAutomaton(AbstractMachine):
    """
    states: list
    transitions: dictionary of tuples in format (start_node, read) --> (end_node)
    starting_state: a value in states
    accepting_states: a sublist of states
    current_state: tracking variable
    """
    def __init__(self, states, transitions, starting_state, accepting_states):
        super().__init__(states, transitions, starting_state, accepting_states)
        self.current_state = starting_state

    
    def process(self,input) -> bool:
        """
        input: list to be accepted by the FA
        """
        for i in input:
            self.current_state = self.transitions.get((self.current_state, i))
            if self.current_state == None:
                return False

        return (self.current_state in self.accepting_states)

    def visualize(self) -> None:
        pass

### PDA

class PushdownAutomaton(AbstractMachine):
    """
    states: list
    transitions: dictionary of tuples in format (start_node, read, pop_stack) --> (end_node, push_stack)
    starting_state: a value in states
    accepting_states: a sublist of states
    current_state: tracking variable
    stack: a stack implemented as list
    
    by default the PDA is input-driven, meaning it accepts by empty stack
    """
    def __init__(self, states, transitions, starting_state):
        super().__init__(states, transitions, starting_state, None)
        self.current_state = starting_state
        self.stack = []

    def process(self,input) -> bool:
        """
        input: list to be accepted by the PDA
        """
        for i in input:
            out = self.transitions.get((self.current_state, i, (self.stack.pop() if self.stack else None)))
            if out == None:
                return False
            self.current_state = out[0]
            self.stack += out[1]

        return (len(self.stack)==0) # input driven definition

    def visualize(self) -> None:
        pass