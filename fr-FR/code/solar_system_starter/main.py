#!/bin/python3
from p5 import *
from make_planet import make_planet


def dessiner_soleil():
    fill(255, 255, 0)  # Jaune
    ellipse(width / 2, height / 2, 100, 100)


# Fonction dessiner_orbites


# Fonction dessiner_planetes


# Fonction charger_planetes


def setup():
    # Mettre le code à exécuter ci-dessous
    size(400, 400)


def draw():
    # Mettre le code pour exécuter chaque frame ici
    background(0)
    no_stroke()
    dessiner_soleil()


def mouse_pressed():
    # Mettre le code à exécuter lorsque la souris est pressée ici
    # Ici, la valeur RVB est convertie en hexadécimal afin de pouvoir être utilisée ultérieurement dans une comparaison de chaînes de caractères
    couleur_pixel = Color(get(mouse_x, mouse_y)).hex


run(frame_rate=60)
