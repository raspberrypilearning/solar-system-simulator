
--- question ---

---
legend: Question 3 sur 3
---

Ton programme a pris des valeurs dans une liste et les a stockées dans un dictionnaire. Maintenant, tu as un programme avec ce code :

--- code ---
---
language: python
---

pets = ['cat', 'dog', 'rabbit']

personne = { 'age': 12, 'cheveux': 'brun', 'animal': animaux[1] }

print(person['pet'])

--- /code ---

Lorsque tu lanceras le programme, laquelle de ces options devrait s'afficher ?

--- choices ---

- (x)
```
chien
```
  --- feedback ---

  C'est exact ! Le dictionnaire `personne` a enregistré 'chien' - qui a l'indice `1` dans la liste `animaux` - avec la clé `animal`.

  --- /feedback ---

- ( )
```
chat
```

  --- feedback ---

  Presque - 'chat' est le premier élément dans `animaux`, mais les index de liste ne commencent pas à partir de `1`.

  --- /feedback ---

- ( )
```
pets[1]
```

  --- feedback ---

  Pas exactement. Python récupère la chaîne stockée dans `animaux[1]` et la stocke dans `personne` avec la clé `animal`.

  --- /feedback ---

- ( )
```
['cat', 'dog', 'rabbit']
```

  --- feedback ---

  Pas tout à fait. Voici la liste complète des `animaux` . Mais un seul élément de cette liste a été ajouté au dictionnaire.

  --- /feedback ---

--- /choices ---

--- /question ---
