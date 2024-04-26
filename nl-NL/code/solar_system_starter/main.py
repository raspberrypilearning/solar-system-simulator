#!/bin/python3
from p5 import *
from make_planet import maak_planeet


def teken_zon():
    fill(255, 255, 0) # Geel
    ellipse(width / 2, height / 2, 100, 100)


# teken_baan functie


# teken_planeten functie


# laad_planeten functie


def setup():
    # Zet de code om eenmalig uit te voeren hier onder
    size(400, 400)


def draw():
    # Zet hier code om bij elk frame uit te voeren
    background(0)
    no_stroke()
    teken_zon()


def mouse_pressed():
    # Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
    # Hier wordt de RGB-waarde omgezet naar Hex, zodat deze later in een stringvergelijking kan worden gebruikt
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex


run(frame_rate=60)
