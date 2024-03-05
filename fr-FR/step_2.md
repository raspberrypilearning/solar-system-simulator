## Créer un dictionnaire

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Pour commencer, tu vas collecter quelques informations sur Mercure et dessiner son orbite.
</div>
<div>
![Un arrière-plan noir avec un cercle jaune, entouré d'un anneau blanc.](images/mercury_orbit.png){:width="300px"}
</div>
</div>

--- task ---

Ouvre le [projet de démarrage Le système solaire](https://editor.raspberrypi.org/en/projects/solar-system-starter){:target="_blank"}. Le Code Editor Raspberry Pi s'ouvre dans un autre onglet du navigateur.

Si tu as un compte Raspberry Pi, tu peux cliquer sur le bouton **Enregistrer** pour enregistrer une copie dans ta bibliothèque `Projets`.

--- /task ---

### Faire un dictionnaire

Les dictionnaires Python te permettent de rechercher une **clé** et d'obtenir sa **valeur**. Il peut s'agir d'un mot et de sa signification, qui sont tous deux des textes. Mais tu pourrais aussi utiliser une clé de texte (comme `'distance'`) pour obtenir une valeur qui est un nombre, ou tout autre chose que tu peux stocker en Python.

--- collapse ---
---
title: Dictionnaires Python
---

En Python, un dictionnaire stocke des paires de **clés** et de **valeurs**.

Les clés et les valeurs peuvent être presque toutes les valeurs que tu peux stocker en Python. En dehors des listes et des dictionnaires, il ne peut s'agir de clés.

Tu peux utiliser une clé pour obtenir la valeur qui lui est associée.

Pour faire un dictionnaire, tu utilises des accolades `{}`, avec des paires `clé: valeur` à l'intérieur. Une paire est une clé, suivie de deux points (`:`), suivie de la valeur connectée à cette clé. Par exemple :

```python
persone = {
    'age': 12,
    'hauteur': 149.5,
    'cheveux': 'brun',
}
```
Ici, `age`, `taille` et `cheveux` sont les clés. Tu peux les utiliser pour rechercher leurs valeurs avec les crochets `[]`. Par exemple :

```python
print(person['hair'])
```
Ceci imprimera la valeur `brun`. --- /collapse ---

--- task ---

Trouve le commentaire `# Fonction charger_planetes` dans le projet de démarrage. Crée la fonction sous le commentaire. À l'intérieur de la fonction, crée un dictionnaire global `mercure`. Ensuite, ajoute des informations sur Mercure au dictionnaire.

<table>
<thead>
  <tr>
    <th>Clé</th>
    <th>Valeur</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>nom</td>
    <td>Mercure</td>
  </tr>
  <tr>
    <td>couleur</td>
    <td>Color(165, 42, 42)</td>
  </tr>
  <tr>
    <td>taille</td>
    <td>15</td>
  </tr>
  <tr>
    <td>orbite</td>
    <td>150</td>
  </tr>
  <tr>
    <td>vitesse</td>
    <td>1</td>
  </tr>
  <tr>
    <td>info</td>
    <td>La plus petite et la plus rapide des planètes.</td>
  </tr>
</tbody>
</table>

Les accolades `{}` sont utilisées pour démarrer et terminer le dictionnaire. Les deux points `:` sont utilisés pour séparer la clé et la (les) valeur(s). Une virgule `,` est utilisée pour séparer chaque élément du dictionnaire.

--- code ---
---
language: python filename: main.py — load_planets() line_numbers: true line_number_start: 16
line_highlights: 17-27
---
# load_planets function
def load_planets(): global mercury

    mercury = {
        'name': 'Mercury',
        'colour': Color(165, 42, 42),
        'size': 15,
        'orbit': 150,
        'speed': 1,
        'info': 'The smallest and fastest planet.'
    }
--- /code ---

**Astuce :** tu peux mettre chaque paire `clé: valeur` sur sa propre ligne. Cela rend le code plus facile à lire, mais veille à tout garder à l'intérieur des accolades `{}`.

--- /task ---

L'utilisation d'un dictionnaire te permet de garder toutes les informations sur Mercure en un seul endroit. Il est ainsi plus facile de les retrouver et de les modifier si nécessaire.

--- task ---

Appelle `charger_planetes()` dans ta fonction `configuration()`.

--- code ---
---
language: python filename: main.py — setup() line_numbers: true line_number_start: 30
line_highlights: 33
---
def setup(): # Put code to run once here size(400, 400) load_planets()

--- /code ---

--- /task ---

### Dessiner l'orbite de Mercure

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">**Modélisation des orbites :**</span> les orbites des vraies planètes ne sont pas des cercles parfaits, elles ont la forme d'une ellipse. Mais l'utilisation de cercles rend le modèle plus facile à construire !
</p>

Tu peux obtenir une valeur d'un dictionnaire en mettant sa clé entre crochets `[]`, tout comme tu obtiens un élément de liste par son index. Par exemple, `mercure['taille']` t'obtiendrait la valeur correspondante `15`.

--- task ---

Trouve le commentaire `# Fonction dessiner_orbites`. Crée la fonction `dessiner_orbites()` en dessous de celle-ci. Dessine ensuite l'orbite de Mercure sous la forme d'une `ellipse` centrée au milieu du modèle `width/2` et `height/2`. La taille de l'`ellipse` sera `mercure['orbite']`, qui est stockée dans ton dictionnaire sous la forme `150`.

[[[processing-python-ellipse]]]

--- code ---
---
language: python filename: main.py — draw_orbits() line_numbers: true line_number_start: 10
line_highlights: 11-15
---
# draw_orbits function
def draw_orbits(): no_fill() stroke(255)  # Make it white

    ellipse(width / 2, height / 2, mercury['orbit'], mercury['orbit'])

--- /code ---

--- /task ---

--- task ---

Appelle ta fonction `dessiner_orbites()` à partir de ta fonction `dessiner()`.

--- code ---
---
language: python filename: main.py — draw() line_numbers: true line_number_start: 39
line_highlights: 42
---
def draw(): # Put code to run every frame here background(0) no_stroke() draw_sun() draw_orbits()

--- /code ---

--- /task ---

--- task ---

 **Test :** exécute ton code et vois apparaître l'orbite de Mercure.

![Un arrière-plan noir avec un cercle jaune, entouré d'un anneau blanc.](images/mercury_orbit.png)

**Débogage :** si tu vois un message indiquant que `mercure` n'est pas "défini" :
 - Vérifie ta fonction `charger_planetes()` pour être sûr qu'elle déclare `mercure` comme `global`
 - Vérifie que `charger_planetes()` est appelé dans `configuration()`

**Débogage :** si l'orbite n'apparaît pas :
 - Vérifie que tu as bien appelé `dessiner_orbites()` dans ta fonction `dessiner()`
 - Vérifie `dessiner_orbites()` pour être sûr que tu as bien utilisé `stroke(255)` pour rendre l'ellipse blanche

**Débogage :** si l'orbite est un cercle rempli, au lieu d'un anneau, vérifie que tu as `no_fill()` dans ta fonction `dessiner_orbites()`.

**Débogage :** si tu obtiens une erreur `bad input`, vérifie que tu as bien un `:` entre les clés et les valeurs de ton dictionnaire `mercure`, et que chaque ligne (sauf la toute dernière) comporte une virgule.

--- /task ---

--- save ---

