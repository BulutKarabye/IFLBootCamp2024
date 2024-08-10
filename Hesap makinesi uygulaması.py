from tkinter import Tk
from tkinter import Button
from tkinter import LEFT
from tkinter import Entry
from tkinter import Label

pencere = Tk()
pencere.title("Hesap Makinesi")
pencere.geometry("300x200")

mk1 = Label(pencere, text="Birinci sayıyı giriniz:",font=1)
mk2 = Label(pencere, text="İkinci sayıyı giriniz:",font=1)
mk3 = Label(pencere, text="Sonuç", background="Blue", fg="#FFFFFF", font=60, width=15, height=1)
mk1.place(x=25,y=10)
mk2.place(x=25,y=50)
mk3. place(x=25, y=130)

giriş1 = Entry(pencere, text="",font=1, width=8)
giriş1.insert(string="", index=0)
giriş2 = Entry(pencere, text="", font=1,width=8)
giriş2.insert(string="", index=0)
giriş1.place(x=200, y=10)
giriş2.place(x=200, y=50)


def topla():
    try:
        sayı1 = (giriş1.get())
        sayı2 = (giriş2.get())
        sonuç = str(float(sayı1) + float(sayı2))
        mk3.config(text = sonuç, bg="#FF9933", fg="#000000")
    except ValueError:
        print("Yapılan giriş sayı olmalıdır.")

def çıkar():
    try:
        sayı1 = (giriş1.get())
        sayı2 = (giriş2.get())
        sonuç = str(float(sayı1) - float(sayı2))
        mk3.config(text = sonuç, bg="#FF9933", fg="#000000")
    except ValueError:
        print("Yapılan giriş sayı olmalıdır.")

def çarp():
    try:
        sayı1 = (giriş1.get())
        sayı2 = (giriş2.get())        
        sonuç = str(float(sayı1) * float(sayı2))
        mk3.config(text = sonuç, bg="#FF9933", fg="#000000")
    except ValueError:
        print("Yapılan giriş sayı olmalıdır.")

def böl():
    try:
        sayı1 = (giriş1.get())
        sayı2 = (giriş2.get())
        if sayı2 == "0":
            print("Sıfıra bölünemez")
        else:
            sonuç = str(round(float(sayı1) / float(sayı2),2))
            mk3.config(text = sonuç, bg="#FF9933", fg="#000000")
    except ValueError:
        print("Yapılan giriş sayı olmalıdır.")
    
    

tuş1 = Button(pencere, text="+", background="#FF9933", fg="#603300", activebackground="#FF0000",width=2,height=1,font=1, command=topla)
tuş1.place(x=25, y=85)
tuş2 = Button(pencere, text="-", background="#FF9933", fg="#603300", activebackground="#FF0000",width=2,height=1,font=1, command=çıkar)
tuş2.place(x=70, y=85)
tuş3 = Button(pencere, text="x", background="#FF9933", fg="#603300", activebackground="#FF0000",width=2,height=1,font=1, command=çarp)
tuş3.place(x=115, y=85)
tuş4 = Button(pencere, text=":", background="#FF9933", fg="#603300", activebackground="#FF0000",width=2,height=1,font=1, command=böl)
tuş4.place(x=160, y=85)

pencere.mainloop()

