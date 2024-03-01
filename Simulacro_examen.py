import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Bruno
apellido: Freijomil
---
Simulacro Turno Noche

Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

    Nombre

    Importe ganado (mayor o igual $1000)

    Género (“Femenino”, “Masculino”, “Otro”)

    Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

1) Nombre y género de la persona que más ganó.

2) Promedio de dinero ganado en Ruleta.

3) Porcentaje de personas que jugaron en el Tragamonedas.

4) Cuál es el juego menos elegido por los ganadores.

5) El nombre del jugador que ganó más dinero jugando Poker

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_mostrar_iteracion = customtkinter.CTkButton(master=self, text="Mostrar iteración", command=self.btn_mostrar_iteracion_on_click)
        self.btn_mostrar_iteracion.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_mostrar_iteracion_on_click(self):
        seguir = True
        contador_personas_totales = 0

        contador_juegos_ruleta = 0
        acumulador_juegos_ruleta = 0

        contador_juegos_tragamonedas = 0

        contador_juegos_poker = 0

        while seguir:
            contador_personas_totales += 1

            print(f"\tINGRESE NUEVOS DATOS:")
            nombre = input("Ingrese nombre: ")
            importe_ganado = int(input("Ingrese importe ganado (mayor o igual $1000): "))
            while (importe_ganado < 1000):
                importe_ganado = int(input("Reingrese importe ganado (mayor o igual $1000): "))
            genero = input("Ingrese genero (Masculino, Femenino, Otro): ")

            while (genero != "Masculino" and genero != "Femenino" and genero != "Otro"):
                genero = input("Reingrese genero (Masculino, Femenino, Otro): ")

            juego = input("Ingrese juego (Ruleta, Poker, Tragamonedas): ")
            while (juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas"):
                juego = input("Reingrese juego (Ruleta, Poker, Tragamonedas): ")

            if contador_personas_totales == 1 or importe_ganado > importe_mayor_ganado:
                importe_mayor_ganado = importe_ganado
                nombre_mayor_ganado = nombre
                genero_mayor_ganado = genero

            match juego:
                case "Ruleta":
                    contador_juegos_ruleta += 1
                    acumulador_juegos_ruleta += importe_ganado
                case "Tragamonedas":
                    contador_juegos_tragamonedas += 1
                case "Poker":
                    contador_juegos_poker += 1
                    if contador_juegos_poker == 1 or importe_ganado > importe_mayor_poker:
                        importe_mayor_poker = importe_ganado
                        nombre_mayor_poker = nombre
                        
            seguir = question("¿Desea continuar?","")


        if contador_juegos_ruleta > 0:
            promedio_juegos_ruleta = f"$ {acumulador_juegos_ruleta / contador_juegos_ruleta}"
        else:
            promedio_juegos_ruleta = "(No se jugó Ruleta)"


        if contador_juegos_tragamonedas > 0:
            porcentaje_juegos_tragamonedas = f"{(100 * contador_juegos_tragamonedas) / contador_personas_totales}%"
        else:
            porcentaje_juegos_tragamonedas = "(No se jugó Tragamonedas)"


        if contador_juegos_ruleta < contador_juegos_tragamonedas and contador_juegos_ruleta < contador_juegos_poker:
            juego_menos_elegido = "Ruleta"
        elif contador_juegos_tragamonedas < contador_juegos_ruleta and contador_juegos_tragamonedas < contador_juegos_poker:
            juego_menos_elegido = "Tragamonedas"
        elif contador_juegos_poker < contador_juegos_ruleta and contador_juegos_poker < contador_juegos_tragamonedas:
            juego_menos_elegido = "Poker"
        else:
            juego_menos_elegido = "(Ninguno / Hay empate)"


        print(f"\t ¡PROGRAMA FINALIZADO!")
        # 1)
        print(f"Nombre y genero de la persona que mas ganó: {nombre_mayor_ganado} / {genero_mayor_ganado}")

        # 2)
        print(f"Promedio de dinero ganado en Ruleta: {promedio_juegos_ruleta}")

        # 3)
        print(f"Porcentaje de personas que jugaron en Tragamonedas: {porcentaje_juegos_tragamonedas}")

        # 4)
        print(f"Juego menos elegido por los ganadores: {juego_menos_elegido}")

        # 5)
        if contador_juegos_poker > 0:
            print(f"El nombre del jugador que ganó mas dinero jugando Poker: {nombre_mayor_poker}")
        else:
            print("El nombre del jugador que ganó mas dinero jugando Poker: (Nadie jugó Poker)")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()