import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Bruno
apellido: Freijomil
---
TP: Iluminación
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = int(self.combobox_cantidad.get())
        precio_total = cantidad * 800

        match marca, cantidad:
            case "ArgentinaLuz", 3:
                precio_con_descuento = precio_total * 0.15
                mensaje = f"TOTAL ${precio_total} \n El precio final con 15% de descuento es ${precio_con_descuento}"

            case "FelipeLamparas", 3:
                precio_con_descuento = precio_total * 0.10
                mensaje = f"TOTAL ${precio_total} \n El precio final con 10% de descuento es ${precio_con_descuento}"

            case "JeLuz" | "HazIluminacion" | "Osram", 3:
                precio_con_descuento = precio_total * 0.05
                mensaje = f"TOTAL ${precio_total} \n El precio final con 5% de descuento es ${precio_con_descuento}"

            case "ArgentinaLuz" | 'FelipeLamparas', 4:
                precio_con_descuento = precio_total * 0.25
                mensaje = f"TOTAL ${precio_total} \n El precio final con 25% de descuento es ${precio_con_descuento}"

            case "JeLuz" | "HazIluminacion" | "Osram", 4:
                precio_con_descuento = precio_total * 0.20
                mensaje = f"TOTAL ${precio_total} \n El precio final con 20% de descuento es ${precio_con_descuento}"

            case "ArgentinaLuz" , 5 :
                precio_con_descuento = precio_total * 0.4
                mensaje = f"TOTAL ${precio_total} \n El precio final con 40% de descuento es ${precio_con_descuento}"

            case "FelipeLamparas" | "JeLuz" | "HazIluminacion" | "Osram", 5:
                precio_con_descuento = precio_total * 0.3
                mensaje = f"TOTAL ${precio_total} \n El precio final con 30% de descuento es ${precio_con_descuento}"

            case "ArgentinaLuz" | "FelipeLamparas" | "JeLuz" | "HazIluminacion" | "Osram", 1 | 2 | 3 | 4 | 5:
                mensaje = f"TOTAL ${precio_total} \n El precio final es ${precio_total}"

            case "ArgentinaLuz" | "JeLuz" | "HazIluminacion" | "Osram", 6 | 7 | 8 | 9 | 10 | 11 | 12:
                precio_con_descuento = precio_total * 0.5

                if precio_con_descuento > 4000:
                    descuento_adicional = precio_con_descuento * 0.05
                    precio_final_adicional = precio_con_descuento - descuento_adicional
                    mensaje = f"TOTAL ${precio_total} \n El precio con 50% de descuento (${precio_con_descuento}) \n+ 5% de DESCUENTO ADICIONAL es = ${precio_final_adicional}"
                else:
                    mensaje = f"TOTAL ${precio_total} \n El precio final con 50% de descuento es ${precio_con_descuento}"

        alert(None, mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()