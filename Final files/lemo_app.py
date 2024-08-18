import tkinter as tk
import tkinter.messagebox as tkm
import tkinter.simpledialog as tks
import tkinter.filedialog as tkf
import pyautogui as pya
import numpy as np

def lemo_change(bills): #checks the bills
    five , ten = 0, 0
    for i in bills:
        if i == 5:
            five += 1
        elif i == 10:
            if five == 0:
                return 10, False
            five -= 1
            ten += 1
        else:
            if ten > 0:
                ten -= 1
                if five == 0:
                    return 15, False
                five -= 1
            else:
                if five < 3:
                    return 15, False
                five -= 3
    return 0, True

def calculate_change():
    bills_str = entry.get()
    bills = list(map(int, bills_str.split(' ')))
    if lemo_change(bills) == (0, True):
        tkm.showinfo("Result", "All customers have got their change back.")
    else:
        left_money = lemo_change(bills)[0]
        tkm.showinfo("Result", f"The shopkeeper has {left_money} rupees left.")
        
# create the window
root = tk.Tk()
root.title("Lemo Change")
root.geometry("500x500")
root.config(bg="lightblue")
root.resizable(False, False)

label = tk.Label(root, text="Enter the number of bills: ") # Title widget
label.pack()
label.config(bg="aquamarine", fg="black", font=("Poppins", 20, "bold"))

entry = tk.Entry(root) # Entry widget
entry.pack()
entry.config(fg="black", bg="lightblue")
entry.config(border=5, relief="sunken", font=("Arial", 20), width=20, justify="center")

button = tk.Button(root, text="Calculate", command=calculate_change) # Calculate button
button.pack()
button.config(bg="blue", fg="white", width=16 , activebackground="darkblue", activeforeground="white")

result_label = tk.Label(root, text="") # Results area
result_label.pack()
result_label.config(fg="red", bg="lightblue", font=("Arial", 16, "bold", "underline"))

def show_result():
    bills_str = entry.get()
    bills = list(map(int, bills_str.split(' ')))
    if lemo_change(bills) == (0, True):
        result_label.config(text="All customers have got their change back.", bg="green")
    else:
        left_money = lemo_change(bills)[0]
        result_label.config(text=f"The shopkeeper has {left_money} rupees left.", bg="red")
        result_label.config(fg="white")

show_result_button = tk.Button(root, text="Show Result", command=show_result) #Results Button
show_result_button.pack()
show_result_button.config(bg="blue", fg="white", width=16 , activebackground="darkblue", activeforeground="white")

root.mainloop()