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
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el voton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
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
