> [!CAUTION]
Ce travail s'effectue dans [l'environnement Github](https://perso.esiee.fr/~courivad/courses/utils/misc-01-github-environment.html)

# Liste de Syracuse

Cet exercice est la continuité d'un exercice précédent sur [les suites de Syracuse](https://perso.esiee.fr/~courivad/courses/exercices/python-04-fonctions-suites-syracuse.html) dans lequel vous retrouverez la définition des grandeurs caractéristiques utilisées dans cet exercice. Précédemment, les valeurs de la suite étaient calculées à la volée sans mémorisation. L'objectif est ici de les stocker dans une liste pour post traitement.

Le fichier ``main.py`` contient :

- une fonction secondaire ``syr_plot()`` (NE PAS MODIFIER) qui permet de construire un graphique. 

- une fonction secondaire ``syracuse_l()``
  
  - qui prend en argument un entier ``n`` ;
  - et retourne la liste des valeurs de la suite.

  Pour ``n=3``, les valeurs de la suite sont ``[3, 10, 5, 16, 8, 4, 2, 1]``.

- une fonction secondaire ``temps_de_vol()``
  
  - qui prend en argument une liste de Syracuse ``l`` ;
  - et retourne son temps de vol.

  Pour ``n=3``, le temps de vol est ``7``.

- une fonction secondaire ``temps_de_vol_en_altitude()``
  
  - qui prend en argument une liste de Syracuse ``l`` ;
  - et retourne son temps de vol en altitude.

  Pour ``n=3``, le temps de vol en altitude est ``5``.

- une fonction secondaire ``altitude_maximale()``
  
  - qui prend en argument une liste de Syracuse ``l`` ;
  - et retourne son altitude maximale.

  Pour ``n=3``, l'altitude maximale est ``16``.

- la fonction principale ``main()`` qui fait appel aux fonctions secondaires pour vérifier leur bon fonctionnement .

<!-- START INSERT -->

## To do

1️⃣ Ecrire (ou modifier) le code de la fonction secondaire.

2️⃣ Si nécessaire, ajouter (ou modifier) les appels à la fonction secondaire logés dans la fonction principale ``main()``. Cela permet de tester la fonction secondaire sur quelques cas simples.

3️⃣ Exécuter le programme depuis le terminal. Tant que la fonction secondaire ne retourne pas les résultats attendus, répéter le cycle 1️⃣ 2️⃣ 3️⃣.

    $ python main.py

4️⃣ Lorsque les résultats obtenus à l'étape 3️⃣ sont satisfaisants, soumettre le code à une procédure de test plus robuste, les tests unitaires.

    $ pytest .python

Le score de test ``ST`` obtenu est le pourcentage de tests réussis. Tant que certains tests échouent, répéter le cycle 1️⃣ 2️⃣ 3️⃣ 4️⃣

5️⃣ Lorsque le score de test ``ST`` est satisfaisant, s'intéresser à la [qualité du code](https://perso.esiee.fr/~courivad/courses/utils/sources/python-23-codequality.html).

    $ pylint main.py

Si le score de qualité ``SQ`` n'est pas maximal, répéter l'étape 5️⃣ en tenant compte des messages dans le terminal

6️⃣ Lorsque les scores ``ST`` et ``SQ`` sont satisfaisants, pusher le travail vers votre repo distant. Ce travail est susceptible d'être pris en compte dans l'évaluation de l'unité.

    $ git add .
    $ git commit -m "un message explicatif"
    $ git push

> [!CAUTION]
En cas de soumissions multiples, seule la première est prise en compte.

<!-- END INSERT -->
