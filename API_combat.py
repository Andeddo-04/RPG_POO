from random import randint

from API_monstres import Monstres
from API_boss import Boss

class Combat:
    
    def __init__(self):
        self.pv_joueur = self.joueur.points_de_vie
        self.def_joueur = self.joueur.defense
        self.attaque_physique_joueur = self.joueur.attaque_physique
        self.attaque_magique_joueur = self.joueur.attaque_magique
        self.jauge_mana = self.joueur.jauge_mana
        
        self.pv_monstre = self.monstre.points_de_vie
        self.def_monstre = self.monstre.defense
        self.res_monstre = self.monstre.resistance
        self.attaque_physique_monstre = self.monstre.attaque
        
        self.pv_boss = self.boss.points_de_vie
        self.def_boss = self.boss.defense
        self.res_boss = self.boss.resistance
        self.attaque_physique_boss = self.boss.attaque
        
    # ===========================================================================================
    # ===========================================================================================
    
    def joueur_attaque_physique_monstre(self):
        
        dgt_subi = self.attaque_physique_joueur - self.def_monstre
        
        if dgt_subi > 0:
        
            self.pv_monstre -= dgt_subi
            
            print(f"Le monstre reçois {dgt_subi} dégats, il à désormait {self.pv_monstre} pv")
        
        else:
            print(f"Ce n'est pas très efficace ... le monstre à toujours {self.pv_monstre} pv")
        
    
    def joueur_attaque_magique_monstre(self):
    
        if self.jauge_mana > 0 :
            
            self.jauge_mana -= 10
            dgt_subi = self.attaque_physique_joueur * self.res_monstre
            
            if dgt_subi > 0:
            
                self.pv_monstre -= dgt_subi
                
                print(f"Le monstre reçois {dgt_subi} dégats, il à désormait {self.pv_monstre} pv, il vous reste {self.jauge_mana} points de mana.")
            
            else:
                print(f"Ce n'est pas très efficace ... le monstre à toujours {self.pv_monstre} pv, il vous reste {self.jauge_mana} points de mana.")
        
        else:
            print(f"Il ne vous reste plus assez de mana pour lancer un sort ...")
    # ===========================================================================================
    # ===========================================================================================
    
    def joueur_attaque_physique_boss(self):
        
        dgt_subi = self.attaque_physique_joueur - self.def_boss
        
        if dgt_subi > 0:
        
            self.pv_boss -= dgt_subi
            
            print(f"Le monstre reçois {dgt_subi} dégats, il à désormait {self.pv_boss} pv")
        
        else:
            print(f"Ce n'est pas très efficace ... le monstre à toujours {self.pv_boss} pv")
        
        
    def joueur_attaque_magique_boss(self):
    
        dgt_subi = self.attaque_physique_joueur * self.res_boss
        
        if dgt_subi > 0:
        
            self.pv_boss -= dgt_subi
            
            print(f"Le monstre reçois {dgt_subi} dégats, il à désormait {self.pv_boss} pv")
        
        else:
            print(f"Ce n'est pas très efficace ... le monstre à toujours {self.pv_boss} pv")
        
    # ===========================================================================================
    # ===========================================================================================
    
    def monstre_attaque_joueur(self):
        
        dgt_subi = self.attaque_physique_monstre - self.def_joueur
        
        if dgt_subi > 0:
        
            self.pv_boss -= dgt_subi
            
            print(f"Le monstre vous inflige {dgt_subi} dégats, il vous reste désormait {self.pv_joueur} pv")
        
        else:
            print(f"Vous parez l'attaque du monstre  ... vous conservez vos {self.pv_boss} pv")
        
    
    def boss_attaque_joueur(self):
    
        dgt_subi = self.attaque_physique_boss * self.def_joueur
        
        if dgt_subi > 0:
        
            self.pv_boss -= dgt_subi
            
            print(f"Le Boss vous inflige {dgt_subi} dégats, il vous reste désormait {self.pv_joueur} pv")
        
        else:
            print(f"Vous parez l'attaque du [ {self.get_nom_boss} ] ... vous conservez vos {self.pv_boss} pv")