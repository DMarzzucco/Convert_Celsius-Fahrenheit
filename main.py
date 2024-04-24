import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convertir_a_fahrenheit():
    try:
        celsius = float(celsius_scale.get())
        fahrenheit = round(celsius * 9 / 5 + 32, 1)
        result_label.config(text=f"{fahrenheit} Fahrenheit")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido para Celsius.")

def convertir_a_celsius():
    try:
        fahrenheit = float(fahrenheit_scale.get())
        celsius = round((fahrenheit - 32) * 5 / 9, 1)
        result_label.config(text=f"{celsius} Celsius")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido para Fahrenheit.")

app = tk.Tk()
app.title("Convertidor de Temperatura")
app.geometry("400x300")
app.configure(bg="#282C34")

style = ttk.Style()
style.configure("TScale", font=("Arial", 12))

frame1 = tk.Frame(app, bg="#282C34")
frame1.pack(pady=20)

tk.Label(frame1, text="Celsius", font=("Arial", 12), bg="#282C34").grid(row=0, column=0, padx=10)
celsius_scale = ttk.Scale(frame1, from_=-50, to=50, length=200, orient="horizontal", style="TScale")
celsius_scale.grid(row=0, column=1, padx=10)

convertir_f_btn = tk.Button(frame1, text="Convertir a Fahrenheit", font=("Arial", 12), command=convertir_a_fahrenheit)
convertir_f_btn.grid(row=1, columnspan=2, pady=10)

frame2 = tk.Frame(app, bg="#282C34")
frame2.pack(pady=20)

tk.Label(frame2, text="Fahrenheit", font=("Arial", 12), bg="#282C34").grid(row=0, column=0, padx=10)
fahrenheit_scale = ttk.Scale(frame2, from_=-58, to=122, length=200, orient="horizontal", style="TScale")
fahrenheit_scale.grid(row=0, column=1, padx=10)

convertir_c_btn = tk.Button(frame2, text="Convertir a Celsius", font=("Arial", 12), command=convertir_a_celsius)
convertir_c_btn.grid(row=1, columnspan=2, pady=10)

result_label = tk.Label(app, text="Resultado", font=("Arial", 16), bg="#282C34")
result_label.pack(pady=20)

app.mainloop()
