import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: ignacio
apellido: tevez
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        edades_total = 0
        promedio_edades = 0
        total_votos = 0
        contador = 0
        nombre_primero = 0
        nombre_ultimo = 0
        edad_ultimo = 0
        menos_votos = 0
        mas_votos = 0
        while True:
            nombre = prompt("","Ingrese el nombre")
            if nombre == None:
                break
            edad = prompt("","Ingrese la edad (mayor de 25)")
            if edad == None: #or edad < 25 NO ANDUVO, EDAD = STRING
                break
            cantidad_votos = prompt("","Ingrese la cantidad de votos(no menor a cero)")
            if cantidad_votos == None: #or cantidad_votos < 0:
                break

            edad = int(edad)
            cantidad_votos = int(cantidad_votos)
            nombre_primero = str(nombre_primero) 
            nombre_ultimo = str(nombre_ultimo)
            edad_ultimo = int(edad_ultimo)
            
            if menos_votos == 0 and mas_votos == 0:
                menos_votos = cantidad_votos
                mas_votos = cantidad_votos
                nombre_primero = nombre
                nombre_ultimo = nombre
                edad_ultimo = edad
            else:
                if cantidad_votos > mas_votos:
                    mas_votos = cantidad_votos
                    nombre_primero = nombre
                elif cantidad_votos < menos_votos:
                    menos_votos = cantidad_votos
                    nombre_ultimo = nombre
                    edad_ultimo = edad
            total_votos += cantidad_votos
            edades_total += edad
            contador +=1
            promedio_edades = edades_total/contador
        msg = f"El candidato con mas votos es: {nombre_primero}, El candidato con menos votos es: {nombre_ultimo} con edad de: {edad_ultimo}, El promedio de las edades de los candidatos es: {promedio_edades},La cantidad total de votos es: {total_votos}"
        alert("",msg)
            
            



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
