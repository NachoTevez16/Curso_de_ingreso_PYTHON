import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: ignacio
apellido: tevez
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0
        suma_positivo = 0
        suma_negativo = 0
        numeros_positivos = 0
        numeros_negativos = 0
        numeros_cero = 0

        while True:
            numero = prompt("","Ingrese un numero")
            if numero == None:
                break
            numero = int(numero)
            if numero == 0:
                numeros_cero += 1
            elif numero > 0:
                suma_positivo += numero
                numeros_positivos += 1
            else:
                suma_negativo += numero
                numeros_negativos += 1
            contador+=1

        diferencia_total = numeros_positivos-numeros_negativos
        msg = f"La cantidad de numeros negativos es: {numeros_negativos} y su suma fue {suma_negativo} ,la cantidad de numeros positivos es: {numeros_positivos} y la suma es: {suma_positivo}, la diferencia entre los positivos y negativos es: {diferencia_total} y la cantidad de veces que ingreso 0 es: {numeros_cero}"
        alert("",msg)
        

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
