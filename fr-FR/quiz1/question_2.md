--- question ---

---
legend: Question 2 sur 3
---

Ton projet a lu beaucoup de données dans les dictionnaires pour créer les planètes et leurs orbites. Si ton programme contenait ce dictionnaire, comment imprimerais-tu la hauteur de la montagne ?

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

  Pas exactement, cela imprimerait une variable appelée `hauteur`. Ce dictionnaire est appelé `montagne`.

  --- /feedback ---

- (x)
```python
print(mountain['height'])
```

  --- feedback ---

    Correct ! Cela imprimera la valeur stockée dans la clé 'hauteur'.

  --- /feedback ---

- ( )
```python
print(mountain{'height'})
```

  --- feedback ---

  C'est presque vrai : les accolades (`{}`) sont utilisées pour créer un dictionnaire. Mais une autre paire de caractères est utilisée pour obtenir une valeur.

  --- /feedback ---

- ( )
```python
print(mountain)
```

  --- feedback ---

  Fermer ! Cela imprimera tout le dictionnaire. Tu veux juste imprimer la valeur stockée avec la clé `hauteur`.

  --- /feedback ---

--- /choices ---

--- /question ---
