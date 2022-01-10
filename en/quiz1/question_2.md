--- question ---

---
legend: Question 2 of 3
---

Your project read a lot of data from dictionaries to create the planets and their orbits. If your program contained this dictionary, how would you print the height of the mountain?

```python

mountain = {
 'name': 'Kangchenjunga',
 'range': 'Himalayas',
 'height': '8586 metres'
}

```

--- choices ---

- ( ) 
```python
print(height)
```
  --- feedback ---

  Not exactly, this would print a variable called `height`. This dictionary is called `mountain`.

  --- /feedback ---

- (x) 
```python
print(mountain['height'])
```

  --- feedback ---

    Correct! This will print the value stored with the `height` key.

  --- /feedback ---

- ( ) 
```python
print(mountain{'height'})
```

  --- feedback ---
 
  Almost right — braces (`{}`) are used to create a dictionary. But a different pair of characters are used to get a value from it.

  --- /feedback ---

- ( ) 
```python
print(mountain)
```

  --- feedback ---
 
  Close! This will print the whole dictionary — you just want to print the value stored with the `height` key.

  --- /feedback ---

--- /choices ---

--- /question ---
