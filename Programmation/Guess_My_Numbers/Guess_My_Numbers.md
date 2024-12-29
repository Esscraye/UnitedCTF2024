# Challenge

```txt
Description (français)
Alors que vous vous promenez dans le parc, un charlatan vous interpelle et vous propose un défi simple.

"Devinez les dix prochains nombres dans une série de séquences et gagnez! C'est un jeu d'enfant!"

Description (english)
As you were walking in the park, a charlatan calls out to you and offers you a simple challenge.

"Guess the next ten numbers in a series of sequences and win! It's child's play!"
```

Lorsque l'on se connectait au serveur, on avait 3 niveaux de difficultés à la suite :

chaque niveau possèdait sa propre logique de suite de nombres.

## Résolution

En étudiant le 1er niveau on remarque assez vite que la logique. à savoir chaque nombre valait le nombre précédent plus une `constante`. (je récupère donc la constante en faisant la différence entre deux nombres consécutifs)

Pour le niveau deux j'ai repéré le shéma suivant :
num1 + `Constante1` = num2
num2 + `Constante2` = num3 (ici la constante2 est négative)
num3 * `10` = num4
et on recommence.

Pour le niveau 3, pour tous les nombre pairs, il fallait le divisé par deux pour obtenir le nombre suivant. Pour les nombres impairs, il fallait lui additionner `4294967295` et diviser par `2` pour obtenir le nombre suivant.

pour trouver le `4294967295` j'ai fait plusieurs tests pour obtenir la plus longue suite de nombres impairs d'affilé et je les ai donné à manger à [wolframalpha](https://www.wolframalpha.com/input?i=303574591%2C+2299270943%2C+3297119119%2C+3796043207%2C+4045505251%2C+4170236273) pour qu'il trouve une relation. et il m'a donné :
`a_n = 2^(-n) (4294967295 2^n - 7982785408)`

Flag : `flag-L3sM4th5C3s7F4c1l3`
