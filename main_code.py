from random import randint

# Importation des classes situé dans des fichiers différents
from API_personnage import Personnage
from API_donjon import Donjon

# Crée le personnage du joueur avec des attributs spécifiques (magie et magie_disponible)
    # [nom, classe, xp, points_de_vie, defense, attaque_physique, attaque_magique, mana_restant]
    # nom, classe, xp, points_de_vie, attaque_physique, defense, attaque_magique, jauge_mana)
joueur = Personnage("Arion", "Le dernier espoir", 0, 100, 10, 20, 15, 100)
     
# Défini le nombre d'étages dans le donjon
etages_du_donjon = randint(1,2)

# Crée l'objet Donjon
donjon = Donjon(etages_du_donjon,joueur)
# donjon.joueur = joueur

# Démarre le jeu
donjon.jouer
