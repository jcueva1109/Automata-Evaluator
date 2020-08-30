import copy
import networkx as nx
import matplotlib.pyplot as plt

class DFA:
    def __init__(self):
        pass

    def convert(self, param):
        return (*param,)
        pass

    def dfa_evaluate(self, alphabet, states, initial_state, accepting_states, transitions, str_test):
        
        current_state = initial_state
        G = nx.MultiDiGraph()
        
        for x in states:
            n = self.convert(x)
            G.add_node(n)

        #TODO: transitions me imprime dos veces
        # agregar las transiciones al graph

        for char_index in range(len(str_test)):
           current_char = str_test[char_index]
           for t in transitions:
                next_state = t[2]
                current_state = next_state

        if current_state in accepting_states:
            print ("Pertenece a L(M)")
        else: 
            print ("No pertenece a L(M)")

        nx.draw(G, with_labels=True)
        #plt.savefig("DFA.png", format="PNG")
        plt.show()

        pass