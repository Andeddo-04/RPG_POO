class Monstres:
    
    def __init__(self, nom, classe, points_de_vie, attaque, defense, resistance):
        self.nom = nom
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
        return(f"{self.nom} ({self.classe}) - PV : {self.points_de_vie} | Attaque : {self.attaque} | Défense : {self.defense} | Résistance : {self.resistance}")
    
