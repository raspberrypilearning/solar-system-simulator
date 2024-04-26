--- question ---

---
legend: Vraag 2 van 3
---

Je project heeft veel gegevens uit dictionaries gelezen om de planeten en hun banen te creëren. Als je programma deze dictionary zou bevatten, hoe zou je dan de hoogte van de berg afdrukken?

```python

berg = {
 'naam': 'Kangchenjunga',
 'bergketen': 'Himalaya',
 'lengte': '8586 meter'
}

```

--- choices ---

- ( )
```python
print(lengte)
```
  --- feedback ---

  Niet precies, dit zou een variabele afdrukken met de naam `lengte`. Deze dictionary heet `berg`.

  --- /feedback ---

- (x)
```python
print(berg['lengte'])
```

  --- feedback ---

    Juist! Hierdoor wordt de waarde afgedrukt die is opgeslagen in de `lengte`-sleutel.

  --- /feedback ---

- ( )
```python
print(berg{'lengte'})
```

  --- feedback ---

  Bijna goed: accolades (`{}`) worden gebruikt om een dictionary te maken. Maar er wordt een ander paar karakters gebruikt om er een waarde uit te halen.

  --- /feedback ---

- ( )
```python
print(berg)
```

  --- feedback ---

  Bijna! Hiermee wordt de hele dictionary afgedrukt. Je wilt alleen de waarde afdrukken die is opgeslagen in de sleutel `lengte`.

  --- /feedback ---

--- /choices ---

--- /question ---
