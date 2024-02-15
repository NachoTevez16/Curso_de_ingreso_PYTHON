import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: ignacio
apellido: tevez
---
Ejercicio: Match_06
---
Enunciado:
Obtener la hora ingresada en el cuadro de texto txt_hora. 
Al presionar el botón ‘Informar’ mostrar mediante alert alguno de los 
siguientes mensajes según la hora ingresada:
    Si está entre las 7 y las 11: ‘Es de mañana’
    Si está entre las 12 y las 19: ‘Es de tarde’
    Si está entre las 20 y las 24 o entre las 0 y las 6: ‘Es de noche’
    Si no está entre 0 y las 24: ‘La hora no existe’
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_hora = customtkinter.CTkLabel(master=self, text="Hora")
        self.label_hora.grid(row=0, column=0, padx=20, pady=10)
        self.txt_hora = customtkinter.CTkEntry(master=self)
        self.txt_hora.grid(row=0, column=1)
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        hora = self.txt_hora.get()
        match hora:
            case "0":
                msg = f"Son las {hora}, Es de noche"
            case "1":
                msg = f"Son la {hora}, Es de noche"
            case "2":
                msg = f"Son las {hora}, Es de noche"
            case "3":
                msg = f"Son las {hora}, Es de noche"
            case "4":
                msg = f"Son las {hora}, Es de noche"
            case "5":
                msg = f"Son las {hora}, Es de noche"
            case "6":
                msg = f"Son las {hora}, Es de noche"
            case "7":
                msg = f"Son las {hora}, Es de mañana"
            case "8":
                msg = f"Son las {hora}, Es de mañana"
            case "9":
                msg = f"Son las {hora}, Es de mañana"
            case "10":
                msg = f"Son las {hora}, Es de mañana"
            case "11":
                msg = f"Son las {hora}, Es de mañana"
            case "12":
                msg = f"Son las {hora}, Es de tarde"
            case "13":
                msg = f"Son las {hora}, Es de tarde"
            case "14":
                msg = f"Son las {hora}, Es de tarde"
            case "15":
                msg = f"Son las {hora}, Es de tarde"
            case "16":
                msg = f"Son las {hora}, Es de tarde"
            case "17":
                msg = f"Son las {hora}, Es de tarde"
            case "18":
                msg = f"Son las {hora}, Es de tarde"
            case "19":
                msg = f"Son las {hora}, Es de tarde"
            case "20":
                msg = f"Son las {hora}, Es de noche"
            case "21":
                msg = f"Son las {hora}, Es de noche"
            case "22":
                msg = f"Son las {hora}, Es de noche"
            case "23":
                msg = f"Son las {hora}, Es de noche"
            case "24":
                msg = f"Son las {hora}, Es de noche"
            case _:
                msg = f"La hora no existe"

        alert("",msg)
    
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()