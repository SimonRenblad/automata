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
    
    """
    def __init__(self, states, transitions, starting_state, accepting_states):
        super().__init__(states, transitions, starting_state, accepting_states)

    def process(self,input) -> bool:
        pass

    def visualize(self) -> None:
        pass