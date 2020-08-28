class NFA:
    def __init(self):
        pass

    def nfa_evaluate(self, alphabet, states, initial_state, accepting_states, transitions, str_test):
        current_state = initial_state
        final = True

        for char_index in range(len(str_test)):
            current_char = str_test[char_index]
            existe = True       

            for t in transitions:
                if current_state == t[0] and current_char == t[1]:
                    current_state = t[2]
                    existe = False
                    break
            if existe:
                final = False
                break

        if current_state in accepting_states and final:
            print("Pertenece a L(M)")
        else:
            print("No pertenece a L(M)")
        pass
    
    def union(self, states):
        return tuple( i for i in states)
        pass

    def nfa2dfa(self, alphabet, states, initial_state, accepting_states, transitions, str_test):

        current_state = initial_state

        for alpha in alphabet:
            _input = alpha[0]
            print("Input: ", _input)

        print("\n")
        for char_index in range(len(str_test)):
            current_char = str_test[char_index]
            for t in transitions:
                if current_state == t[0] and _input == t[1]:
                    print(self.union(t[2]))
        pass
