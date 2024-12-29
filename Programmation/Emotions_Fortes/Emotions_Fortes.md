# Challenge Emotions Fortes

## Emotions fortes 1

Pour le niveau 1 d'émotions fortes, j'ai récupéré tous les émojis et j'ai demandé à ChatGPT de les classés dans les 3 catégories.

En testant 2 ou 3 fois j'ai ajusté à la main les quelques émojis qui n'étaient pas bien classés.

Flag : `flag-wwwwoo0ooOOOaAAa4ah`

## Emotions fortes 2

Cette fois-ci, j'ai de nouveau récupéré les 72 émojis et j'ai créé un dictionnaire JSON associant chaque émoji à une liste ['G1', 'G2', 'G3'].

J'ai retiré les groupes incorrects de la liste pour les émojis dont nous connaissions déjà la classification grâce à la description du challenge.

Pour classer les autres émojis, j'ai recherché dans les cas du serveur les émojis que je ne connaissais pas encore mais qui étaient déjà associés à des émojis de deux groupes distincts. J'ai donc supposé qu'ils n'appartenaient pas au troisième groupe. Par itérations successives, j'ai éliminé les "mauvais groupes" pour chaque émoji. J'ai construit le dictionnaire cinq fois et, pour chaque émoji, j'ai associé le groupe le plus fréquent.

Ainsi, j'ai pu obtenir les bonnes listes d'émojis pour chaque groupe.

Flag : `flag-s3tTh30ryMuch`
