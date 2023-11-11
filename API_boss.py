from random import randint

class Boss:
    
    def __init__(self, nom, classe, points_de_vie, attaque, defense, resistance):
        self.nom_boss = nom
        self.classe = classe
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.defense = defense
        self.resistance = resistance
    
    @property
    def is_alive(self):
        return self.points_de_vie > 0

    def __str__(self):
        # Méthode pour afficher l'état actuel du personnage, y compris les points de magie disponibles
        return(f"{self.nom_boss} ({self.classe}) - PV : {self.points_de_vie} | Attaque : {self.attaque} | Défense : {self.defense} | Résistance : {self.resistance}")
        
    @property
    def get_nom_boss(self):
        return self.nom_boss
    
