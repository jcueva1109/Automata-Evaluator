import copy
from DFA import *

class NFA:
    def __init(self):
        pass

    def union(self, alfabeto, estados, transiciones):
        res = []

        for alfa in alfabeto:
            tr = []
            for t in transiciones:
                if type(estados) != type(res):
                    if t[0] == estados and t[1] == alfa:      #Hay una transicion entre Estado y Alfabeto
                        tr.append(t[2])                       #Entonces guardamos adonde nos lleva
                else:    
                    for index in estados:
                        if t[0] == index and t[1] == alfa:      #Hay una transicion entre Estado y Alfabeto
                            tr.append(t[2])                       #Entonces guardamos adonde nos lleva

            if len(tr) == 0:                            #Si no hay transicion guardamos un valor nulo
                tr.append("/")

            res.append(tr)
        var = [estados, res]
       
        return var                               #Retornamos el estado con sus transacciones

    def nfa2dfa(self, alphabet, states, initial_state, accepting_states, transitions, str_test):

        #Hacemos la copia del archivo para manipular los datos
        alpha = copy.deepcopy(alphabet)
        stat = copy.deepcopy(states)
        i_stat = copy.deepcopy(initial_state)
        a_stat = copy.deepcopy(accepting_states)
        trans = copy.deepcopy(transitions)

        #Borramos datos para pasar NFA -> DFA
        states.clear()  
        accepting_states.clear()
        transitions.clear()

        var = self.union(alpha, i_stat, trans)
        nfaTable = [var]
        
        # nfaTable = [x = estado] [y = transiciones de x]

        for x in nfaTable:      #estados
            for y in x[1]:
                diosito = True
                for z in nfaTable:
                    if y == z[0]:       #transiciones
                        diosito = False #revisamos si existe el nuevo estado
                    
                if diosito:
                    res = self.union(alpha, y, trans)
                    if res not in nfaTable:
                        nfaTable.append(res)

        #Eliminamos alguna transicion repetida
        newtable=[]
        for index in range(len(nfaTable)):
            for ind in range(index,len(nfaTable)):
                    if nfaTable[index] == nfaTable[ind]:
                        newtable.append(nfaTable[ind])
                        break

        #Creamos los nuevos estados, con sus transiciones
        for x in nfaTable:

            if x[0] not in states:
                states.append(x[0])

            for i in range(len(alpha)):
                tran=[x[0],alpha[i],x[1][i]]
                if x[1][i] not in states:
                    states.append(x[1][i])

                if tran[2] != "/":
                    transitions.append(tran)

        for x in states:
            for y in a_stat:
                if y in x:
                    accepting_states.append(x)

        print("E-NFA -> NFA")
        print("Alfabeto: ",alphabet)
        print("Estados: ", states)
        print("Estados iniciales: ", initial_state)
        print("Estados finales: ", accepting_states)
        print("Transiciones: ", transitions)

        dfa = DFA()
        dfa.dfa_evaluate(alphabet, states, initial_state, accepting_states, transitions, str_test)

        pass
