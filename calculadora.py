from tkinter import *

ventana = Tk()
ventana.title("Calculadora facherita")

# esto sera la entrada de texto
e_texto = Entry(ventana, font=("Calibri", 20))
e_texto.pack()
e_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# aqui van los botones

boton = Button(ventana, text="hola", width=5, height=2)
boton2 = Button(ventana, text="adios", width=5, height=2)
boton3 = Button(ventana, text="que hay", width=5, height=2)
boton4 = Button(ventana, text="hola", width=5, height=2)
boton5 = Button(ventana, text="hola", width=5, height=2)
boton6 = Button(ventana, text="hola", width=5, height=2)
boton7 = Button(ventana, text="hola", width=5, height=2)
boton8 = Button(ventana, text="hola", width=5, height=2)
boton9 = Button(ventana, text="hola", width=5, height=2)

ventana.mainloop()
