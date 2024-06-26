
--- question ---

---
legend: Vraag 3 van 3
---

Je programma nam waarden uit een lijst en heeft ze opgeslagen in een dictionary. Nu heb je een programma met deze code:

--- code ---
---
language: python
---

huisdieren = ['kat', 'hond', 'konijn']

persoon = {
    'leeftijd': 12,
    'haarkleur': 'bruin',
    'huisdier': huisdieren[1]
}

print(persoon['huisdier'])

--- /code ---

Als je het programma uitvoert, welke van deze opties verwacht je dan dat deze wordt weergegeven?

--- choices ---

- (x)
```
hond
```
  --- feedback ---

  Dat klopt! De `persoon` dictionary heeft 'hond' opgeslagen — met de index `1` in de `huisdieren` lijst — met de `huisdier`-sleutel.

  --- /feedback ---

- ( )
```
kat
```

  --- feedback ---

  Niet helemaal - 'kat' is het eerste item in `huisdieren`, maar lijstindexen beginnen niet vanaf `1`.

  --- /feedback ---

- ( )
```
huisdieren[1]
```

  --- feedback ---

  Niet helemaal. Python zal de string opslaan bij `huisdieren[1]` en die string opslaan in `persoon` met de `huisdier`-sleutel.

  --- /feedback ---

- ( )
```
['kat', 'hond', 'konijn']
```

  --- feedback ---

  Niet helemaal. Dit is de hele `huisdieren` lijst. Maar slechts één item uit die lijst werd aan de dictionary toegevoegd.

  --- /feedback ---

--- /choices ---

--- /question ---
