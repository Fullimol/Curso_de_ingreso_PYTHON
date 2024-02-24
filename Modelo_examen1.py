import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Bruno
apellido: Freijomil
---
Enunciado:
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
    valores:
    Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
    valores:

    Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
        * Nombre
        * Monto en pesos de la operación (no menor a $10000)
        * Tipo de instrumento(CEDEAR, BONOS, MEP) 
        * Cantidad de instrumentos  (no menos de cero) 
        
    Realizar los siguientes informes:
    
        #! 1) - Tipo de instrumento que menos se operó en total.
        #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
        #! 3) - Cantidad de usuarios que no compraron CEDEAR 
        #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
        #! 5) - Nombre y posicion del usuario que invirtio menos dinero
        #! 6) - Promedio de dinero en CEDEAR  ingresado en total.  
        #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("UTN Fra")

        # self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        # self.label0.grid(row=0, column=0, padx=20, pady=10)
        # self.txt_apellido = customtkinter.CTkEntry(master=self)
        # self.txt_apellido.grid(row=0, column=1)

        # self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        # self.label1.grid(row=1, column=0, padx=20, pady=10)
        # self.txt_edad = customtkinter.CTkEntry(master=self)
        # self.txt_edad.grid(row=1, column=1)

        # self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        # self.label2.grid(row=2, column=0, padx=20, pady=10)
        # self.txt_tipo = customtkinter.CTkEntry(master=self)
        # self.txt_tipo.grid(row=2, column=1, padx=20, pady=10)

        # self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        # self.label3.grid(row=3, column=0, padx=20, pady=10)
        # self.txt_legajo = customtkinter.CTkEntry(master=self)
        # self.txt_legajo.grid(row=3, column=1)

        # self.btn_validar = customtkinter.CTkButton(
        #     master=self, text="Validar", command=self.btn_validar_on_click)
        # self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")


    def btn_validar_on_click(self):
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
