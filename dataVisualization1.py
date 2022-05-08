from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter.filedialog import askopenfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('SEE Project')
root.geometry("400x200")




def upload_file():
    filepath=filedialog.askopenfilename()
    label_file["text"] = filepath 
    my_button2.pack()
    return None
 
    
def graph():
    file_path = label_file["text"]
    csv_filename = r"{}".format(file_path)
    df = pd.read_csv(csv_filename)
    albania_df = df[df['WHOR']=="Europe"]
 

    plt.pie(albania_df['Deaths'],labels=albania_df['Country'])
    plt.show()


# Manage_Frame = Frame(root, bd=4, relief=RIDGE, bg="blue")
# Manage_Frame.place(x=20,y=100, width=450,height=560)

label_file = Label(root, text ="No File Selected")
label_file.place(rely=0,relx=0)
my_button = Button(root, text="Upload CSV File",  command=upload_file)
my_button.pack()
my_button2 = Button(root, text="Data Visualized",  command=graph)


src = StringVar()
l2 = Label(root, textvariable=src, fg="red")
l2.pack()


root.mainloop()