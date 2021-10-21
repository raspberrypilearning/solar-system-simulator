## Make Venus & Earth

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
See Venus and Earth orbit the sun.
</div>
<div>
![A black background with a yellow circle, surrounded by three white rings. Red, pink, and blue circles are orbiting around the rings. Information about Venus and Earth appear in the text output.](images/all_planets_info.gif){:width="400px"}
</div>
</div>

## Draw the planets

--- task ---

Go to your `draw_planets()` function. Add `make_planet()` calls, passing it the values for Venus and Earth.

**Tip:** You copy pasted code, then made small changes, to create your `venus` and `earth` dictionaries. You can do the same here, to draw these with less typing.

--- code ---
---
language: python
filename: main.py — draw_planets()
line_numbers: true
line_number_start: 20
line_highlights: 34-56
---
# draw_planets function
def draw_planets():
  colour = mercury['colour']
  orbit = mercury['orbit']
  size = mercury['size']
  speed = mercury['speed']

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

**Test:** Run your code and check that Venus and Earth are orbiting the Sun.

![A black background with a yellow circle, surrounded by three white rings. Red, pink, and blue circles are orbiting around the rings.](images/all_planets.gif){:width="400px"}

**Debug:** If you get a message about 'KeyError', check the spelling of your keys in `make_planet()`. Make sure the spelling is the same in `load_planets()`. Whether the letters are UPPERCASE or lowercase is important too.

**Debug:** If any planet is too big, too slow, or not visible: Check that your `draw_planets()` code is the same as the example. In particular, check that the keys are in the right order.

--- /task ---

## Tell users about the planets

Like Mercury, Venus and Earth should print out an interesting fact when they're clicked on.

--- task ---

In `mouse_pressed()` add `elif` statements after the `if` you made for Mercury. Have them check for Venus and Earth's colours. Then, if there's a match, `print()` the right fact.

--- code ---
---
language: python
filename: main.py — mouse_pressed()
line_numbers: true
line_number_start: 111 
line_highlights: 118-123
---
def mouse_pressed():
# Put code to run when the mouse is pressed here
  pixel_colour = color(get(mouse_x, mouse_y))

  if pixel_colour == mercury['colour']:
    print(mercury['name'])
    print(mercury['info'])
  elif pixel_colour == venus['colour']:
    print(venus['name'])
    print(venus['info'])
  elif pixel_colour == earth['colour']:
    print(earth['name'])
    print(earth['info'])

--- /code ---

--- /task ---

--- task ---

**Test:** Run your code. Click on Venus and then Earth, to see their information print out.

![A black background with a yellow circle, surrounded by three white rings. Red, pink, and blue circles are orbiting around the rings. Information about Venus and Earth appear in the text output.](images/all_planets_info.gif){:width="400px"}

**Debug:** If nothing happens when you click on a planet, check its `elif` statement. Make sure it looks exactly like the example above. Check that you have `==` and not `=`.

--- /task ---

--- save ---
