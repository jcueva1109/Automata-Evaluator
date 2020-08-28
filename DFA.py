class DFA:
    def __init__(self):
        pass

    def dfa_evaluate(self, alphabet, states, initial_state, accepting_states, transitions, str_test):
        current_state = initial_state
        #Mi current state = q0
        
        final = True

        for char_index in range(len(str_test)):
            current_char = str_test[char_index]
            existe = True       #si encontramos o no un estado
            for t in transitions: 
                if current_state == t[0] and current_char == t[1]:
                    current_state = t[2]
                    existe = False
                    break
            
            if existe:
                final = False       #Para saber si se recorrio toda la cadena
                break

        if current_state in accepting_states and final:
            print ("Pertenece a L(M)")
        else: 
            print ("No pertenece a L(M)")
        pass