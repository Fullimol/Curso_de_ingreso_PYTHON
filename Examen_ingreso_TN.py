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

De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos

Marca (no validar)
Categoría (peligroso, comestible, indumentaria)
Peso ( entre 100 y 800)
Tipo de material ( aluminio, hierro , madera)
Costo en $ (mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:
Informe X A- Cuál fue tipo de material menos usado (aluminio, hierro , madera).
Informe X B- El porcentaje de contenedores por Categoría (peligroso, comestible, indumentaria).
Informe X C- La marca y tipo del contenedor más costoso.
Informe X D- La marca del contenedor de aluminio con mayor costo.
Informe X E- El promedio de costo de todos los contenedores.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):

        contador_aluminio = 0
        contador_hierro = 0
        contador_madera = 0

        contador_categoria_peligroso = 0
        contador_categoria_comestible = 0
        contador_categoria_indumentaria = 0

        bandera_primer_contenedor = True

        acumulador_costo_total = 0
        
        for i in range(20): 
            print(f"\n\tINGRESAR NUEVO DATO {i+1}:")

            marca = input("Ingrese marca: ")  
            categoria = input("Ingrese categoria (peligroso, comestible, indumentaria): ")
            while (categoria != "peligroso" and categoria != "comestible" and categoria != "indumentaria"):
                categoria = input("RE Ingrese categoria (peligroso, comestible, indumentaria): ")
            peso = int(input("Ingrese peso (entre 100 y 800): "))
            while (peso < 100 or peso > 800):
                peso = int(input("RE Ingrese peso (entre 100 y 800): "))
            material = input("Ingrese tipo de material (aluminio, hierro , madera): ")
            while (material != "aluminio" and material != "hierro" and material != "madera"):
                material = input("RE Ingrese tipo de material (aluminio, hierro , madera): ")
            costo = int(input("Ingrese costo (mayor a 0): "))
            while (costo <= 0):
                costo = int(input("RE Ingrese costo (mayor a 0): "))

            match material:
                case "aluminio":
                    # D- La marca del contenedor de aluminio con mayor costo
                    if contador_aluminio == 0 or costo > aluminio_mayor_costo:
                        aluminio_mayor_costo = costo
                        marca_aluminio_mayor_costo = marca

                    contador_aluminio += 1
                case "hierro":
                    contador_hierro += 1
                case "madera":
                    contador_madera += 1

            match categoria:
                case "peligroso":
                    contador_categoria_peligroso += 1
                case "comestible":
                    contador_categoria_comestible += 1
                case "indumentaria":
                    contador_categoria_indumentaria += 1
            
            # C- La marca y tipo del contenedor más costoso
            if bandera_primer_contenedor or costo > contenedor_mas_costoso:
                contenedor_mas_costoso = costo
                marca_contenedor_mas_costoso = marca
                tipo_contenedor_mas_costoso = material

                bandera_primer_contenedor = False

        # E- El promedio de costo de todos los contenedores
            acumulador_costo_total += costo

        promedio_costo_total = acumulador_costo_total / 20

        # A- Cuál fue tipo de material menos usado ( aluminio, hierro , madera)
        if contador_aluminio < contador_hierro and contador_aluminio < contador_madera:
            material_menos_usado = "aluminio"
        elif contador_hierro < contador_aluminio and contador_hierro < contador_madera:
            material_menos_usado = "hierro"
        elif contador_madera < contador_aluminio and contador_madera < contador_hierro:
            material_menos_usado = "madera"
        else:
            material_menos_usado = "Ninguno/Empate"
        
        # B- El porcentaje de contenedores por Categoría (peligroso, comestible, indumentaria)
        porcentaje_peligroso = (contador_categoria_peligroso / 20) * 100
        porcentaje_comestible = (contador_categoria_comestible / 20) * 100
        porcentaje_indumentaria = (contador_categoria_indumentaria / 20) * 100

        print(f"\n\tINFORME FINAL:")
        # A)
        print(f"A) Material menos usado: {material_menos_usado}.")

        # B)
        print(f"B) Porcentaje de contenedores por categoria es: {porcentaje_peligroso}% peligroso, {porcentaje_comestible}% comestible, {porcentaje_indumentaria}% indumentaria.")

        # C)
        print(f"C) El contenedor mas costoso es de la marca '{marca_contenedor_mas_costoso}' y es de tipo '{tipo_contenedor_mas_costoso}'.")

        # D)
        if contador_aluminio == 0:
            print(f"D) No hay contenedores de aluminio.")
        else:
            print(f"D) El contenedor de aluminio con mayor costo es marca '{marca_aluminio_mayor_costo}.'")

        # E)
        print(f"E) El promedio de costo de todos los contenedores es de '${promedio_costo_total}.'")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
