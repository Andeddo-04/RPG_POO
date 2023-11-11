class Monstres:
    
    def __init__(self, nom, classe, points_de_vie, attaque, defense, resistance):
        self.nom = nom
        self.classe = classe
        self.points_de_vie = points_de_vie
        self.attaque = attaque
        self.defense = defense
        self.resistance = resistance
        
    @property
    def get_pv_monstre(self):
        return self.points_de_vie > 0

    @property
    def get_etat_monstre(self):
        # Méthode pour afficher l'état actuel du personnage, y compris les points de magie disponibles
        print(f"{self.nom} ({self.classe}) - PV : {self.points_de_vie} | Attaque : {self.attaque} | Défense : {self.defense} | Résistance : {self.resistance}")
    
