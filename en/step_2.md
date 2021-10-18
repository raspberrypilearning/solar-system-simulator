## Create a dictionary

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Create a dictionary of data about Mercury, and draw its orbit.
</div>
<div>
![A black background with a yellow circle, surrounded by a white ring.](images/mercury_orbit.png){:width="300px"}
</div>
</div>

--- task ---

Open the [Solar System starter project](https://trinket.io/python/33d830b0ce){:target="_blank"}. Trinket will open in another browser tab.

If you have a Trinket account, you can click on the **Remix button** to save a copy to your `My Trinkets` library.

--- /task ---

### Make a dictionary

You can use a normal dictionary to look up a word's meaning. Python dictionaries let you look up a **key** and get its **value**. That could be a word and its meaning, which are both text. But you could also use a text key (e.g. `'distance'`) to get a value that's a number, or anything else you can store in Python .

--- collapse ---
---
title: Python dictionaries
---

A dictionary in Python stores pairs of **keys** and **values**.

Both a keys and values can be almost any value you can store in Python. Although neither lists nor dictionaries can be keys.

You can use a key to get its connected value.

To make a dictionary you use braces (`{}`), with key: value pairs, separated by commas, inside. For example:

```python
person = {
  'age': 12,
  'height': 149.5,
  'hair': 'brown',
}
```
`age`, `height`, and `hair` are keys. You can use them to look up their values with square brackets (`[]`). For example:

```python
print(person['hair'])
```
Will print out the value `brown`.
--- /collapse ---

--- task ---

Find the `# load_planets function` comment. Create the function below the comment. Inside the function, make a global `mercury` dictionary.  Then, add information about Mercury to the dictionary.

--- code ---
---
language: python
filename: main.py — load_planets()
line_numbers: true
line_number_start: 30
line_highlights: 31-41
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

You can put each key: value pair on its own line. This makes the code easier to read, but be sure to keep it all inside the braces (`{}`).

--- task ---

Call `load_planets()` in your `setup()` function.

--- code ---
---
language: python
filename: main.py — setup()
line_numbers: true
line_number_start: 44
line_highlights: 48
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
<span style="color: #0faeb0">**Modeling orbits:**</span> The real planets' orbits are not perfect circles — they're oval shaped. But using circles makes the model easier to build!
</p>

You can get a value out of a dictionary using its key in square brackets (`[]`),  like getting a list item by its index. For example `mercury['size']` would get you the matching value, `15`.

--- task ---

Find the `#draw_orbits function` comment. Create the function below it. Then draw Mercury's orbit around the centre of the model.

--- code ---
---
language: python
filename: main.py — draw_orbits()
line_numbers: true
line_number_start: 24
line_highlights: 25-29
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
line_numbers: true
line_number_start: 56
line_highlights: 61 
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

![A black background with a yellow circle, surrounded by a white ring.](images/mercury_orbit.png)

**Debug:** if you see a message about `mercury` being 'not defined':
 - check your `load_planets()` to be sure that it declares `mercury` as `global`
 - check that `load_planets()` is called in `setup()`

**Debug:** if the orbit isn't appearing:
 - check that you have called `draw_orbits()` in your `draw()` function
 - check `draw_orbits()` to be sure you have used `stroke(255)` to make the ellipse white

**Debug:** if the orbit is a filled circle, instead of a ring, check you have `no_fill()` in your `draw_orbits()` function.

--- /task ---

--- save ---

