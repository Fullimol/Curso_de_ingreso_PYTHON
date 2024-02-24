import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Bruno
apellido: Freijomil
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

    G. El máximo valor. 
    H. El mínimo valor (incluyendo en que iteracion se encontro, solo la primera)

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        suma_positivos = 0
        suma_negativos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0

        contador_iteracion = 0

        while True:
            numero = prompt("UTN", "Ingrese un numero: ")
            if numero == None:
                break

            numero = int(numero)

            if numero > 0:
                suma_positivos += numero
                cantidad_positivos += 1
            elif numero < 0:
                suma_negativos += numero
                cantidad_negativos += 1
            else:
                cantidad_ceros  += 1


            if  contador_iteracion == 0 or numero > numero_maximo:
                numero_maximo = numero
            if  contador_iteracion == 0 or numero < numero_minimo:
                numero_minimo = numero
                iteracion_minimo = contador_iteracion + 1
            contador_iteracion += 1

        diferencia = cantidad_negativos - cantidad_positivos
        if diferencia < 0:
            diferencia *= -1 #esto es, por si la diferencia es negativa, la muestre positiva.

        if contador_iteracion == 0:
            resultado = "No se ingresaron datos"
        else:
            resultado = (
            f"La suma acumulada de los negativos es: {suma_negativos} \nLa suma acumulada de los positivos es: {suma_positivos}"
            f"\nLa cantidad de numeros positivos ingresados es: {cantidad_positivos}"
            f"\nLa cantidad de numeros negativos ingresados es: {cantidad_negativos}"
            f"\nLa cantidad de ceros ingresados es: {cantidad_ceros}"
            f"\nLa diferencia entre la cantidad de numeros positivos ingresados y los negativos es: {diferencia}"
            f"\nEl numero maximo ingresado fue: {numero_maximo}"
            f"\nEl numero mínimo ingresado fue: {numero_minimo} encontrado en la iteracion {iteracion_minimo}"
            )

        alert("UTN", resultado)


    #ESTO HABÍA HECHO YO...
    # def btn_comenzar_ingreso_on_click(self):
    #     array_de_numeros = []

    #     while True:
    #             numero = prompt(title="Validar numero", prompt="Ingrese un numero")

    #             if numero == None:
    #                 break

    #             array_de_numeros.append(int(numero))
        
    #     suma_positivos = 0
    #     suma_negativos = 0

    #     for num in array_de_numeros:
    #         if num > 0:
    #             suma_positivos += num
    #         elif num < 0:
    #             suma_negativos += num


    #     cantidad_positivos = 0
    #     cantidad_negativos = 0

    #     for num in array_de_numeros:
    #         if num > 0:
    #             cantidad_positivos += 1
    #         elif num < 0:
    #             cantidad_negativos += 1

    #     cantidad_negativos = len(array_de_numeros) - cantidad_positivos
    #     cantidad_positivos = len(array_de_numeros) - cantidad_negativos
    #     diferencia_cantidad = cantidad_positivos - cantidad_negativos

    #     # Cuenta los números con algún digito 0
    #     cantidad_numeros_con_cero = 0
    #     for num in array_de_numeros:
    #         if "0" in str(num):
    #             cantidad_numeros_con_cero += 1

    #     mensaje = f"La suma acumulada de los positivos es: {suma_positivos}\nLa suma acumulada de los negativos es: {suma_negativos}\nLa cantidad de positivos es: {cantidad_positivos}\nLa cantidad de negativos es: {cantidad_negativos} \n La cantidad de ceros es: {cantidad_numeros_con_cero} \nLa diferencia entre la cantidad de positivos y negativos es: {diferencia_cantidad}"

    #     alert(None, mensaje)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
