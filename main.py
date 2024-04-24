import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


def fahrenheit_convert():
	try:
		celsius = float(celsius_scale.get())
		fahrenheit = round(celsius * 9 / 5 + 32, 1)
		result_label.config(text=f"{fahrenheit} Fahrenheit")
		result_label.config(fg="#A5B11B")
	except ValueError:
		messagebox.showerror("Error", "wrong values")


def celsius_convert():
	try:
		fahrenheit = float(fahrenheit_scale.get())
		celsius = round((fahrenheit - 32) * 5 / 9, 1)
		result_label.config(text=f"{celsius} Celsius")
		result_label.config(fg="#22B14C")
	except ValueError:
		messagebox.showerror("Error", "wrong values")


app = tk.Tk()
app.title("Temperature Calculator")
app.geometry("600x800")
app.configure(bg="#282C34")

style = ttk.Style()
style.configure("TScale", font=("Arial", 12), background="#282C34")

button_img = Image.open("./img/Conv_btn.png")
button_photo = ImageTk.PhotoImage(button_img)

frame1 = tk.Frame(app, bg="#282C34")
frame1.pack(pady=20)

# C zu F
tk.Label(frame1, text="Celsius", fg="white", font=("Arial", 12), bg="#282C34").grid(row=0, column=0, padx=10)
celsius_scale = ttk.Scale(frame1, from_=-50, to=50, length=200, orient="horizontal", style="TScale")
celsius_scale.grid(row=0, column=1, padx=10)

convertir_f_btn = tk.Button(frame1, bg="#282C34", fg="white", border="1",
                            borderwidth="0", font=("Arial", 12), image=button_photo,
                            command=fahrenheit_convert)
convertir_f_btn.grid(row=1, columnspan=2, pady=10)

# F zu c

frame2 = tk.Frame(app, bg="#282C34")
frame2.pack(pady=20)

tk.Label(frame2, text="Fahrenheit", fg="white", font=("Arial", 12), bg="#282C34").grid(row=0, column=0, padx=10)
fahrenheit_scale = ttk.Scale(frame2, from_=-58, to=122, length=200, orient="horizontal", style="TScale")
fahrenheit_scale.grid(row=0, column=1, padx=10)

convertir_c_btn = tk.Button(frame2, font=("Arial", 12), bg="#282C34", borderwidth="0", image=button_photo,
                            command=celsius_convert)
convertir_c_btn.grid(row=1, columnspan=2, pady=10)

result_label = tk.Label(app, text="Resultado", font=("Arial", 16), fg="white", bg="#282C34")
result_label.pack(pady=20)

app.mainloop()
