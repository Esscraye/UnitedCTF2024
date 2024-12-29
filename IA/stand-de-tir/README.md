# Challenge petite-fringale

## Description

### Description (français)

Dans ces défits, on le but était de prédir avec un algorithme de d'ia (knn) les points de tir de la cible d'une épreuve de tir à l'arc.
Plus variations sont présentent en fonction des niveaux, je vous invite à regarder les descriptions exactes [ici](https://github.com/UnitedCTF/UnitedCTF2024/blob/main/challenges/ai/standdetir).

## Solutions

Pour les 3 niveaux, la solution a été de faire un simple algorithme de knn.
Lorsque j'ai commencé j'ai fait l'erreur de commencer par une régression, ça m'a permis de résoudre le niveau 1, mais je n'arrivais pas à le rendre assez précis pour le niveau 2 et 3. C'est pourquoi je suis finalement passer en classification.

cf les solutions :
- [Solution niveau 1](./level-1/knn.py)
- [Solution niveau 2](./level-2/knn2.py)
- [Solution niveau 3](./level-3/knn3.py)