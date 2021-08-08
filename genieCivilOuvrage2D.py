from turtle import *
width(4)
speed(20)
# Commentaire de specification
"""
    Listing des blocs dinstruction  
    Fonction 1: Rectangle
    Fonction 2: Triangle
    Fonction 3: Carre
    Fonction 4: Cercle
    Fonction 5: Demi-cercle
    Fonction 6: Polygone
    Fonction 7: Trapeze
    Fonction 8: losange
    Fonction 9: ellipse
 Detailler le travail de chaque fonction 
    Fonction 1: Rectangle 
        Entrees : longueur,largeur
        Sorties : _
        Methode : Boucle
        Connus  : Angle(90°)
        
    Fonction 2: Triangle
        Entrees : x
        Sorties : _
        Methode : Boucle
        Connus  : Angle(120°) //on suppose que le triangle est isocele
        
      Fonction 3: Carre
        Entrees : cote 
        Sorties : _
        Methode : Boucle
        Connus  : Angle(90°)
        
        Fonction 4: Cercle
        Entrees : rayon
        Sorties : _
        Methode : Utilisation de la fonction circle()
        Connus  : Angle(360°) //mais ce n'est la peine de la mentionner dans les parametres de le fontion circle()
        
        
        Fonction 5: Demi-cercle
        Entrees : rayon
        Sorties : _ 
        Methode : Fonction circle()
        Connus  : Angle(180°)
        
        Fonction 6: Polygone
        Entrees : NombreDeCote
        Sorties : _
        Methode : Boucle
        Connus  : Angle(360/NombreDeCote)
        
        Fonction 7: Trapeze
        Entrees : x,y,z
        Sorties : _ 
        Methode : Boucle
        Connus  : Angle(90°) // on en utilise deux pour assurer que l'un des cotes soit paralelles
        
        Fonction 8: Losange
        Entrees : taille,angle
        Sorties : _
        Methode : Boucle et Iteration
        Connus  : Angle(180-angle)
        
        Fonction 7: Ellipse
        Entrees : rad
        Sorties : _
        Methode : Boucle , fonction circle()
        Connus  : Angles(45°)
        
"""
#fonction rectangle
def rectangle(longueur,largeur):
     for i in range(2):
            fd(longueur)
            left(90)
            fd(largeur)
            left(90)
#fonction triangle
def triangle(x):
    for i in range(3):
        forward(x)
        left(120)
#fonction carre
def carre(cote):
    for i in range(4):
        forward(cote)
        left(90)
#fonction cercle
def cercle(rayon):
    circle(rayon)
#fonction demi-cercle
def demiCercle(rayon):
    circle(rayon,180)

#fonction polygone
def polygone(NombreDeCote):
    for i in range(NombreDeCote):
        forward(100)
        left(360/NombreDeCote)
#fonction trapeze
def trapeze(x,y,z):
        left(180)
        forward(x)
        left(90)
        forward(y)
        left(90)
        forward(z)
        goto(0,0)
#fonction losange
def losange(taille,angle):
    c=0
    while c<4:
        if c%2==0:
            right(angle)
            forward(taille)
        if c%2==1:
            right(180-angle)
            forward(taille)
        c=c+1
#fonction ellipse
def ellipse(rad):
     for i in range(2):
        circle(rad, 45)
        circle(rad // 2, 45)


