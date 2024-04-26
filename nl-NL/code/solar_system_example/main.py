#!/bin/python3
from p5 import *
from make_planet import maak_planeet


def teken_zon():
    fill(255, 255, 0) # Geel
    ellipse(width / 2, height / 2, 100, 100)


# teken_banen functie
def teken_banen():
    no_fill()
    stroke(255) # Maak het wit

    ellipse(width / 2, height / 2, mercurius['baan'], mercurius['baan'])
    ellipse(width / 2, height / 2, venus['baan'], venus['baan'])
    ellipse(width / 2, height / 2, aarde['baan'], aarde['baan'])

# teken_planeten functie


def teken_planeten():

    kleur = mercurius['kleur']
    baan = mercurius['baan']
    grootte = mercurius['grootte']
    snelheid = mercurius['snelheid']

    maak_planeet(
        kleur,
        baan,
        grootte,
        snelheid
    )

    kleur = venus['kleur']
    baan = venus['baan']
    grootte = venus['grootte']
    snelheid = venus['snelheid']

    maak_planeet(
        kleur,
        baan,
        grootte,
        snelheid
    )

    kleur = aarde['kleur']
    baan = aarde['baan']
    grootte = aarde['grootte']
    snelheid = aarde['snelheid']

    maak_planeet(
        kleur,
        baan,
        grootte,
        snelheid
    )


# laad_planeten functie
def laad_planeten():
    global mercurius, venus, aarde

    mercurius = {
        'naam': 'Mercurius',
        'kleur': Color(165, 42, 42),
        'grootte': 15,
        'baan': 150,
        'snelheid': 1,
        'info': 'De kleinste en snelste planeet.'
    }

    with open('planets.csv', 'w') as f:
        data = f.read()
        lijnen = data.splitlines()

    planeet = lijnen[2].split(',') # Splits de gegevens van Venus
    venus = {
        'naam': planeet[0],
        'kleur': Color(int(planeet[1]), int(planeet[2]), int(planeet[3])),
        'grootte': int(planeet[4]), # int() voor hele getallen
        'baan': int(planeet[5]),
        'snelheid': float(planet[6]), # float() voor decimalen
        'info': planeet[7]
    }

    planeet = lijnen[3].split(',')
    aarde = {
        'naam': planeet[0],
        'kleur': Color(int(planeet[1]), int(planeet[2]), int(planeet[3])),
        'grootte': int(planeet[4]),
        'baan': int(planeet[5]),
        'snelheid': float(planeet[6]),
        'info': planeet[7]
    }


def setup():
    # Zet de code om eenmalig uit te voeren hier onder
    size(400, 400)
    laad_planeten()


def draw():
    # Zet hier code om bij elk frame uit te voeren
    background(0)
    no_stroke()
    teken_zon()
    teken_banen()
    teken_planeten()


def mouse_pressed():
    # Zet code hier die moet worden uitgevoerd wanneer de muis wordt ingedrukt
    # Hier wordt de RGB-waarde omgezet naar Hex, zodat deze later in een stringvergelijking kan worden gebruikt
    pixel_kleur = Color(get(mouse_x, mouse_y)).hex

    if pixel_kleur == mercurius['kleur'].hex:
        print(mercurius['naam'])
        print(mercurius['info'])
    elif pixel_kleur == venus['kleur'].hex:
        print(venus['naam'])
        print(venus['info'])
    elif pixel_kleur == aarde['kleur'].hex:
        print(aarde['naam'])
        print(aarde['info'])


run(frame_rate=60)
