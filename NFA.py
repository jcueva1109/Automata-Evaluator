import copy

class NFA:
    def __init(self):
        pass

    def union(self, alfabeto, estados, transiciones):
        res = []

        for alfa in alfabeto:
            tr = []
            for t in transiciones:
                for index in estados:
                    if t[0] == index and t[1] == alfa:      #Hay una transicion entre Estado y Alfabeto
                        tr.append(t[2])                       #Entonces guardamos adonde nos lleva

            if len(tr) == 0:                            #Si no hay transicion guardamos un valor nulo
                tr.append("/")

        res.append(tr)
        return [estados, res]                               #Retornamos el estado con sus transacciones


    def nfa2dfa(self, alphabet, states, initial_state, accepting_states, transitions):

        #Hacemos la copia del archivo para manipular los datos
        alpha = copy.deepcopy(alphabet)
        stat = copy.deepcopy(states)
        i_stat = copy.deepcopy(initial_state)
        a_stat = copy.deepcopy(accepting_states)
        trans = copy.deepcopy(transitions)

        # borrramos info que cambia de nfa a dfa
        states.clear()  
        accepting_states.clear()
        transitions.clear()

        #   funcion a crear combinacion

        #  estados       0       1       2
        # [a,       [[a,b],  a,    c]]
        # [[a,b]    [a, ab]

        nfaTable = [self.union(alpha, stat, trans)]
      
        # nfaTable = 
        # x = estado
        # y = transiciones de x

        for x in nfaTable:      #estados
            for y in x[1]:
                if y not in x[0]:       #transiciones
                    # CREAR LA COMBI
                    res = self.union(alpha, x, y)
                    #nfaTable.append(mandas la combi)
                    nfaTable.append(res)

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
