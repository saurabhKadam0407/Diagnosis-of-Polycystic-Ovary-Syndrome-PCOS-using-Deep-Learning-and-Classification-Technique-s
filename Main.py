

import tkinter  as tk 
from tkinter import * 

from tkvideo import tkvideo
# from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
# from PIL import Image , ImageTk  
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1
root = tk.Tk()
#root.geometry('500x500')
#root.title("Login Form")


#------------------------------------------------------

#root.configure(background="seashell2")
#root.geometry("1300x700")


# w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# root.geometry("%dx%d+0+0" % (w, h))
root.title("main")
#------------------Frame----------------------

# image2 =Image.open('A.jpg')
# image2 =image2.resize((750,890), Image.ANTIALIAS)

# background_image=ImageTk.PhotoImage(image2)
# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=250, y=0) #, relwidth=1, relheight=1)
# #
# def shift():
#     x1,y1,x2,y2 = canvas.bbox("marquee")
#     if(x2<0 or y1<0): #reset the coordinates
#         x1 = canvas.winfo_width()
#         y1 = canvas.winfo_height()//2
#         canvas.coords("marquee",x1,y1)
#     else:
#         canvas.move("marquee", -2, 0)
#     canvas.after(1000//fps,shift)

# canvas=tk.Canvas(root,bg="maroon")
# canvas.pack()
# text_var="Form Based Document Using OCR Using Machine Learning_Crime & Fake Document Prediction"
# text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
# x1,y1,x2,y2 = canvas.bbox("marquee")
# width = 1600
# height = 100
# canvas['width']=width
# canvas['height']=height
# fps=40    #Change the fps to make the animation faster/slower
# shift()


#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "GUI_Master_old.py"])   



def login():
    
##### tkinter window ######
    
    print("log")
    from subprocess import call
    call(["python", "GUI_MASTER.py"])   
    


def window():
    root.destroy()
    from subprocess import call
    call(["python", "GUI_main.py"])   

#++++++++++++++++++++++++++++++++++++++++++++
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("PCOS detection using Machine learning ")
video_label =tk.Label(root)
video_label.pack()
#read video to display on label
player = tkvideo("v.mp4", video_label,loop = 1, size = (w, h))
player.play()
#####For background Image
# image2 =Image.open('D1.jpg')
# image2 =image2.resize((1400,700), Image.ANTIALIAS)

# background_image=ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=100, y=100) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Machine Learning Approaches On Polycystic Ovary Syndrome", font=('times', 40,' bold '), height=1, width=50,bg="BLACK",fg="white")
lbl.place(x=0, y=0)

# framed = tk.LabelFrame(root, text=" --WELCOME-- ", width=400, height=300, bd=5, font=('times', 14, ' bold '),bg="GRAY")
# framed.grid(row=0, column=0, sticky='nw')
# framed.place(x=200, y=200)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
button1 = tk.Button(text='TEXT',width=15,height=2,bd=5,bg='#152238',font=('times', 15, ' bold '),fg='white',command=login).place(x=100,y=200)
button1 = tk.Button(text='IMAGE',width=15,height=2,bd=5,bg='#152238',font=('times', 15, ' bold '),fg='white',command=reg).place(x=100,y=300)
exit = tk.Button(text="Back", command=window, width=15, height=2, bd=5,font=('times', 15, ' bold '),bg="red",fg="white").place(x=100, y=400)

root.mainloop()
