# Imporation des modules tkinter et messagebox et affichage des images en jpg et de génération d'un entier aléatoire
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from random import randint

# Création de la fonction pour ouvrir l'image du code couleur
def code():
    img = Image.open("code.jpg")
    img.show()

# Découpage du nombre en plusieurs valeurs
def Decoupage_nombre(nbdec):
    n=0
    couleur1=nbdec
    couleur2=nbdec
    couleur3=nbdec
    couleur = [0]*4
    while nbdec>0 :
        nbdec=nbdec//10
        n=n+1
    for i in range(n-1) :
        couleur1=couleur1//10
    couleur[0]=couleur1%10
    for i in range(n-2) :
        couleur2=couleur2//10
    couleur[1]=couleur2%10
    for i in range(n-3) :
        couleur3=couleur3//10
    couleur[2]=couleur3%10
    couleur[3]=(n-3)
    return couleur

# Définition des erreurs
def erreur():
    messagebox.showinfo("ERREUR !", "Erreur ! La valeur de la résistance ne peut être négative.")
def erreur1():
    messagebox.showinfo("ERREUR !", "Erreur ! La valeur de la résistance ne peut être si élevée.")
def erreur2():
    messagebox.showinfo("ERREUR !", "Erreur ! La valeur de la résistance ne peut être nulle.")

# Fonction coloriant les bagues en fonction de la valeur de la résistance entrée et transformant afficher en effacer
def coloriage():
    nombre=int(ValResistance.get())
    coul = Decoupage_nombre(nombre)
    tabcouleur=["black","DarkOrange4","red","orange","yellow","forest green","deep sky blue","purple2","snow4","white"]
    if 999999999>nombre>99:
        ZoneGraphique.itemconfig(bague1, fill=tabcouleur[coul[0]])
        ZoneGraphique.itemconfig(bague2, fill=tabcouleur[coul[1]])
        ZoneGraphique.itemconfig(bague3, fill=tabcouleur[coul[2]])
        ZoneGraphique.itemconfig(bague4, fill=tabcouleur[coul[3]])
        BoutonAfficher.configure(text="Effacer",command=effacer,background="red2")
    if nombre<0:
        effacer()
        erreur()
    if nombre>999999999:
        effacer()
        erreur1()
    if nombre==0:
        effacer()
        erreur2()
    if 10<nombre<100:
        ZoneGraphique.itemconfig(bague1, fill="black")
        ZoneGraphique.itemconfig(bague2, fill=tabcouleur[coul[0]])
        ZoneGraphique.itemconfig(bague3, fill=tabcouleur[coul[1]])
        ZoneGraphique.itemconfig(bague4, fill="black")
        BoutonAfficher.configure(text="Effacer",command=effacer,background="red2")
    if 0<nombre<10:
        ZoneGraphique.itemconfig(bague1, fill="black")
        ZoneGraphique.itemconfig(bague2, fill="black")
        ZoneGraphique.itemconfig(bague3, fill=tabcouleur[nombre])
        ZoneGraphique.itemconfig(bague4, fill="goldenrod")
        BoutonAfficher.configure(text="Effacer",command=effacer,background="red2")

# Fonction permettant d'effacer le contenu des bagues et de transformer effacer en afficher
def effacer():
    ZoneGraphique.itemconfig(bague1, fill="ivory2")
    ZoneGraphique.itemconfig(bague2, fill="ivory2")
    ZoneGraphique.itemconfig(bague3, fill="ivory2")
    ZoneGraphique.itemconfig(bague4, fill="ivory2")
    BoutonAfficher.configure(text="Afficher",command=coloriage,background="limegreen")
    Champ.delete(0,END)

