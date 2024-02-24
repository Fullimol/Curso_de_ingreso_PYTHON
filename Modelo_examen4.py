import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado 1 : 
De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.
    • nombre , 
    • temperatura, entre 35 y 42 
    • sexo( f, m , nb ) 
    • edad(mayor a 0)

Pedir datos por prompt y mostrar por print:
Punto A - Informar cual fue el sexo mas ingresado
Punto B - El porcentaje de personas con fiebre y el porcentaje sin fiebre
Punto C - por el número de DNI del alumno...


DNI terminados en  0 o 1
1)informar la cantidad de personas de sexo  femenino
2) la edad promedio de  personas de sexo  masculino
3) el nombre de la persona la persona de sexo  nb con más temperatura(si la hay)


DNI terminados en  2 o 3
1) informar la cantidad de personas de sexo  masculino
2) la edad promedio de  personas de sexo  nb
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)


DNI terminados en  4 o 5
1)informar la cantidad de personas de sexo  nb
2) la edad promedio de  personas de sexo  femenino
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)


DNI terminados en  6 o 7
1)informar la cantidad de personas mayores de edad (desde los 18 años)
2)la edad promedio en total de todas las personas mayores de edad (18 años)
3) el nombre de la persona  la persona de sexo  masculino con la temperatura mas baja(si la hay)


DNI terminados en  8 o 9
1))informar la cantidad de personas menores de edad (menos de 18 años)
2)la temperatura promedio en total de todas las personas menores de edad
3) el nombre de la persona de sexo  femenino  con la temperatura mas baja(si la hay)

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        cantidad_personas = 0

        cantidad_f = 0
        cantidad_m = 0
        cantidad_nb = 0

        cantidad_con_fiebre= 0
        cantidad_sin_fiebre = 0

        acomulador_edad_f = 0

        bandera = True
        masculino_menor_temperatura = 0
        nombre_masculino_menor_temperatura = 0

        while cantidad_personas < 5:
            cantidad_personas += 1

            nombre = prompt(None, "ingrese el nombre")
            temperatura = int(prompt(None,"ingrese la temperatura (entre 35 y 42)"))
            while (temperatura < 35) or (temperatura > 42):
                temperatura = int(prompt(None,"reingrese la temperatura (entre 35 y 42)"))
            
            if temperatura > 37:
                cantidad_con_fiebre += 1
            else:
                cantidad_sin_fiebre += 1

            sexo = prompt(None,"ingrese el sexo ( f, m , nb )")
            edad = int(prompt(None,"ingrese la edad"))

            if sexo == "f":
                cantidad_f += 1
                acomulador_edad_f += edad
            elif sexo == "m":
                cantidad_m += 1
                if bandera or temperatura < masculino_menor_temperatura:
                    masculino_menor_temperatura = temperatura
                    nombre_masculino_menor_temperatura = nombre
                    bandera = False
            elif sexo == "nb":
                cantidad_nb += 1

        # Punto B - El porcentaje de personas con fiebre y el porcentaje sin fiebre
        if cantidad_con_fiebre > 0:
            porcentaje_con_fiebre = (cantidad_con_fiebre / cantidad_personas) * 100
        else:
            porcentaje_con_fiebre = "No hay personas con fiebre"

        if cantidad_sin_fiebre > 0:
            porcentaje_sin_fiebre = (cantidad_sin_fiebre / cantidad_personas) * 100
        else:
            porcentaje_sin_fiebre = "No hay personas sin fiebre"


        if cantidad_f > 0:
            promedio_edad_f = int(acomulador_edad_f / cantidad_f)
        else:
            promedio_edad_f = "No hay sexo femenino"

        
        if (cantidad_f > cantidad_m) and (cantidad_f > cantidad_nb):
            sexo_mas_ingresado = "femenino"
        elif (cantidad_m > cantidad_f) and (cantidad_m > cantidad_nb):
            sexo_mas_ingresado = "masculino"
        else:
            sexo_mas_ingresado = "el sexo mas ingresado es nb"

        print(f"\t!PROGRAMA FINALIZADO!")
        print(f"A.  El Sexo mas ingresado es {sexo_mas_ingresado}")
        print(f"B.  El porcentaje de personas con fiebre es {porcentaje_con_fiebre} % y sin fiebre es {porcentaje_sin_fiebre} %")
        print(f"C1. Cantidad de personas NB es {cantidad_nb}")
        print(f"C2. Promedio de edad femenino es {promedio_edad_f}")
        print(f"C3. Nombre de la persona con la temperatura mas baja es {nombre_masculino_menor_temperatura}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
