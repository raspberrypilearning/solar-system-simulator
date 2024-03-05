#!/bin/python3
from p5 import *
from make_planet import creer_planete


def dessiner_soleil():
    fill(255, 255, 0)  # Jaune
    ellipse(width / 2, height / 2, 100, 100)


# Fonction dessiner_orbites
def dessiner_orbites():
    no_fill()
    stroke(255)  # Rendre blanc

    ellipse(width / 2, height / 2, mercure['orbite'], mercure['orbite'])
    ellipse(width / 2, height / 2, venus['orbite'], venus['orbite'])
    ellipse(width / 2, height / 2, terre['orbite'], terre['orbite'])

# Fonction dessiner_planetes


def dessiner_planetes():

    couleur = mercure['couleur']
    orbite = mercure['orbite']
    taille = mercure['taille']
    vitesse = mercure['vitesse']

    creer_planete(
        couleur,
        orbite,
        taille,
        vitesse
    )

    couleur = venus['couleur']
    orbite = venus['orbite']
    taille = venus['taille']
    vitesse = venus['vitesse']

    creer_planete(
        couleur,
        orbite,
        taille,
        vitesse
    )

    couleur = terre['couleur']
    orbite = terre['orbite']
    taille = terre['taille']
    vitesse = terre['vitesse']

    creer_planete(
        couleur,
        orbite,
        taille,
        vitesse
    )


# Fonction charger_planetes
def charger_planetes():
    global mercure, venus, terre

    mercure = {
        'nom': 'Mercure',
        'couleur': Color(165, 42, 42),
        'taille': 15,
        'orbite': 150,
        'vitesse': 1,
        'info': 'La plus petite et la plus rapide des planètes.'
    }

    with open('planets.csv') as f:
        donnees = f.read()
        lignes = donnees.splitlines()

    planete = lignes[2].split(',')  # Diviser les données de Vénus
    venus = {
        'nom': planete[0],
        'couleur': Color(int(planete[1]), int(planete[2]), int(planete[3])),
        'taille': int(planete[4]),  # int() pour les nombres entiers
        'orbite': int(planete[5]),
        'vitesse': float(planete[6]),  # float() pour les décimales
        'info': planete[7]
    }

    planete = lignes[3].split(',')
    terre = {
        'nom': planete[0],
        'couleur': Color(int(planete[1]), int(planete[2]), int(planete[3])),
        'taille': int(planete[4]),
        'orbite': int(planete[5]),
        'vitesse': float(planete[6]),
        'info': planete[7]
    }


def setup():
    # Mettre le code à exécuter ci-dessous
    size(400, 400)
    charger_planetes()


def draw():
    # Mettre le code pour exécuter chaque frame ici
    background(0)
    no_stroke()
    dessiner_soleil()
    dessiner_orbites()
    dessiner_planetes()


def mouse_pressed():
    # Mettre le code à exécuter lorsque la souris est pressée ici
    # Ici, la valeur RVB est convertie en hexadécimal afin de pouvoir être utilisée ultérieurement dans une comparaison de chaînes de caractères
    couleur_pixel = Color(get(mouse_x, mouse_y)).hex

    if couleur_pixel == mercure['couleur'].hex:
        print(mercure['nom'])
        print(mercure['info'])
    elif couleur_pixel == venus['couleur'].hex:
        print(venus['nom'])
        print(venus['info'])
    elif couleur_pixel == terre['couleur'].hex:
        print(terre['nom'])
        print(terre['info'])


run(frame_rate=60)
