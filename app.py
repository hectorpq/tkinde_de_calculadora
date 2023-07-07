from tkinter import *

root = Tk()
root.title("CALCULADORA")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i = 0

def obtener_numero(n):
    global i
    display.insert(i, n)
    i += 1

def obtener_operador(operador):
    global i
    operador_length = len(operador)
    display.insert(i, operador)
    i += operador_length

def reiniciar_pantalla():
    display.delete(0, END)

def eliminar():
    estado_actual = display.get()
    if len(estado_actual):
        nuevo_estado = estado_actual[:-1]
        reiniciar_pantalla()
        display.insert(0, nuevo_estado)
    else:
        reiniciar_pantalla()
        display.insert(0, 'Error')

def calcular():
    estado_actual = display.get()
    try:
        result = eval(estado_actual)
        reiniciar_pantalla()
        display.insert(0, result)
    except:
        reiniciar_pantalla()
        display.insert(0, 'Error')


# botones numericos

Button(root, text="1", command=lambda: obtener_numero(1), height=4, width=12).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda: obtener_numero(2), height=4, width=12).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda: obtener_numero(3), height=4, width=12).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda: obtener_numero(4), height=4, width=12).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda: obtener_numero(5), height=4, width=12).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda: obtener_numero(6), height=4, width=12).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda: obtener_numero(7), height=4, width=12).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda: obtener_numero(8), height=4, width=12).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda: obtener_numero(9), height=4, width=12).grid(row=4, column=2, sticky=W+E)

# botones extras

Button(root, text="AC", command=lambda: reiniciar_pantalla(), height=4, width=12).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda: obtener_numero(0), height=4, width=12).grid(row=5, column=1, sticky=W+E)
Button(root, text="%", command=lambda: obtener_operador("%"), height=4, widt=12).grid(row=5, column=2, sticky=W+E)

Button(root, text="+", command=lambda: obtener_operador("+"), height=4, width=12).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda: obtener_operador("-"), height=4, width=12).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda: obtener_operador("*"), height=4, width=12).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda: obtener_operador("/"), height=4, width=12).grid(row=5, column=3, sticky=W+E)

Button(root, text="🠜", command=lambda: eliminar(), height=4, width=12).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", command=lambda: obtener_operador("**"), height=4, width=12).grid(row=3, column=4, sticky=W+E)
Button(root, text="x²", command=lambda: obtener_operador("**2"), height=4, width=12).grid(row=3, column=5, sticky=W+E)
Button(root, text="(", command=lambda: obtener_operador("("), height=4, width=12).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", command=lambda: obtener_operador(")"), height=4, width=12).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", command=lambda: calcular(), height=4, width=12).grid(row=5, column=4, sticky=W+E, columnspan=2)

root.mainloop()
