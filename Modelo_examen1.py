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
    
        #! 1) X Tipo de instrumento que menos se operó en total.
        #! 2) X Cantidad de usuarios que compraron entre 50  y 200 MEP 
        #! 3) X Cantidad de usuarios que no compraron CEDEAR 
        #! 4) X Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
        #! 5) X Nombre y posicion del usuario que invirtio menos dinero
        #! 6) X Promedio de dinero en CEDEAR ingresado en total.  
        #! 7) - Promedio de cantidad de instrumentos MEP vendidos en total
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):

        acumulador_casos_CEDEAR = 0
        acumulador_casos_BONOS = 0
        acumulador_casos_MEP = 0

        cantidad_MEP_entre_50_200 = 0

        contador_no_compran_CEDEAR = 0

        bandera_primero_compro_BONOS_CEDEAR = False

        bandera_usuario_menos_dinero = False

        contador_CEDEAR = 0
        cantidad_dinero_CEDEAR = 0

        contador_MEP = 0

        for i in range(1, 3+1):
            nombre = input("Ingrese nombre: ")
            monto = int(input("Ingrese monto (mayor a $10.000): "))
            while monto < 10000:
                monto = int(input("Reingrese monto: "))
            tipo_instrumento = input("Ingrese tipo de instrumento (CEDEAR, BONOS, MEP): ")
            cantidad_instrumentos = int(input("Ingrese cantidad de instrumentos (mayor a 0): "))
            while cantidad_instrumentos < 0:
                cantidad_instrumentos = int(input("Reingrese cantidad de instrumentos: "))

            if bandera_usuario_menos_dinero == False or monto < monto_menos_dinero:
                monto_menos_dinero = monto
                nombre_menos_dinero = nombre
                posicion_menos_dinero = i 
                bandera_usuario_menos_dinero = True
            
            match tipo_instrumento:
                case "CEDEAR":
                    acumulador_casos_CEDEAR += cantidad_instrumentos
                    cantidad_dinero_CEDEAR += monto
                    contador_CEDEAR += 1
                case "BONOS":
                    contador_no_compran_CEDEAR += 1
                    acumulador_casos_BONOS += cantidad_instrumentos

                    if bandera_primero_compro_BONOS_CEDEAR == False:
                        nombre_primero_compro_BONOS_CEDEAR = nombre
                        monto_primero_compro_BONOS_CEDEAR = monto

                        bandera_primero_compro_BONOS_CEDEAR = True
                case "MEP":
                    contador_no_compran_CEDEAR += 1
                    acumulador_casos_MEP += cantidad_instrumentos
                    if cantidad_instrumentos >= 50 and cantidad_instrumentos <= 200:
                        cantidad_MEP_entre_50_200 += 1
                    contador_MEP += 1

        if acumulador_casos_CEDEAR < acumulador_casos_BONOS:
            instrumento_menos_usado = "CEDEAR"
        elif acumulador_casos_CEDEAR > acumulador_casos_BONOS:
            instrumento_menos_usado = "BONOS"
        else:
            instrumento_menos_usado = "MEP"
        
        if contador_CEDEAR > 0:
            promedio_dinero_CEDEAR = f"$ {cantidad_dinero_CEDEAR / contador_CEDEAR}"
        else:
            promedio_dinero_CEDEAR = "(Nadie compró CEDEARs)"

        if contador_MEP > 0:
            promedio_MEP = acumulador_casos_MEP / contador_MEP
        else:
            promedio_MEP = "(Nadie compró MEP)"

        print(f"\t¡PROGRAMA FINALIZADO!")
        # 1)
        print(f"Instrumento menos usado: {instrumento_menos_usado}")
        # 2)
        print(f"Cant. MEP entre 50 y 200: {cantidad_MEP_entre_50_200}")
        # 3)
        print(f"Cant. de usuarios que no compraron CEDEAR: {contador_no_compran_CEDEAR}")
        # 4)
        print(f"Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR: {nombre_primero_compro_BONOS_CEDEAR}/{monto_primero_compro_BONOS_CEDEAR}")
        # 5)
        print(f"Nombre y posicion del usuario que invirtio menos dinero: {nombre_menos_dinero} / Posición: {posicion_menos_dinero}")
        # 6)
        print(f"Promedio de dinero invertido en CEDEAR: {promedio_dinero_CEDEAR}")
        # 7)
        print(f"Promedio de instrumentos invertido en MEP: {promedio_MEP}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
