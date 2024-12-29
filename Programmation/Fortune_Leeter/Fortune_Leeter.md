# Challenge

## Énoncé

```txt
Description (français)
Dans une petite allée sombre du parc, vous tombez sur un vieil automate de voyance. Intrigué·e, vous insérez un jeton pour savoir ce que vous réserve l'avenir. Mais là c'est la douche froide ! La réponse de cette machine est incompréhensible. Cependant, votre instinct informatique détecte une forme de logique dans les messages de l'automate et vous vous retroussez les manches pour comprendre ce qu'il raconte.

Description (english)
In a small dark alley of the park, you come across an old fortune-telling machine. Intrigued, you insert a token to find out what the future holds. But then it's a cold shower! The machine's response is incomprehensible. However, your computer instinct detects a form of logic in the machine's messages, and you roll up your sleeves to understand what it's saying.
```

Lorsqu'on se conneccet au serveur, on a 3 niveaux de difficulté :

```txt
 .+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+. 
(      ,gggggggggggggg                                                                    )
 )    dP""""""88""""""                      I8                                           ( 
(     Yb,_    88                            I8                                            )
 )     `""    88                         88888888                                        ( 
(          ggg88gggg                        I8                                            )
 )            88   8 ,ggggg,    ,gggggg,    I8    gg      gg  ,ggg,,ggg,    ,ggg,        ( 
(             88    dP"  "Y8ggg dP""""8I    I8    I8      8I ,8" "8P" "8,  i8" "8i        )
 )      gg,   88   i8'    ,8I  ,8'    8I   ,I8,   I8,    ,8I I8   8I   8I  I8, ,8I       ( 
(        "Yb,,8P  ,d8,   ,d8' ,dP     Y8, ,d88b, ,d8b,  ,d8b,dP   8I   Yb, `YbadP'        )
 )         "Y8P'  P"Y8888P"   8P      `Y888P""Y888P'"Y88P"`Y8P'   8I   `Y8888P"Y888      ( 
(                                                                                         )
 )                                                                                       ( 
(      ,ggggggggggggggg                                                                   )
 )    dP""""""88"""""""    ,dPYb, ,dPYb,                                                 ( 
(     Yb,_    88           IP'`Yb IP'`Yb                                                  )
 )     `""    88           I8  8I I8  8I                                                 ( 
(             88           I8  8' I8  8'                                                  )
 )            88   ,ggg,   I8 dP  I8 dP  ,ggg,    ,gggggg,                               ( 
(             88  i8" "8i  I8dP   I8dP  i8" "8i   dP""""8I                                )
 )    #######################################################                            ( 
(        "Yb,,8P  `YbadP' ,d8b,_ ,d8b,_ `YbadP' ,dP     Y8,                               )
 )         "Y8P' 888P"Y8888P'"Y888P'"Y8888P"Y8888P      `Y8                              ( 
(                                                                                         )
 )                                                                                       ( 
(            ,gggg,   ad888888b,  ad888888b,          ad888888b,                          )
 )          d8" "8I  d8"     "88 d8"     "88    I8   d8"     "88                         ( 
(           88  ,dP          a88         a88    I8           a88                          )
 )       8888888P"          ,88P        ,88P 88888888       ,88P                         ( 
(           88            aad8"       aad8"     I8        aad8"                           )
 )          88            ""Y8,       ""Y8,     I8        ""Y8,    ,gggggg,              ( 
(      ,aa,_88              `88b        `88b    I8          `88b   dP""""8I               )
 )    dP" "88P               "88         "88   ,I8,          "88  ,8'    8I              ( 
(     Yb,_,d88b,,_   Y8,     a88 Y8,     a88  ,d88b, Y8,     a88 ,dP     Y8,              )
 )     "Y8P"  "Y88888 "Y888888P'  "Y888888P' 88P""Y88 "Y888888P' 8P      `Y8             ( 
(                                                                                         )
 "+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+"+.+" 

Peux tu me renvoyer la phrase encodé en clair ? Toutes les lettres sont en minuscule.
Can you send me the sentence back in plain text ? All letters are lowercase.

Choose your level of difficulty (from 0 to 2) : 
```

Level 0, 1, 2 avec des phrases à comprendre :

```txt
Choose your level of difficulty (from 0 to 2) : 0
Leet Quote: y0u 4r3 7h3 m4573r 0f 3v3ry 5i7u47i0n.
>>

Choose your level of difficulty (from 0 to 2) : 1
Leet Quote: \/e/Vture /Vot /-\ll i/V o/Ve /3o/-\t.
>> 

Choose your level of difficulty (from 0 to 2) : 2
Leet Quote: @ )-(@/\/|)/=(_)£ ()/= |>@"|"1€/\/[€ 1$ \\'()/2"|")-( |V|()/2€ "|")-(@/\/ @ |3(_)$)-(€£ ()/= |3/2@1/\/$.
>> 
```

## Résolution

Pour les 3, j'ai construit un dictionnaire de correspondance.

Partie 1 du flag : `flag-7h3`
Partie 2 du flag : `Fu7ur3`
Partie 3 du flag : `1sY0ur5`

Flag : `flag-7h3Fu7ur31sY0ur5`

## Fortune Leeter 2

Pour ce niveau ci le principe est exactement le même sauf qu'il n'y a qu'un seul level et les caractères ne correspondent pas toujours à la même chose ils peuvent varier.

J'ai globalement récupéré toutes les phrases du server (135), je les ai traduites et me suis fait un dictionnaires.

(il se trouve que je n'ai manifestement pas réussi à traduire toutes les phrases, il y en a une j'y ai même vu une faute ^^. Ducoup j'ai lancer le script plusieurs fois pour avoir un cas où je tombe que sur des phrases que j'ai su traduire ^^)

Flag : `flag-Th3F0r7un3C00ki3IsN07ALi3`
