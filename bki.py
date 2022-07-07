from tkinter import *

window = Tk()
window.title("Mustafa Akipek 20217170030")
window.geometry("500x500+450+150")
window.configure(bg="blue")

def hesapla():
    BKI = int(kilo_girdisi.get())/(float(boy_girdisi.get())*float(boy_girdisi.get()))
    if BKI < 18.5:
        durum.config(text="Zayif")
    elif 18.5 < BKI <= 25:
        durum.config(text="Normal")
    elif 25 < BKI <= 30:
        durum.config(text="Fazla Kilolu")
    else:
        durum.config(text="Obez")

boy_kismi = Label(window,text="Boyunuzu Giriniz (Metre): ")
boy_kismi.place(x=150,y=10)

boy_girdisi = Entry(window)
boy_girdisi.place(x=150,y=40,width=150,height=20)


kilo_kismi = Label(window,text="Kilonuzu Giriniz (Kilogram): ")
kilo_kismi.place(x=150,y=75)

kilo_girdisi = Entry(window)
kilo_girdisi.place(x=150,y=105,width=150,height=20)

hesap = Button(window,text="Hesapla",command=hesapla,activebackground="purple")
hesap.place(x=150,y=140)

sonuc = Label(window,text="BKI Durumunuz: ")
sonuc.place(x=150,y=175)

durum = Label(window)
durum.place(x=150,y=200)

window.mainloop()