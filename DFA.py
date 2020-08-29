import copy

class DFA:
    def __init__(self):
        pass

    def dfa_evaluate(self, alphabet, states, initial_state, accepting_states, transitions, str_test):
        
        current_state = initial_state

        #TODO: transitions imprime dos veces

        for char_index in range(len(str_test)):
           current_char = str_test[char_index]
           for t in transitions:
                next_state = t[2]
                current_state = next_state

        if current_state in accepting_states:
            print ("Pertenece a L(M)")
        else: 
            print ("No pertenece a L(M)")
        pass