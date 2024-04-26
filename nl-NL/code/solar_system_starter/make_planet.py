from p5 import *
import __main__


def maak_planeet(kleur, baan, grootte, snelheid):
    no_stroke()
    fill(colour)
    # 2D transformatie
    push_matrix()
    # Centreer de baan op het midden van het model
    translate(width / 2, height / 2)
    # Draai 'snelheid' graden elk frame
    rotate(radians((frame_count * snelheid) % 360))
    # Teken de planeet
    ellipse(baan / 2, 0, grootte, grootte)
    # Beëindig de 2D-transformatie
    pop_matrix()
