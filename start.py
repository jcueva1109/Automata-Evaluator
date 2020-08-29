#       IMPORTS     #
from DFA import *
from NFA import *
import json
import tkinter as tk
from tkinter import filedialog

def main():
    print("     Bienvenido")
    print("Selecciona la opcion a ejecutar: ")
    print("1. Evaluar DFA")
    print("2. Evaluar NFA")
    print("3. Evaluar NFA-E")
    print("4. Evaluar Expresion Regular")
    print("5. Equivalencia")
    print("6. Salir")
    opcion = int(input())
    print("\n")

    #selectedFile = filedialog.askopenfilename()
    #print(selectedFile)
    #Opening JSON File
    f = open("C:/Users/jesus/Downloads/NFA Examples/SimpleNFA_4_.json")

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
    f.close()

    if opcion == 1:
        
        
        dfa = DFA()
        dfa.dfa_evaluate(alphabet, states, initial_states, final_states, transitions, str_test)

    elif opcion == 2:
       
        nfa = NFA()
        nfa.nfa2dfa(alphabet, states, initial_states, final_states, transitions)
        
    elif opcion == 3:
        print("Opcion 3")
    elif opcion == 4:
        print("Opcion 4")
    elif opcion == 4:
        print("Opcion 5")
    elif opcion == 6:
        print("Hasta Pronto!")
    pass

#       EJECUCION DE PROGRAMA       #
main()

#ejecucion: python -u fileName.py