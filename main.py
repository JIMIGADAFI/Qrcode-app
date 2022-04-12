#import tkinter for gui creation
from tkinter import *
# import pil to resize image
from PIL import Image,ImageTk
#import qrcode to create the qrcode
import qrcode
#import message box f rom tkinter to display messages
from tkinter import messagebox
#function to save qrcode
def save():
    #get file name from tkinter variable
    file=filename.get()
    #saving to the format png show append png at end of filename
    file=file+'.png'
    #get link from tkinter variable
    info=link.get()
    #create the qrcode
    img = qrcode.make(info)
    #save the Qrcode
    img.save(file)
    #display message that file has been saved successfully
    messagebox.showinfo('info','Qrcode saved successfully\nin your current working directory')
#create app main window name it as app
app=Tk()
#set app background_color to white
app.config(bg='white')
#set app size 
app.geometry('300x250')
#set app title
app.title('Qrcode creator')
#load image to be set as logo
image=Image.open('C:\\Users\\g\\AppData\\Local\\Programs\\Python\\Python38\\logo2.png')
#resize image and make it suitable in tkinter
r=image.resize((100,100))
img=ImageTk.PhotoImage(r)
#label to display logo
image=Label(image=img).pack()
#label to show user positon of entering link
lab1=Label(text='link/info to embbede ',bg='white',fg='black').pack()
#create a tkinter variable to store link
link=StringVar()
#create entry box were users enter link
entry=Entry(textvariable=link).pack()
#label for file name
lab1=Label(text='filename to save us',bg='white',fg='black').pack()
#tkinter variable for filename
filename=StringVar()
#entry box for file name 
entry=Entry(textvariable=filename).pack()
#button to call the save function
Button1=Button(text='save Qrcode',command=save,bg='black',fg='white').pack()
#this is to run the app and wait for user  action
app.mainloop()
