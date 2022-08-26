from tkinter import *


def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def calculate():
    height_get = entry_height.get()
    weight_get = entry_weight.get()
    if isfloat(height_get) or isfloat(weight_get) is False:
        label_error = Label(root, text="NOT A NUMBER!")
        label_error.grid(row=2, column=0)
    else:
        pass
    height = float(height_get)
    weight = float(weight_get)
    imc = weight / (height * height)
    imc_label = Label(root, text=f"Your imc is: {round(imc, 2)}")
    imc_label.grid(row=2, column=0)


# Creating the window and changing the tittle
root = Tk()
root.title("Imc Calculator")

# Height label
label_height = Label(root, text="Heigth: ")
label_height.grid(row=0, column=0)

# Weight label
label_weight = Label(root, text="Weight: ")
label_weight.grid(row=1, column=0)

# Height Entry
entry_height = Entry(root, width=30)
entry_height.grid(row=0, column=1)

# Weight Entry
entry_weight = Entry(root, width=30)
entry_weight.grid(row=1, column=1)

# Calculate Button
button_calculate = Button(root, text="Calculate!", command=calculate)
button_calculate.grid(row=2, column=1)

root.mainloop()