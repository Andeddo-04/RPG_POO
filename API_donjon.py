from random import randint

from API_monstres import Monstres
from API_boss import Boss
from API_combat import Combat

class Donjon:
    
    def __init__(self, etages, joueur):
        self.etages = etages  # Nombre d'étages dans le donjon
        self.niveau = 0  # Niveau actuel (étage)
        self.joueur = joueur  # Le personnage du joueur

    @property
    def jouer(self):
        
        print("\nLINK START !\n\nBienvenue au Royaume d'Éldoria\n")
        
        print("\nDans un monde en proie aux ténèbres, le royaume d'Éldoria est menacé par une magie maléfique.")
        print("Jadis prospère, le Cercle de l'Aube Noir, un culte maléfique, à plongé Éldoria dans le sang et le chaos.\n")
        print("Un héros solitaire, Arion, se lève pour affronter le Cercle de l'Aube Noir.\n")
        print("Accompagné de compagnons loyaux, il entreprend une quête périlleuse pour délivrer le royaume.")
        print("Leur objectif est de restaurer les runes antiques et ainsi, repousser les ténèbres qui menacent la capitale d'Éldoria.\n")
        print("Le destin du royaume repose entre les mains de ces valeureux héros. L'avenir est incertain, mais l'espoir demeure, car dans ce monde, la bravoure et la magie peuvent accomplir des miracles.\n")
        print("Vous arrivez après d'inombrables efforts, à votre destination finale, déterminer à venger la mort de vos compagnons, vous pénétrer, seul, dans ce donjon ...\n")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        
        while self.niveau < self.etages:
            self.niveau += 1
            print(f"Vous arrivez a l'étage {self.niveau} du donjon.")
            self.jouer_etage

        print("Félicitations ! Vous êtes venu a bout du dernier étage du donjon.")

    @property
    def jouer_etage(self):
        # Génère des monstres aléatoires pour cet étage
        # [nom, classe, points_de_vie, attaque, defense, résistance]
        monstres = [Monstres(f"Monstre n°{i+1}", "Bête", 40, randint(5, 15), randint(2, 10), 0.9) for i in range(self.niveau)]
        # [nom, classe, points_de_vie, attaque, defense, résistance]
        boss = Boss(f"Démon au Yeux Azur", "Boss", 125, randint(20, 25), randint(10, 20), 0.25)

        rencontre_boss = False
        
        print(f"Vous reprerez {len(monstres)} monstres à cet étage.\n")

        for monstre in monstres:
            
            while self.joueur.get_pv_perso and monstre.get_etat_monstre:
                
                self.joueur.get_etat_perso
                print("")
                
                monstre.get_etat_monstre
                
                print("\nQue voulez-vous faire ?\n1. Attaque physique\n2. Attaque Magique")
                
                choix = input("Choisissez une option : ")
                print("")

                if choix == "1":
                    self.joueur.joueur_attaque_physique_monstre()
                elif choix == "2":
                    self.joueur.joueur_attaque_magique_monstre()

                if monstre.get_pv_monstre:
                    monstre.monstre_attaque_joueur()
                
                if not monstre.get_pv_monstre:
                    self.joueur.get_xp
                    self.joueur.add_xp
                    self.joueur.get_xp
        
        print("")
        
        if self.joueur.get_pv_perso and self.niveau == self.etages:
            
            print("Le boss du donjon apparait, ...\nVous rencontrez le Démon aux Yeux Azur.\n")
            rencontre_boss = True
                       
            while self.joueur.get_pv_perso and boss.get_pv_boss:
                
                self.joueur.get_etat_perso
                print("")
                
                boss.get_etat_boss
                print("\nQue voulez-vous faire ?\n1. Attaque physique\n2. Attaque Magique")
                
                choix = input("Choisissez une option : ")
                print("")

                if choix == "1":
                    self.joueur.joueur_attaque_physique_boss()
                
                elif choix == "2":
                    self.joueur.joueur_attaque_magique_boss()
                    
                if boss.est_en_vie:
                    boss.boss_attaque_joueur()



        if self.joueur.get_pv_perso and self.niveau < self.etages:
            print(f"Vous avez vaincu tous les monstres de l'étage {self.niveau} !")
            # self.joueur.up_aptittude
            # \nToute vos apttitudes de combat augmente de , vous regagner 10 % de vos PV max et regagner 1 unité de magie !\n
        
        if self.joueur.get_pv_perso and self.niveau == self.etages and not boss.get_pv_boss:
            
            print(f"\nFélicitaation ! Vous êtes venu a bout du donjon !")
            # exit()
            
        if not self.joueur.get_pv_perso and self.niveau == self.etages and boss.get_pv_boss:
            if rencontre_boss == True:
                
                self.joueur.get_etat_perso
                print("")
                boss.get_etat_boss
                
                print(f"\nVous avez été vaincu par le [ {boss.get_nom_boss} ] ...")
            
            else:
                print(f"Vous avez été vaincu par les monstres de l'étage {self.niveau} ...")
            
            print(f"Vous n'avez pas été en mesure de sauver Éldoria, le Cercle de l'Aube Noir acheva sont oeuvre sans plus personne pour l'arrêter ...\n")
            # exit()
        
    
