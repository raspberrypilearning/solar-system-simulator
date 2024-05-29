## Maak Aarde

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Maak het model nu af door de planeet waarop je je bevindt toe te voegen!
</div>
<div>
![Een zwarte achtergrond met een gele cirkel, omgeven door drie witte ringen. Op de ringen draaien rode, roze en blauwe cirkels om de gele cirkel. Informatie over de aarde verschijnt in de tekstuitvoer.](images/all_planets_info.gif){:width="400px"}
</div>
</div>

### Laad de gegevens

--- task ---

Voeg een `global` variabele voor Aarde toe aan je `laad_planeten()` functie:

--- code ---
---
language: python filename: main.py — load_planets() line_numbers: true line_number_start: 47
line_highlights: 49
---
# load_planets function
def load_planets(): global mercury, venus, earth --- /code ---

--- /task ---

Je hebt de gegevens al in je programma: de gegevens van de aarde zijn in `lijnen` geladen toen je `planets.csv`laadde.

--- task ---

Splits onder je `venus` dictionary `regels[3]` en plaats het in een `aarde` dictionary.

**Tip:** Je kunt de code kopiëren en plakken die je hebt gebruikt om de `venus` dictionary te maken, om je wat tijd te besparen. Vervolgens moet je gewoon kleine wijzigingen aanbrengen - `lijnen[2]` wordt `lijnen[3]`, en `venus` wordt `aarde`.

--- code ---
---
language: python filename: main.py — load_planets() line_numbers: true line_number_start: 56
line_highlights: 71-79
---

    with open('planets.csv') as f:
        data = f.read()
        lines = data.splitlines()
    
    planet = lines[2].split(',')
    #print(planet)
    venus = { 
        'name': planet[0],
        'colour': Color(int(planet[1]), int(planet[2]), int(planet[3])),
        'size': int(planet[4]), 
        'orbit': int(planet[5]),
        'speed': float(planet[6]), 
        'info': planet[7]
    }
    
    planet = lines[3].split(',') 
    earth = { 
        'name': planet[0],
        'colour': Color(int(planet[1]), int(planet[2]), int(planet[3])),
        'size': int(planet[4]), 
        'orbit': int(planet[5]),
        'speed': float(planet[6]), 
        'info': planet[7]
    }

--- /code ---

--- /task ---

### Teken de baan

--- task ---

Ga naar je `teken_banen()` functie en voeg de baan van Aarde toe.

--- code ---
---
language: python filename: main.py — draw_orbits() line_numbers: true line_number_start: 10
line_highlights: 17
---
# draw_orbits function
def draw_orbits(): no_fill() stroke(255)  # Make it white

    ellipse(width / 2, height / 2, mercury['orbit'], mercury['orbit'])
    ellipse(width / 2, height / 2, venus['orbit'], venus['orbit'])
    ellipse(width / 2, height / 2, earth['orbit'], earth['orbit'])

--- /code ---

--- /task ---

--- task ---

 **Test:** Voer je code uit en zie de baan van Aarde verschijnen.

![Een zwarte achtergrond met een gele cirkel, omgeven door drie witte ringen. Op twee van de ringen draaien rode en roze cirkels rond de gele cirkel.](images/all_orbit.gif)

**Debug:** Als je een bericht ziet dat `aarde` 'not defined' is, controleer dan `laad_planeten()`. Zorg ervoor dat je `aarde`  hebt aangeduid als `global`.

--- /task ---

### Teken de aarde

--- task ---

Ga naar je `teken_planeten()` functie. Voeg een `maak_planeet()` aanroep toe, waarbij je de waarden voor Aarde doorgeeft. Net als bij Venus kun je hier code kopiëren en plakken om jezelf wat werk te besparen.

--- code ---
---
language: python filename: main.py — draw_planets() line_numbers: true line_number_start: 19
line_highlights: 45-55
---
# draw_planets function
def draw_planets(): colour = mercury['colour'] orbit = mercury['orbit'] size = mercury['size'] speed = mercury['speed']

    make_planet(
        colour, 
        orbit, 
        size, 
        speed
    )
    
    colour = venus['colour']
    orbit = venus['orbit']
    size = venus['size']
    speed = venus['speed']
    
    make_planet(
        colour, 
        orbit, 
        size, 
        speed
    )
    
    colour = earth['colour']
    orbit = earth['orbit']
    size = earth['size']
    speed = earth['speed']
    
    make_planet(
        colour, 
        orbit, 
        size, 
        speed
    )

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit en controleer of de aarde om de zon draait.

![Een zwarte achtergrond met een gele cirkel, omgeven door drie witte ringen. Op de ringen draaien rode, roze en blauwe cirkels om de gele cirkel.](images/all_planets.gif){:width="400px"}

**Debug:** Als je een bericht krijgt over 'KeyError', controleer dan de spelling van je sleutels in `maak_planeet()`. Zorg ervoor dat de spelling hetzelfde is in `laad_planeten()`. Of de letters HOOFDLETTERS of kleine letters zijn, is ook belangrijk.

**Debug:** Als een planeet te groot, te langzaam of niet zichtbaar is, controleer dan of je `teken_planeten()` code hetzelfde is als in het voorbeeld. Controleer vooral of de sleutels in de juiste volgorde staan.

--- /task ---

### Vertel gebruikers over de aarde

Net als Mercurius en Venus zou de aarde een interessant feit moeten afdrukken wanneer erop wordt geklikt.

--- task ---

In `mouse_pressed()` voeg `elif` statement toe voor Aarde zoals je hebt gemaakt voor Venus. Laat hem de kleur van de aarde controleren. Als er dan een overeenkomst is, `print()` het juiste feit.

--- code ---
---
language: python filename: main.py — mouse_pressed() line_numbers: true line_number_start: 108
line_highlights: 118-120
---
def mouse_pressed(): # Put code to run when the mouse is pressed here pixel_colour = Color(get(mouse_x, mouse_y)).hex  # Here the RGB value is converted to Hex so it can be used in a string comparison later

    if pixel_colour == mercury['colour'].hex:
        print(mercury['name'])
        print(mercury['info'])
    elif pixel_colour == venus['colour'].hex:
        print(venus['name'])
        print(venus['info'])
    elif pixel_colour == earth['colour'].hex:
        print(earth['name'])
        print(earth['info'])

--- /code ---

--- /task ---

--- task ---

**Test:** Voer je code uit. Klik op Aarde om de informatie te zien.

![Een zwarte achtergrond met een gele cirkel, omgeven door drie witte ringen. Op de ringen draaien rode, roze en blauwe cirkels om de gele cirkel. Informatie over de aarde verschijnt in de tekstuitvoer.](images/all_planets_info.gif){:width="400px"}

**Debug:** Als er niets gebeurt wanneer je op Aarde klikt, controleer dan de instructie `elif`. Zorg ervoor dat het er precies zo uitziet als in het bovenstaande voorbeeld. Controleer of je `==` hebt en niet `=`.

--- /task ---

--- save ---
