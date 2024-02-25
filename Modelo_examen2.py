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

    #! 1) X- Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) X- Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) X- Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito respecto al total de personas en la lista.
    #! 4) X- Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) X- El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) X- Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        seguir = True

        contador_femenino_campo = 0
        contador_masculino_campo = 0
        contador_otro_campo = 0

        contador_entradas_general_credito = 0
        acumulador_edad_general_credito = 0

        contador_entradas_platea = 0
        contador_personas_totales = 0
        
        acumulador_descuento_total_credito = 0

        bandera_primer_general_debito = True
        nombre_precio_mas_alto_general_debito = ""
        edad_precio_mas_alto_general_debito = 0

        monto_total_platea_debito_multiplo6 = 0

        contador_entradas_platea_primo = 0

        while seguir:
            contador_personas_totales += 1
            
            nombre = input("Ingrese nombre del comprador: ")
            edad = int(input("Ingrese la edad: "))
            while edad < 16:
                edad = int(input("Reingrese la edad: "))
            genero = input("Ingrese el genero (Masculino, Femenino, Otro): ")
            tipo_entrada = input("Ingrese el tipo de entrada (General, Campo, Platea): ")
            medio_de_pago = input("Ingrese el medio de pago (Credito, Efectivo, Debito): ")

            match tipo_entrada:
                case "General":
                    precio_entrada = 16000
                    if medio_de_pago == "Credito":
                        contador_entradas_general_credito += 1
                        acumulador_edad_general_credito += edad

                    # 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
                    if bandera_primer_general_debito and medio_de_pago == "Debito":
                        nombre_precio_mas_alto_general_debito = nombre
                        edad_precio_mas_alto_general_debito = edad
                        bandera_primer_general_debito = False

                case "Campo":
                    precio_entrada = 25000
                    if genero == "Femenino":
                        contador_femenino_campo += 1
                    elif genero == "Masculino":
                        contador_masculino_campo += 1
                    elif genero == "Otro":
                        contador_otro_campo += 1

                case "Platea":
                    precio_entrada = 30000
                    if medio_de_pago == "Debito":
                        contador_entradas_platea += 1
#  6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
                    for i in range(1, edad + 1):
                        if edad % i == 0:
                            contador_entradas_platea_primo += 1


#             Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
#             precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 
            if medio_de_pago == "Credito":
                descuento = 0.20
                precio_entrada_con_descuento = precio_entrada - (precio_entrada * descuento)
                # 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito
                acumulador_descuento_total_credito += precio_entrada - precio_entrada_con_descuento
            elif medio_de_pago == "Debito":
                descuento = 0.15
                precio_entrada_con_descuento = precio_entrada - (precio_entrada * descuento)
                #7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
                if tipo_entrada == "Platea" and edad % 6 == 0:
                        monto_total_platea_debito_multiplo6 += precio_entrada_con_descuento

            seguir = question("¿Desea continuar?")

        # 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
        if contador_femenino_campo > contador_masculino_campo and contador_femenino_campo > contador_otro_campo:
            genero_mas_frecuente_campo = "Femenino"
        elif contador_masculino_campo > contador_femenino_campo and contador_masculino_campo > contador_otro_campo:
            genero_mas_frecuente_campo = "Masculino"
        else:
            genero_mas_frecuente_campo = "Otro"

        print(f"\t¡PROGRAMA FINALILZADO! (entradas totales: {contador_personas_totales})")
        
        # 1)
        if contador_femenino_campo > 0 or contador_masculino_campo > 0 or contador_otro_campo > 0:
            print(f"1. Genero más frecuente que compraron Campo: {genero_mas_frecuente_campo}")
        else:
            print(f"1. Genero más frecuente que compraron Campo: No hay personas que compraron Campo")

        # 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta  de crédito y su edad promedio.
        if contador_entradas_general_credito > 0:
            edad_promedio_general_credito = int(acumulador_edad_general_credito / contador_entradas_general_credito)
            print(f"2. Edad promedio de entrada General con Crédito: {edad_promedio_general_credito}")
        else:
            print(f"2. Edad promedio de entrada General con Crédito: No hay entradas de tipo General con Crédito")

        #3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito respecto al total de personas en la lista.
        if contador_entradas_platea > 0:
            porcentaje_entradas_platea = (contador_entradas_platea / contador_personas_totales) * 100
            print(f"3. Porcentaje de personas que compraron entradas Platea y pagaron con Debito: {porcentaje_entradas_platea}%")  
        else:
            print(f"3. Porcentaje de personas que compraron entradas Platea y pagaron con Debito: No hay entradas Platea")  

        # 4)
        print(f"4. Total de descuentos en pesos que aplicó la empresa con Crédito: ${acumulador_descuento_total_credito}")

        # 5)
        if bandera_primer_general_debito == False:
            print(f"5. El primero que pagó el precio más alto por una entrada General con Debito es: {nombre_precio_mas_alto_general_debito} de {edad_precio_mas_alto_general_debito} años")
        else:
            print(f"5. No hay personas con entradas de tipo General con Debito")

        # 6)
        if contador_entradas_platea_primo == 2:
            print(f"6. Cantidad de personas que compraron entradas Platea y cuya edad es un número primo: {contador_entradas_platea_primo}")

        
        # 7)
        if monto_total_platea_debito_multiplo6 > 0:
                print(f"7. Monto total recaudado de Platea con Debito por personas cuyas edades son multiplos de 6: ${monto_total_platea_debito_multiplo6}")
        else:
                print(f"7. Monto total recaudado de Platea con Debito por personas cuyas edades son multiplos de 6: (no hubo casos)")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
