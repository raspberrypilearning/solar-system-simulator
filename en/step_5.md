## Make Venus & Earth

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Draw Venus and Earth to join Mercury in orbit.
</div>
<div>
<mark>gif goes here</mark>
</div>
</div>

## Draw the planets

--- task ---

Go to your `draw_planets()` function. Below the code that draws Mercury, add `make_planet()` calls with the values for Venus and Earth. 

**Tip:** You copy pasted code, then made small changes, to create your dictionaries faster. You can do the same here, to make your planets with less typing.

--- code ---
---
language: python
filename: main.py — draw_planets()
line_numbers: true
line_number_start:  
line_highlights: 10-12
---
# draw_planets function
def draw_planets():
  make_planet(
    mercury['colour'], 
    mercury['orbit'], 
    mercury['size'], 
    mercury['speed']
    )

  make_planet(
    venus['colour'], 
    venus['orbit'], 
    venus['size'], 
    venus['speed']
    )
    
  make_planet(
    earth['colour'], 
    earth['orbit'], 
    earth['size'], 
    earth['speed']
    )
--- /code ---

--- /task ---

