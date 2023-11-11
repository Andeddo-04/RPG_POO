class Personnage:
    
    def __init__(self, nom, classe, xp, points_de_vie, defense, attaque_physique, attaque_magique, jauge_mana):
        self.nom = nom
        self.classe = classe
        self.xp = xp
        
        self.points_de_vie = points_de_vie
        self.defense = defense
        
        self.attaque_physique = attaque_physique
        self.attaque_magique = attaque_magique
        
        self.jauge_mana = jauge_mana

    @property
    def get_pv_perso(self):
        # Méthode pour vérifier si le personnage est en vie (PV > 0)
        return self.points_de_vie > 0

    @property
    def get_etat_perso(self):
        # Méthode pour afficher l'état actuel du personnage, y compris les points de magie disponibles
        print(f"{self.nom} ({self.classe}) - PV : {self.points_de_vie} | Défense : {self.defense} | Attaque physique : {self.attaque_physique} | Attaque magique : {self.attaque_magique} | Jauge mana : {self.jauge_mana}")

    # @property
    # def up_stats_perso(self):
    #     self.points_de_vie += (self.pv_initiaux * 10/100)
    #     self.attaque *= 105/100
    #     self.defense *= 105/100
    #     self.magie *= 105/100
    #     if self.magie_disponible == self.magie_disponible_initial:
    #         pass
    #     else:
    #         self.magie_disponible += 1

    @property
    def get_xp(self):
        print(f"Vous avez {self.xp} xp")
    
    @property
    def add_xp(self):
        self.xp += 10