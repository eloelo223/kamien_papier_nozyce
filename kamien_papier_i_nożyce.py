import random as r
from tkinter import *

#tworzymy kolor
def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb  

#tworzymy okienko gry
root = Tk()
root.title('kamien,papier,nozyce')
root.config(bg=rgb_hack((255, 0, 122))) 



#tworzymy przeciwnika
def enemy():
    lista_przeciwnika = [papier,nozyce,kamien]
    przeciwnik = (lista_przeciwnika[r.randint(0,len(lista_przeciwnika)-1)])
    return przeciwnik


#tworzymy kamien papier i nożyce
kamien = "kamien"
papier = "papier"
nozyce = "nozyce"
mylabel3 = Label(root,text="wprowadz",bg=rgb_hack((255, 0, 122)))
mylabel3.grid(row=0,column=1)



#gra
ty = Entry(root)
ty.grid(row=0, column=2)
def Myclick():
    przeciwnik = enemy()
    if ty.get() == kamien and przeciwnik == nozyce:
        miec=('przeciwnik miał', przeciwnik)
        we=("wygrałeś")

    if ty.get() == kamien and przeciwnik == papier:
        miec=('przeciwnik miał', przeciwnik)
        we=("przegrałeś")

    if ty.get() == kamien and przeciwnik == kamien:
        miec=('przeciwnik miał', przeciwnik)
        we=("remis")
    if ty.get() == papier and przeciwnik == nozyce:
        miec=('przeciwnik miał', przeciwnik)
        we=("przegrałś")

    if ty.get() == papier and przeciwnik == papier:
        miec=('przeciwnik miał', przeciwnik)
        we=("remis")

    if ty.get() == papier and przeciwnik == kamien:
        miec=('przeciwnik miał', przeciwnik)
        we=("wygrałeś")

    if ty.get() == nozyce and przeciwnik == nozyce:
        miec=('przeciwnik miał', przeciwnik)
        we=("remis")

    if ty.get() == nozyce and przeciwnik == papier:
        miec=('przeciwnik miał', przeciwnik)
        we=("wygrałeś")

    if ty.get() == nozyce and przeciwnik == kamien:
        miec=('przeciwnik miał', przeciwnik)
        we=("przegrałeś")


    mylabel = Label(root,text=miec)
    mylabel.grid(row=4,column=2)
    mylabel2 = Label(root,text=we)
    mylabel2.grid(row=5,column=2)

#przyciski
def clear():
    mylabel = Label(root,text="                                                                          ",bg=rgb_hack((255, 0, 122)))
    mylabel.grid(row=4,column=2)
    mylabel = Label(root,text="                                                                          ",bg=rgb_hack((255, 0, 122)))
    mylabel.grid(row=5,column=2)

myButton = Button(root,text="wyczysc", command=clear,bg=rgb_hack((255, 0, 122)))
myButton.grid(row=4,column=1)


myButton = Button(root,text="sprawdz", command=Myclick,bg=rgb_hack((255, 0, 122)))
myButton.grid(row=3,column=1)
root.mainloop()