# Fonction permettant de colorier les bagues de manière aléatoire pour jouer
def jeu():
    BoutonAfficher.configure(text="Valider",command=validation)
    BoutonJeu.configure(text="Mode classique",command=retour,background="yellow")
    text.configure(text="Devinez les valeurs des quatres bagues :",font=font2)
    text.place(x=140,y=513)
    global nombrejeu
    nombrejeu=randint(1,999999999)
    global coul
    coul = Decoupage_nombre(nombrejeu)
    tabcouleur=["black","DarkOrange4","red","orange","yellow","forest green","deep sky blue","purple2","snow4","white"]
    if nombrejeu>99:
        ZoneGraphique.itemconfig(bague1, fill=tabcouleur[coul[0]])
        ZoneGraphique.itemconfig(bague2, fill=tabcouleur[coul[1]])
        ZoneGraphique.itemconfig(bague3, fill=tabcouleur[coul[2]])
        ZoneGraphique.itemconfig(bague4, fill=tabcouleur[coul[3]])
    if 10<nombrejeu<100:
        ZoneGraphique.itemconfig(bague1, fill="black")
        ZoneGraphique.itemconfig(bague2, fill=tabcouleur[coul[0]])
        ZoneGraphique.itemconfig(bague3, fill=tabcouleur[coul[1]])
        ZoneGraphique.itemconfig(bague4, fill="black")
    if 0<nombrejeu<10:
        ZoneGraphique.itemconfig(bague1, fill="black")
        ZoneGraphique.itemconfig(bague2, fill="black")
        ZoneGraphique.itemconfig(bague3, fill=tabcouleur[nombre])
        ZoneGraphique.itemconfig(bague4, fill="goldenrod")
    return (nombrejeu)

# Fonction vérifiant si vous avez la bonne réponse
def validation():
    coul = Decoupage_nombre(nombrejeu)
    valeur=(str(coul[0])+str(coul[1])+str(coul[2])+str(coul[3]))
    reponse=ValResistance.get()
    if reponse==valeur:
        messagebox.showinfo("Bravo !")
        jeu()
    else :
        messagebox.showinfo("Raté !")
        jeu()
    Champ.delete(0,END)

# Fonction qui fait retourner l'utilisateur en mode classique
def retour():
    effacer()
    BoutonAfficher.configure(text="Afficher",command=coloriage)
    BoutonJeu.configure(text="Mode jeu",command=jeu,background="deeppink")
    text.configure(text="Valeur de la résistance :",font=font1)
    text.place(x=190,y=511)

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title('Résistance')
Mafenetre.geometry('+250+125')

# Création de la zone graphique
ZoneGraphique = Canvas(Mafenetre, width = 1000, height = 500, bg ='snow')
ZoneGraphique.pack()

# Création de la résistance
Rectangle = ZoneGraphique.create_rectangle(275, 350, 700, 125, outline='black', fill='ivory')

# Création de la première bague
bague1 = ZoneGraphique.create_rectangle(300, 350, 340, 125, outline='black', fill='ivory2')

# Création de la deuxième bague
bague2 = ZoneGraphique.create_rectangle(380, 350, 420, 125, outline='black', fill='ivory2')

# Création de la troisième bague
bague3 = ZoneGraphique.create_rectangle(460, 350, 500, 125, outline='black', fill='ivory2')

# Création de la quatrième bague
bague4 = ZoneGraphique.create_rectangle(580, 350, 620, 125, outline='black', fill='ivory2')

#Création du trait gauche
traitg = ZoneGraphique.create_rectangle(150, 240, 275, 240, outline='black', fill='ivory')

#Création du trait droit
traitd = ZoneGraphique.create_rectangle(825, 240, 700, 240, outline='black', fill='ivory')

#Création des polices
font1=("Helvetica",-18,"bold")
font2=("Helvetica",-13,"bold")

# Création du bouton afficher
BoutonAfficher = Button(Mafenetre, text ='Afficher', command = coloriage, background="limegreen",font=font1,cursor="spraycan")
BoutonAfficher.pack()
BoutonAfficher.place(x=432,y=463)

# Création du bouton code couleur
BoutonCode = Button(Mafenetre, text ='Code couleur', command = code, background="snow",font=font1,cursor="question_arrow")
BoutonCode.pack(side=RIGHT, padx=25)

# Création du bouton jeu
BoutonJeu = Button(Mafenetre, text ='Mode jeu', command = jeu, background="deeppink",font=font1,cursor="exchange")
BoutonJeu.pack()
BoutonJeu.place(x=25,y=25)

# Création du buton quitter
BoutonQuitter = Button(Mafenetre, text ='Quitter', command = Mafenetre.destroy, background="red2",font=font1,cursor="no")
BoutonQuitter.pack(side=LEFT, padx=25)

# Création du champ de saisie
ValResistance= StringVar()
Champ = Entry(Mafenetre,textvariable=ValResistance,bg ='bisque',fg='maroon',font=font1)
Champ.focus_set()
Champ.pack()
Champ.place(x=415,y=513)

#Création texte valeur de la résistance :
text = Label(text="Valeur de la résistance :",font=font1)
text.place(x=190,y=511)

# Lancement du gestionnaire d'évènements
Mafenetre.mainloop()