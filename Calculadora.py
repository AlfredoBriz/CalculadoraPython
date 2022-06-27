from tkinter import *

ventana = Tk()
ventana.title("Calculadora")
ventana.configure(background="SkyBlue3")
color_boton = "grey77"

i = 0

# Entrada
e_texto = Entry(ventana, font="Calibri 20", )
e_texto.grid(row=0, column=0, columnspan=5, padx=5, pady=5)


# Funciones
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1


def borrar():
    e_texto.delete(0, END)
    i = 0


def borraruno():
    global i
    e_texto.delete(i, END)
    i -= 1


# def borrarunos(i=0):
#     if e_texto.insert(i, 1):
#        e_texto.delete(i, END)
#       i -= 1
#  else:
#     e_texto.delete(i, END)
#    i = 0

# def mov_izquierda():
# global i
# e_texto.delete(END, i)
# i = 0

def resultado_op():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete(0, END)
    e_texto.insert(0, resultado)
    i = 0


def iva():
    numero = e_texto.get()
    total = eval(numero) * 0.21
    e_texto.delete(0, END)
    e_texto.insert(0, total)
    i = 0


def masiva():
    numero = e_texto.get()
    total = eval(numero) * 1.21
    e_texto.delete(0, END)
    e_texto.insert(0, total)
    i = 0


# Botones
boton1 = Button(ventana, bg=color_boton, text="1", width=5, height=2, command=lambda: click_boton(1))
boton2 = Button(ventana, bg=color_boton, text="2", width=5, height=2, command=lambda: click_boton(2))
boton3 = Button(ventana, bg=color_boton, text="3", width=5, height=2, command=lambda: click_boton(3))
boton4 = Button(ventana, bg=color_boton, text="4", width=5, height=2, command=lambda: click_boton(4))
boton5 = Button(ventana, bg=color_boton, text="5", width=5, height=2, command=lambda: click_boton(5))
boton6 = Button(ventana, bg=color_boton, text="6", width=5, height=2, command=lambda: click_boton(6))
boton7 = Button(ventana, bg=color_boton, text="7", width=5, height=2, command=lambda: click_boton(7))
boton8 = Button(ventana, bg=color_boton, text="8", width=5, height=2, command=lambda: click_boton(8))
boton9 = Button(ventana, bg=color_boton, text="9", width=5, height=2, command=lambda: click_boton(9))
boton0 = Button(ventana, bg=color_boton, text="0", width=13, height=2, command=lambda: click_boton(0))

boton_borrar = Button(ventana, bg=color_boton, text="AC", width=5, height=2, command=lambda: borrar())
boton_parentesis1 = Button(ventana, bg=color_boton, text="(", width=5, height=2, command=lambda: click_boton("("))
boton_parentesis2 = Button(ventana, bg=color_boton, text=")", width=5, height=2, command=lambda: click_boton(")"))
boton_punto = Button(ventana, bg=color_boton, text=".", width=5, height=2, command=lambda: click_boton("."))
# boton_mov_izquierda = Button(ventana, text="⇤", width=5, height=2, command=lambda: mov_izquierda())
# boton_borraruno = Button(ventana, bg=color_boton, text="⌫", width=5, height=2, command=lambda: borraruno())

boton_div = Button(ventana, bg=color_boton, text="÷", width=5, height=2, command=lambda: click_boton("÷"))
boton_mult = Button(ventana, bg=color_boton, text="x", width=5, height=2, command=lambda: click_boton("*"))
boton_sum = Button(ventana, bg=color_boton, text="+", width=5, height=2, command=lambda: click_boton("+"))
boton_rest = Button(ventana, bg=color_boton, text="-", width=5, height=2, command=lambda: click_boton("-"))
boton_igual = Button(ventana, bg=color_boton, text="=", width=5, height=2, command=lambda: resultado_op())
boton_iva = Button(ventana, bg=color_boton, text="%IVA", width=5, height=2, command=lambda: iva())
boton_masiva = Button(ventana, bg=color_boton, text="+IVA", width=5, height=2, command=lambda: masiva())
boton_salir = Button(ventana, bg=color_boton, text='Salir', command=quit)

# Agregar botones en pantalla
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_div.grid(row=1, column=3, padx=5, pady=5)
# boton_borraruno.grid(row=1, column=4, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_mult.grid(row=2, column=3, padx=5, pady=5)
boton_iva.grid(row=1, column=4, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sum.grid(row=3, column=3, padx=5, pady=5)
boton_masiva.grid(row=2, column=4, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_rest.grid(row=4, column=3, padx=5, pady=5)
# boton_mov_izquierda.grid(row=4, column=4, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)
boton_salir.grid(row=5, column=4, padx=5, pady=5)

ventana.mainloop()
