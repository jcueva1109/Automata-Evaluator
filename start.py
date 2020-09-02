#       IMPORTS     #
from DFA import *
from NFA import *
from ENFA import *
import json
import tkinter as tk
from tkinter import filedialog
from time import time

def main():
    print("     Bienvenido")
    print("Porfavor ingresa tu archivo: ")
    
    root = tk.Tk()
    root.withdraw()
    selectedFile = filedialog.askopenfilename()
    #Opening JSON File
    f = open(selectedFile,)

    #Returns JSON object as a dictionary
    data = json.load(f)

    alphabet = data["alphabet"]
    states = data["states"]
    initial_states = data["initial_state"]
    final_states = data["accepting_states"]
    transitions = data["transitions"]

    print("Ingresa la cadena que quieres evaluar: ")
    str_test = input()

    print("\nEvaluando automata...")

    tiempo_inicial = time()

    # enfa = ENFA()
    # enfa.enfa2nfa(alphabet, states, initial_states, final_states, transitions, str_test)

    # nfa = NFA()
    # nfa.nfa2dfa(alphabet, states, initial_states, final_states, transitions, str_test)

    dfa = DFA()
    dfa.dfa_evaluate(alphabet, states, initial_states, final_states, transitions, str_test)
    
    tiempo_final = time()
    print("Tiempo de ejecucion fue de: ", (tiempo_final - tiempo_inicial))

    f.close()

    pass

#       EJECUCION DE PROGRAMA       #
main()
