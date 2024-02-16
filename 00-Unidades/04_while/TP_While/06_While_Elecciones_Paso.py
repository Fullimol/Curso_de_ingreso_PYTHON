import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Bruno
apellido: Freijomil
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        candidatos = []
        
        while True:
            nombre = prompt(title="Validar nombre", prompt="Ingrese nombre")
            if nombre is None:
                break
            edad = prompt(title="Validar edad", prompt="Ingrese edad")
            if edad is None:
                break
            votos = prompt(title="Validar votos", prompt="Ingrese votos")
            if votos is None:
                break
            candidatos.append((nombre, int(edad), int(votos)))

            salir = prompt(title="Salir", prompt="¿Desea salir? (Sí/No)")
            if salir and salir.lower() == "si":
                break

        mensaje = "Candidatos registrados:\n"

        maximo = max(candidatos, key=lambda x: x[2])
        minimo = min(candidatos, key=lambda x: x[2])

        promedio_edades = sum(x[1] for x in candidatos) / len(candidatos)

        for candidato in candidatos:
            mensaje += f"Nombre: {candidato[0]}, Edad: {candidato[1]}, Votos: {candidato[2]}\n"

        alert(title="Candidatos Registrados", message=mensaje + f"\nCandidato con más votos: {maximo[0]} \nCandidato con menos votos: {minimo[0]} ({minimo[1]} años), Votos: {minimo[2]} \nPromedio de edades: {promedio_edades} \nTotal de votos: {sum(x[2] for x in candidatos)}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
