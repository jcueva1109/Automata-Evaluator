import copy
from NFA import *
from time import time
import networkx as nx
import matplotlib.pyplot as plt

class ENFA:
    def __init__(self):
        pass

    def enfa2nfa(self, alphabet, states, initial_state, accepting_states, transitions, str_test):

        tiempo_inicial = time()
        print(tiempo_inicial)

        #Hacemos la copia del archivo para manipular los datos
        alpha = copy.deepcopy(alphabet)
        stat = copy.deepcopy(states)
        i_stat = copy.deepcopy(initial_state)
        a_stat = copy.deepcopy(accepting_states)
        trans = copy.deepcopy(transitions)
        
        #Borrar epsilon del alfabeto listo
        alphabet.remove("E")

        #Borrar transiciones con epsilon
        transitions.clear()
        for t in trans:
            if t[1] != "E":
                transitions.append(t)
        
        G = nx.MultiDiGraph()

        for a in alphabet:
            for s in stat:                              #Estado
                for t in trans:
                    #Encontrar las transiciones con epsilon
                    if s == t[0] and t[1] == "E":
                        ##Adonde voy con epsilon desde el estado actual

                        for t2 in trans:
                            if t[2] == t2[0] and t2[1] == a:
                                #Encontramos el camino del estado con el input 
                                
                                for t3 in trans:
                                    if t2[2] == t3[0] and t3[1] == "E":
                                        #Por ultimo encontramos el camino donde podemos llegar con epsilon con el input del estado
                                        
                                        lista = [s, a, t3[2]]
                                        if lista not in transitions:
                                            transitions.append(lista)

            for t in transitions:
                G.add_edge(t[2], t[0])

        # print("E-NFA -> NFA")
        # print("Alfabeto: ",alphabet)
        # print("Estados: ", states)
        # print("Estados iniciales: ", initial_state)
        # print("Estados finales: ", accepting_states)
        # print("Transiciones: ", transitions)
        
        tiempo_final = time()
        print(tiempo_final)
        tiempo_ejecucion = tiempo_final - tiempo_inicial
        print("El tiempo de ejecucion de la funcion E-NFA fue: ", tiempo_ejecucion)

        nx.draw(G, with_labels=True, node_color='#00b49d')
        plt.ion()
        plt.show()
        plt.pause(0.001)
        input("Press [enter] to continue.")
        
        nfa = NFA()
        nfa.nfa2dfa(alphabet, states, initial_state, accepting_states, transitions, str_test)

        pass