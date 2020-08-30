import copy
from NFA import *

class ENFA:
    def __init__(self):
        pass

    def isENFA(self, alphabet):

        exito = False

        for alpha in alphabet:
           if "E" in alpha:
               exito = True
        
        return exito   
        pass

    def enfa2nfa(self, alphabet, states, initial_state, accepting_states, transitions, str_test):
        
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
        
        for a in alphabet:
            for s in stat:                              #este es el estado 
                for t in trans:
                    #Encontrar las transiciones con epsilon
                    if s == t[0] and t[1] == "E":
                        #aqui encontras donde llegas con epsilon desde el estadp ejemplo [a,E,b] llegas a "b"

                        for t2 in trans:
                            if t[2] == t2[0] and t2[1] == a:
                                #aqui tenes que encontrar a donde llegas con a->alphabet desde el "b" osea [b,a->alfabetp,??]
                                
                                for t3 in trans:
                                    if t2[2] == t3[0] and t3[1] == "E":
                                        #aqui encontramos donde podemos llegar con epsilon desde el estado que podemos llegar desde el alfabeto del estado que llegamos con epsilon

                                        lista = [s, a, t3[2]]
                                        if lista not in transitions:
                                            transitions.append(lista)

        print("E-NFA -> NFA")
        print("Alfabeto: ",alphabet)
        print("Estados: ", states)
        print("Estados iniciales: ", initial_state)
        print("Estados finales: ", accepting_states)
        print("Transiciones: ", transitions)
        
        nfa = NFA()
        nfa.nfa2dfa(alphabet, states, initial_state, accepting_states, transitions, str_test)

        pass