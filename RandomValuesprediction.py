from tkinter import *
import tkinter as tk
import joblib
import numpy as np

def Detect():
    e1 = FileNo.get()
    e2 = Age.get()
    e3 = Weight.get()
    e4 = Height.get()
    e5 = Pulserate.get()
    e6 = RR.get()
    e7 = Hb.get()
    e8 = Cyclelength.get()
    e9 = FollicleNo.get()
    e10 = Endometrium.get()

    try:
        # Load the trained model
        model = joblib.load("F:/2023 project code/Machine Learning Approaches on Polycystic Ovary Syndrome/PCOS 100% Code/SVM_PCOS.joblib")

        # Prepare the input data
        input_data = np.array([[e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]])

        # Make the prediction
        prediction = model.predict(input_data)

        if prediction[0] == 0:
            print("PCOS Not Detected")
            result_label.config(text="PCOS Not Detected", bg="green")
        elif prediction[0] == 1:
            print("PCOS Detected")
            result_label.config(text="PCOS Detected", bg="brown")

    except:
        print("Invalid input values")
        result_label.config(text="Invalid input values", bg="red")


root = tk.Tk()
root.geometry("1700x1550")
root.title("Machine Learning Approaches On Polycystic Ovary Syndrome")
root.configure(background="#152238")

# Define the variables
FileNo = tk.IntVar()
Age = tk.IntVar()
Weight = tk.IntVar()
Height = tk.IntVar()
Pulserate = tk.IntVar()
RR = tk.IntVar()
Hb = tk.IntVar()
Cyclelength = tk.IntVar()
FollicleNo = tk.IntVar()
Endometrium = tk.IntVar()

# Create the labels and entry fields
labels = ["FileNo", "Age", "Weight", "Height", "Pulserate", "RR", "Hb", "Cyclelength", "FollicleNo", "Endometrium"]
entries = [FileNo, Age, Weight, Height, Pulserate, RR, Hb, Cyclelength, FollicleNo, Endometrium]

for i in range(len(labels)):
    label = tk.Label(root, text=labels[i], background="olive", font=('times', 20, 'bold'), width=20)
    label.place(x=400, y=50 + i * 50)
    entry = tk.Entry(root, bd=2, width=15, font=("TkDefaultFont", 20), textvar=entries[i])
    entry.place(x=800, y=50 + i * 50)

# Create the result label
result_label = tk.Label(root, text="", background="white", font=('times', 20, 'bold'), width=20)
result_label.place(x=630, y=650)

# Create the submit button
button1 = tk.Button(root, text="Submit", command=Detect, font=('times', 20, 'bold'), width=10)
button1.place(x=660, y=580)

root.mainloop()