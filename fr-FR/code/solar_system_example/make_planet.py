from p5 import *


def creer_planete(couleur, orbite, taille, vitesse):
    no_stroke()
    fill(couleur)
    # Transformation 2D
    push_matrix()
    # Centrer l'orbite sur le centre du modèle
    translate(width / 2, height / 2)
    # Rotation de la "vitesse" en degrés à chaque frame
    rotate(radians((frame_count * vitesse) % 360))
    # Dessiner la planète
    ellipse(orbite / 2, 0, taille, taille)
    # Fin de la transformation 2D
    pop_matrix()
