## Create a dictionary

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create a dictionary of data about Mercury, and draw its orbit.
</div>
<div>
![A yellow circle, surrounded by a white ring, on a black background.](images/mercury_orbit.png){:width="300px"}
</div>
</div>

--- task ---

Open the [Solar System starter project](https://trinket.io/python/0e48381967){:target="_blank"}. Trinket will open in another browser tab.

If you have a Trinket account, you can click on the **Remix button** to save a copy to your `My Trinkets` library.

--- /task ---

### Make a dictionary

You can create a dictionary using braces `{}`. Python uses dictionaries to store a **value** with a **key**. You can use the key get the value later.

--- task ---

Find the `# load_planets function` comment. Create the function below it and, inside the function, a global `mercury` dictionary with some keys and values about the planet.

--- code ---
---
language: python
filename: main.py — load_planets()
---
# load_planets function
def load_planets():
  global mercury

  mercury = {
      'name': 'Mercury',
      'colour': color(165, 42, 42),
      'size': 15,
      'orbit': 150,
      'speed': 1,
      'info': 'The smallest, and fastest, planet.'
  }
--- /code ---

--- /task ---

When creating a dictionary write your key, followed by a colon, then the value you want to link to that key. For example: `'size': 15`. Put a comma between each key:value pair. 


You can put each pair on its own line. This makes the code easier to read, but be sure to keep it all inside the braces (`{}`).

--- task ---

Call `load_planets()` in your `setup()` function.

--- code ---
---
language: python
filename: main.py — setup()
---
def setup():
  # Put code to run once here
  size(400, 400)
  frame_rate(60)
  load_planets()
  
  
--- /code ---

--- /task ---

### Draw Mercury's orbit

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Modeling orbits:**</span> the real planets don't orbit in perfect circles. Their orbits are actually oval shaped. But using circles makes the model easier to build!
</p>

You can get a value out of a dictionary using its key in square brackets (`[]`), just like getting a list item by its index. For example `mercury['size']` would get you the matching value, `15`.

--- task ---

Find the `#draw_orbits function` comment. Create the function below it and add the code to draw Mercury's orbit around the centre using the `orbit` value from the `mercury` dictionary.

--- code ---
---
language: python
filename: main.py — draw_orbits()
---
# draw_orbits function
def draw_orbits():
  no_fill()
  stroke(255) # Make it white
  
  ellipse(width / 2, height / 2, mercury['orbit'], mercury['orbit'])
  
  
--- /code ---

--- /task ---

--- task ---

Call your `draw_orbits()` function from your `draw()` function.

--- code ---
---
language: python
filename: main.py — draw()
---
def draw():
  # Put code to run every frame here
  background(0)
  no_stroke()
  draw_sun()
  draw_orbits()
  
  
--- /code ---

--- /task ---

--- task ---

 **Test:** Run your code and see the orbit of Mercury appear.

![A yellow circle, surrounded by a white ring, on a black background.](images/mercury_orbit.png)

**Debug:** if you get a message about `mercury` being 'not defined', check your `load_planets()` to be sure that it declares `mercury` as `global`. Also, check that `load_planets()` is called in `setup()`.

**Debug:** if the orbit isn't appearing, check that you have called `draw_orbits()` in your `draw()` function. Also, check `draw_orbits()` to be sure you have used `stroke(255)` to make the ellipse white.

**Debug:** if the orbit is a filled circle, instead of a ring, make sure you have included `no_fill()` in your `draw_orbits()` function.

--- /task ---

--- save ---
