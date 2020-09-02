import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from time import time


class DFA:
    def __init__(self):
        pass

    def list2String(self, s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

    def dfa_evaluate(self, alphabet, states, initial_state, accepting_states, transitions, str_test):

        tiempo_inicial = time()
        print(tiempo_inicial)

        current_state = initial_state
        G = nx.MultiDiGraph()

        for t in transitions:
            u = self.list2String(t[0])  # Estado
            v = self.list2String(t[2])  # Destino
            G.add_edge(u, v)

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
            print ("Pertenece a L(M)")
        else: 
            print ("No pertenece a L(M)")

        tiempo_final = time()
        print(tiempo_final)
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        print("El tiempo de ejecucion de la funcion DFA fue: ", tiempo_ejecucion)

        nx.draw(G, with_labels=True, node_color='#00b49d')
        plt.ion()
        plt.show()
        plt.pause(0.001)
        input("Press [enter] to continue.")
        
        pass
