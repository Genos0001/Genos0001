import num2words as n2w
import tkinter as tk

root = tk.Tk()
root.title("Number to Words")
root.geometry("500x500")
root.config(bg="lightblue")

label = tk.Label(root, text="Enter a number: ")
label.pack()
label.config(bg="aquamarine", font=("Algerian", 20), padx=10, pady=10)

entry = tk.Entry(root)
entry.pack()
entry.config(fg="black", bg="lightblue")
entry.config(border=5, relief="sunken", font=("Arial", 20), width=20, justify="center")

result_label = tk.Label(root, text="")
result_label.pack()
result_label.config(fg="red", bg="#B0E0E6", font=("Arial", 18), width=20, height=8, justify="center")
result_label.config(relief="sunken", border=5)

try:
    def show_result():
        return lambda : result_label.config(text=n2w.num2words(int(entry.get())))
except ValueError:
    result_label.config(text="Please input numbers only.")
except TypeError:
    result_label.config(text="Please input numbers only.")
except ZeroDivisionError:
    result_label.config(text="Please input numbers only.")
    
button = tk.Button(root, text="Convert", command= show_result())
button.pack()
button.config(fg="yellow", bg="grey", font=("Courier", 14), width= 12 )

errormsg_label = tk.Label(root, text="Please input numbers only.")
errormsg_label.pack()
errormsg_label.config(bg="red", fg="yellow", font=("Times New Roman Italic", 18), height=2)
errormsg_label.config(relief="raised", border=5)

root.mainloop()

