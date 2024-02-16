import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Bruno
apellido: Freijomil
---
Ejercicio: while_05
---
Enunciado:
Al presionar el botón ‘Validar letra’, mediante prompt solicitar al usuario que ingrese una letra. 
Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas). 
En caso no coincidir con ninguna de las letras, volver a solicitarla hasta que la condición se cumpla.
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        prompt_letra = prompt(title="Validar letra", prompt="Ingrese una letra")

        while prompt_letra != "U" and prompt_letra != "T" and prompt_letra != "N":
            mensaje= "Seleccione otra letra"
            alert(None, mensaje)
            prompt_letra = prompt(title="Validar letra", prompt="Ingrese una letra")
        
        mensaje = "Letra correcta!"
        alert(None, mensaje)
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()