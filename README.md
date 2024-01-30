# TP Multithreading 

## Structure du Projet : 

- [Classes Python](#Classes Python) 

1. Boss :
La classe Boss est responsable d'ajouter x Task à une QueueClient (Managers).

3. Managers :
La classe Managers utilise la QueueClient pour gérer les Task et leurs résultats. Elle coordonne la distribution des tâches aux Minions et récupère les résultats pour les consolider.

3. Minion :
La classe Minion traite les Task présentes dans la QueueClient. Chaque Minion est responsable de la résolution d'une tâche spécifique.

5. Proxy :
La classe Proxy permet d'envoyer un fichier JSON correspondant à la Task à traiter sur une adresse locale.

5. Task :
La classe Task représente une résolution linéaire ax = b. Elle possède une fonction pour calculer le temps de résolution et résoudre l'équation. La classe Task peut également convertir les paramètres liés à la Task au format JSON.

- [Fichiers C++](#Fichiers C++)

low_level : La classe low_level permet la lecture d'un fichier JSON sur une adresse locale et la résolution de l'équation en fonction de la méthode choisie. 
