
--- question ---

---
legend: Question 3 of 3
---

Your program took values from a list and stored them in a dictionary. Now, you have a program with this code:

--- code ---
---
language: python
---

pets = ['cat', 'dog', 'rabbit']

person = {
    'age': 12,
    'hair': 'brown',
    'pet': pets[1]
}

print(person['pet'])

--- /code ---

If you run the program, which of these would you expect it to display?

--- choices ---

- (x) 
```
dog
```
  --- feedback ---
  
  That's right! The `person` dictionary has saved 'dog' — which has the index `1` in the `pets` list — with the `pet` key.

  --- /feedback ---

- ( ) 
```
cat
```

  --- feedback ---

  Close — 'cat' is the first item in `pets`, but list indexes don't start from `1`.

  --- /feedback ---

- ( ) 
```
pets[1]
```

  --- feedback ---
  
  Not exactly. Python will get the string stored at `pets[1]` and store that string in `person` with the `pet` key.

  --- /feedback ---

- ( ) 
```
['cat', 'dog', 'rabbit']
```

  --- feedback ---
  
  Not quite. This is the whole `pets` list. But only one item from that list was added to the dictionary.

  --- /feedback ---

--- /choices ---

--- /question ---
