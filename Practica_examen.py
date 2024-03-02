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
De 5  mascotas que ingresan a una veterinaria  se deben tomar y validar los siguientes datos.

Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M  )
Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:
Informe X A- Cuál fue el sexo menos ingresado (F o M).
Informe X B- El porcentaje de mascotas que hay por tipo (gato ,perro o exotico).
Informe X C- El nombre y tipo de la mascota menos pesada.
Informe X D- El nombre del perro más joven.
Informe E- El promedio de peso de todas las mascotas.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        contador_sexo_F = 0
        contador_sexo_M = 0

        contador_gatos = 0
        contador_perros = 0
        contador_exoticos = 0

        primer_mascota_ingresada = True

        acumulador_peso_total = 0
        
        for i in range(5):
            print(f"\tINGRESE NUEVO DATO:")

            nombre = input("Ingrese nombre: ")
            tipo = input("Ingrese tipo (gato ,perro o exotico): ")
            while tipo != "gato" and tipo != "perro" and tipo != "exotico":
                tipo = input("Reingrese tipo (gato ,perro o exotico): ")
            peso = int(input("Ingrese peso Kg(entre 10 y 80): "))
            while peso < 10 or peso > 80:
                peso = int(input("Reingrese peso (entre 10 y 80): "))
            sexo = input("Ingrese sexo (F o M): ")
            while sexo != "F" and sexo != "M":
                sexo = input("Reingrese sexo (F o M): ")
            edad = int(input("Ingrese edad (mayor a 0): "))
            while edad < 1:
                edad = int(input("Reingrese edad (mayor a 0): "))

            match sexo:
                case "F":
                    contador_sexo_F += 1
                case "M":
                    contador_sexo_M += 1

            match tipo:
                case "gato":
                    contador_gatos += 1
                case "perro":
                    if contador_perros == 0 or edad < edad_perro_mas_joven:
                        edad_perro_mas_joven = edad
                        nombre_perro_mas_joven = nombre
                    contador_perros += 1
                case "exotico":
                    contador_exoticos += 1

            if primer_mascota_ingresada or peso < peso_menos_pesado:
                peso_menos_pesado = peso
                nombre_menos_pesada = nombre
                tipo_menos_pesada = tipo

                primer_mascota_ingresada = False
        
            acumulador_peso_total += peso

        if contador_sexo_F < contador_sexo_M:
            sexo_menos_ingresado = "F"
        else:
            sexo_menos_ingresado = "M"

        porcentaje_gatos = (contador_gatos / 5) * 100
        porcentaje_perros = (contador_perros / 5) * 100
        porcentaje_exoticos = (contador_exoticos / 5) * 100

        promedio_peso_total = acumulador_peso_total / 5

        print(f"\tINFORME:")
        # A)
        print(f"A) El sexo menos ingresado es '{sexo_menos_ingresado}'.")

        # B)
        print(f"B) El porcentaje de mascotas es: {porcentaje_gatos}% gatos, {porcentaje_perros}% perros, {porcentaje_exoticos}% exóticos.")

        # C)
        print(f"C) La mascota con menos peso fue {nombre_menos_pesada} de tipo {tipo_menos_pesada}.")

        # D)
        if contador_perros > 0:
            print(f"D) El perro mas joven fue {nombre_perro_mas_joven} con {edad_perro_mas_joven} años.")
        else:
            print(f"D) No hay perros registrados.")

        # F)
        print(f"F) El promedio de peso de todas las mascotas es de {promedio_peso_total} Kg.")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
