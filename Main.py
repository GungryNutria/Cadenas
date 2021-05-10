
import tkinter as tk
import Operations as op
from tkinter import ttk
 
 
window = tk.Tk()
o = op.Operations()
window.title("Cadena de Caracteres")
window.minsize(500,400)
exercises = [
    'Inicia con b y termina con cb',
    'No Contiene 2 0s juntos',
    "Contiene numero de c's pares",
    'Inicia con 1 y contiene la subcadena 01 y termina con 0',
    'No contiene ab y termina con c',
    'Empieza con c y termina con cb',
    'No contiene contiene ccc',
    'Contiene ab pero no ba',
    "Numero par de a's e impar de b's"
]
 
def callbackFunc(event):
    if len(name.get()) == 0 or name.get()[0] == ' ':
        print('Cadena Vacia')
    else:
        o.setOption(combo.current(),name.get())
 
label = ttk.Label(window, text = "Ingresar Cadena ")
label.grid(column = 0, row = 1)

label2 = ttk.Label(window, text = "Operacion a realizar ")
label2.grid(column = 0, row= 0)

combo = ttk.Combobox(window, values=exercises, width=50, state="readonly")
combo.grid(column = 1, row =  0, pady=10)
combo.current(0)

name = tk.StringVar()
nameEntered = ttk.Entry(window, width = 50, textvariable = name)
nameEntered.grid(column = 1, row = 1)
 
 
button = ttk.Button(window, text = "Click Me")
button.grid(column= 0, row = 2)
button.bind("<Button>",callbackFunc)
window.mainloop()