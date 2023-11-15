def joueur_attaque_physique_monstre(joueur, monstre):
    
    dgt_subi = joueur.attaque_physique - monstre.defense
    
    if dgt_subi > 0:
    
        monstre.points_de_vie -= dgt_subi
        
        print(f"Le monstre reçois {dgt_subi} dégats, il à désormait {monstre.points_de_vie} pv")
    
    else:
        print(f"Ce n'est pas très efficace ... le monstre à toujours {monstre.points_de_vie} pv")
    

def joueur_attaque_magique_monstre(joueur, monstre):

    if joueur.jauge_mana > 0 :
        
        joueur.jauge_mana -= 10
        dgt_subi = joueur.attaque_magique * monstre.resistance
        
        if dgt_subi > 0:
        
            monstre.points_de_vie -= dgt_subi
            
            print(f"Le monstre reçois {dgt_subi} dégats, il à désormait {monstre.points_de_vie} pv, il vous reste {joueur.jauge_mana} points de mana.")
        
        else:
            print(f"Ce n'est pas très efficace ... le monstre à toujours {monstre.points_de_vie} pv, il vous reste {joueur.jauge_mana} points de mana.")
    
    else:
        print(f"Il ne vous reste plus assez de mana pour lancer un sort ...")
# ===========================================================================================
# ===========================================================================================

def joueur_attaque_physique_boss(joueur, boss):
    
    dgt_subi = joueur.attaque_physique - boss.defense
    
    if dgt_subi > 0:
    
        boss.points_de_vie -= dgt_subi
        
        print(f"Le monstre reçois {dgt_subi} dégats, il à désormait {boss.points_de_vie} pv")
    
    else:
        print(f"Ce n'est pas très efficace ... le monstre à toujours {boss.points_de_vie} pv")
    
    
def joueur_attaque_magique_boss(joueur, boss):

    if joueur.jauge_mana > 0 :
        
        joueur.jauge_mana -= 10
        dgt_subi = joueur.attaque_magique * boss.resistance
        
        if dgt_subi > 0:
        
            boss.points_de_vie -= dgt_subi
            
            print(f"Le monstre reçois {dgt_subi} dégats, il à désormait {boss.points_de_vie} pv")
        
        else:
            print(f"Ce n'est pas très efficace ... le monstre à toujours {boss.points_de_vie} pv")
    else:
        print(f"Il ne vous reste plus assez de mana pour lancer un sort ...")
    
# ===========================================================================================
# ===========================================================================================

def monstre_attaque_joueur(joueur, monstre):
    
    dgt_subi = monstre.attaque - joueur.defense
    
    if dgt_subi > 0:
    
        joueur.points_de_vie -= dgt_subi
        
        print(f"Le monstre vous inflige {dgt_subi} dégats, il vous reste désormait {joueur.points_de_vie} pv")
    
    else:
        print(f"Vous parez l'attaque du monstre  ... vous conservez vos {joueur.points_de_vie} pv")
    

def boss_attaque_joueur(joueur, boss):

    dgt_subi = boss.attaque - joueur.defense
    
    if dgt_subi > 0:
    
        joueur.points_de_vie -= dgt_subi
        
        print(f"Le Boss vous inflige {dgt_subi} dégats, il vous reste désormait {joueur.points_de_vie} pv")
    
    else:
        print(f"Vous parez l'attaque du [ {boss.get_nom_boss} ] ... vous conservez vos {joueur.points_de_vie} pv")