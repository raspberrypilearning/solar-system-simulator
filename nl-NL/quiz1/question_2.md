--- question ---

---
legend: Vraag 2 van 3
---

Je project heeft veel gegevens uit dictionaries gelezen om de planeten en hun banen te creëren. Als je programma deze dictionary zou bevatten, hoe zou je dan de hoogte van de berg afdrukken?

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

  Niet precies, dit zou een variabele afdrukken met de naam `height`. Deze dictionary heet `mountain`.

  --- /feedback ---

- (x)
```python
print(mountain['height'])
```

  --- feedback ---

    Juist! Hierdoor wordt de waarde afgedrukt die is opgeslagen in de `height`-sleutel.

  --- /feedback ---

- ( )
```python
print(mountain{'height'})
```

  --- feedback ---

  Bijna goed: accolades (`{}`) worden gebruikt om een dictionary te maken. Maar er wordt een ander paar karakters gebruikt om er een waarde uit te halen.

  --- /feedback ---

- ( )
```python
print(mountain)
```

  --- feedback ---

  Bijna! Hiermee wordt de hele dictionary afgedrukt. Je wilt alleen de waarde afdrukken die is opgeslagen in de sleutel `height`.

  --- /feedback ---

--- /choices ---

--- /question ---
