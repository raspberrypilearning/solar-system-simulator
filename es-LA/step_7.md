## Upgrade your project

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
In this step, add more planets to your model, or change the ones you have.
</div>
<div>
![A model of the solar system with all eight planets.](images/full_solar.gif){:width="300px"}
</div>
</div>

### Add more planets
The `planets.csv` file has information for the other five planets too. Add as many of them as you want.

--- task ---

To add a planet to your model you will need to:
 - Add code to load it in `load_planets()`
 - Add code to draw its orbit in `draw_orbits()`
 - Add code to draw the planet in `draw_planets()`
 - Add code to notice when the planet is clicked, and print out its info in `mouse_pressed()`

 **Tip:** Don't forget you can copy and paste code!

--- /task ---

--- task ---

Increase the `size()` in your `setup()` function to make the model large enough to see your new planets; `size(900, 900)` will fit them all in.

--- /task ---

### Make up a planet!

--- task ---

Add an extra planet to the solar system. Create a new `global` variable with a dictionary for it. Then, add code to draw it and to print out its info.

--- /task ---

--- collapse ---
---
title: Completed project
---

You can view the [completed project here](https://editor.raspberrypi.org/en/projects/solar-system-example){:target="_blank"}.

--- /collapse ---

--- save ---
