## Make Mercury

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Draw the planet Mercury in orbit of the sun.
</div>
<div>
![A yellow circle, surrounded by a white ring, with a red circle rotating around the ring, on a black background.](images/mercury_click.gif){:width="300px"}
</div>
</div>

### Draw Mercury

The code for creating an orbiting planet has been included for you in the `make_planet()` function.

--- task ---

Find the `# draw_planets function` comment. Create the function below it and add code to call `make_planet()` with Mercury's colour, orbit, size, and speed.

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
--- /code ---

**Tip:** You created your dictionary with one line for each key:value pair. You can do the same with function parameters, to make the code easier to read.

--- /task ---

--- task ---

Add a call to your `draw_planets()` in the `draw()` function, so the planets get redrawn in every frame.

--- code ---
---
language: python
filename: main.py — draw_planets()
line_numbers: true
line_number_start:  
line_highlights: 10-12
---
def draw():
  # Put code to run every frame here
  background(0)
  no_stroke()
  draw_sun()
  draw_orbits()
  draw_planets()
--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and see Mercury in orbit!

![A yellow circle, surrounded by a white ring, with a red circle rotating around the ring, on a black background.](images/mercury.gif){:width="400px"}

**Debug:** If you get a message about 'KeyError', check that all the keys you are using when calling `make_planet()` are spelt the same way as in `load_planets()`. Whether the letters are UPPERCASE or lowercase is important too.

**Debug:** If Mercury doesn't appear, check that you are calling `draw_planets()` in your `draw()` function and that it is after `background(0)`.

**Debug:** If Mercury is too big, moving too slowly, or still not visible, check that the order of the parameters in your `draw_planets()` function matches the example above.

--- /task ---

### Tell users about the planet

When users click on Mercury, your program should print the information about the planet in `mercury['info']`. The project already has the `mouse_pressed()` function and code for getting the colour the mouse was clicked on.

--- task ---

Find the `mouse_pressed()` function and add an `if` statement that will prent Mercury's name and information when its colour is clicked.

--- code ---
---
language: python
filename: main.py — mouse_pressed()
line_numbers: true
line_number_start:  
line_highlights: 
---

def mouse_pressed():
# Put code to run when the mouse is pressed here
  no_stroke()
  pixel_colour = color(get(mouse_x, mouse_y))

  if pixel_colour == mercury['colour']:
    print(mercury['name'])
    print(mercury['info'])

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code and click on Mercury to see its information print out. If it's moving too fast, change the `frame_rate()` value in `setup()` to slow the whole model down.

![A yellow circle, surrounded by a white ring, with a red circle rotating around the ring, on a black background. Information about Mercury appears in the text output.](images/mercury_click.gif){:width="400px"}

**Debug:** If nothing happens when you click on Mercury: ceck that your condition looks exactly like `if pixel_colour == mercury['colour']:`. Make sure you have `==` and not just `=`.

**Debug:** If you get a message about 'KeyError' when you click on Mercury, check that your spellings for `mercury['name']` and `mercury['info']` match the spellings in `load_planets()`

--- /task ---

