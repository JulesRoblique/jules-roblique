import pyxel
from random import randint
from Random_fight_joueur import Joueur
from Random_fight_objet import Objet

class Jeu:
	def __init__(self,joueur1,joueur2):
		pyxel.init(128,128, title="Random fight")
		self.joueur1 = joueur1
		self.joueur2 = joueur2
		self.objets_liste = []
		self.durée = 0
		self.durée2 = 0
		self.game = True
		pyxel.load("Projet_pyxel.pyxres")
		pyxel.run(self.update,self.draw)

	def objets_creation(self):
		if (pyxel.frame_count % 450 == 0):
			self.objets_liste.append(Objet(randint(0, 120),0,2))#randint(2,9)))
        
    #création des objets aléatoirement en haut de la carte, tous ayant des types attribués, et donc des designs différents.

	def objet_contact(self,x,y):
		self.contact_b = False
		for x1 in range(x,x+8):
			if pyxel.pget(x1,y+8) == 3:
				self.contact_b = True

	def objets_deplacement(self):
		self.contact_b = False
		for objet in self.objets_liste:
			self.objet_contact(objet.x,objet.y)
			if self.contact_b == False:
				objet.y += 1
        
	def objets_suppression1(self):
		est_touche = False
		for objet in self.objets_liste:
			if self.joueur1.x-8 <= objet.x <= self.joueur1.x+8  and self.joueur1.y-8 <= objet.y <= self.joueur1.y+8:
				    est_touche = True
				    self.objets_liste.remove(objet)
		if est_touche:
			self.durée = 0
			if objet.type == 2:
			    self.joueur1.vitesse = 3
			    if (self.durée % 150 == 0 ):
				    self.joueur1.vitesse = 2
			if objet.type == 3:
				self.joueur1.dégâts = 15
				if self.durée % 150 == 0 :
					self.joueur1.dégâts = 10
			if objet.type == 4:
				self.joueur1.vies += 10
			if objet.type == 5:
				if self.joueur1.x > objet.x :
					self.joueur1.x -= 1
				else:
					self.joueur1.x += 1
			if objet.type == 6:
				if self.durée < 90 :
					self.joueur2.dégâts = 0
				self.joueur2.dégâts = 10
			if objet.type == 7:
			    pos = self.joueur1.y
			    self.joueur1.y = self.joueur2.y
			    self.joueur2.y = pos
			    pos2 = self.joueur1.x
			    self.joueur1.x = self.joueur2.x
			    self.joueur2.x = pos2
			#if objet.type == 8:
			#    while self.durée != 45 :
			#        self.joueur2.deplacement2() = False
			#    self.joueur2.deplacement2() = True
			#    self.durée = 0qdq
			#    self. = False
			if objet.type == 9:
				if (self.durée) % 150 == 0 :
				    self.joueur2.vies -= 3
					

		    
    #2 objets_suppression pour les 2 joueurs afin d'éviter tous les potentiels bug et de faciliter le codage (pour les pouvoirs nuisants l'adversaire).
	
	def objets_suppression2(self):
	    est_touche = False
	    for objet in self.objets_liste:
	        if self.joueur2.x-8 <= objet.x <= self.joueur2.x+8  and self.joueur2.y-8 <= objet.y <= self.joueur2.y+8:
	            est_touche = True
	            self.objets_liste.remove(objet)
	    if est_touche:
	        self.durée2 = 0
	        if objet.type == 2:
	            self.joueur2.vitesse = 3
	            if self.durée2 % 150 == 0 :
	                self.joueur2.vitesse = 2
	        if objet.type == 3:
	            if self.durée2 < 150:
	                self.joueur2.dégâts = 15
	            self.joueur2.dégâts = 10
	        if objet.type == 4:
	            self.joueur2.vies += 10
	        if objet.type == 5:
	            if self.joueur2.x > objet.x :
	                self.joueur2.x -= 1
	            else:
	                self.joueur2.x += 1
	        if objet.type == 6:
	            if self.durée2 < 90 :
	                self.joueur1.dégâts = 0
	            self.joueur1.dégâts = 10
	        if objet.type == 7:
	            pos = self.joueur2.y
	            self.joueur2.y = self.joueur1.y
	            self.joueur1.y = pos
	            pos2 = self.joueur2.x
	            self.joueur2.x = self.joueur1.x
	            self.joueur1.x = pos2
	        #if objet.type == 8:
	        #    while self.durée != 45 :
	        #        self.joueur1.deplacement() = False
	        #    self.joueur1.deplacement = True
	        #    self.durée = 0
	        if objet.type == 9:
	            if self.durée2 < 150 :
	                self.joueur1.vies -= 3

	def dégat(self):
		coup_touche = False
		for coup in self.joueur1.coups_liste:
			if coup[0]-8 <= self.joueur2.x <= coup[0]+4 and coup[1]-8 <= self.joueur2.y <= coup[1]+4:
				coup_touche = True
			else:
			    self.joueur1.coups_liste.remove(coup)
		if coup_touche:
			self.joueur1.coups_liste.remove(coup)
			self.joueur2.vies -= self.joueur1.dégâts

    #2 dégats pour les 2 joueurs (probablement pouvoir le faire en un seul).

	def dégat2(self):
	    coup_touche = False
	    for coup in self.joueur2.coups_liste:
	    	if coup[0]-8 <= self.joueur1.x <= coup[0]+4 and coup[1]-8 <= self.joueur1.y <= coup[1]+4:
	    		coup_touche = True
	    	else:
	    		self.joueur2.coups_liste.remove(coup)
	    if coup_touche:
	    	self.joueur2.coups_liste.remove(coup)
	    	self.joueur1.vies -= self.joueur2.dégâts

	def vide(self):
		if self.joueur1.y > 128:
			self.joueur1.y = 0
			self.joueur1.vies -= 20

    #2 vides pour quand les joueurs tombent dans le vide (probablement pouvoir le faire en un seul).

	def vide2(self):
		if self.joueur2.y > 128:
			self.joueur2.y = 0
			self.joueur2.vies -= 20

	def update(self):
		self.joueur1.deplacement()
		self.joueur2.deplacement2()

		self.joueur1.coups_creation()
		self.joueur2.coups_creation2()

		self.vide()
		self.vide2()
		
		self.dégat()
		self.dégat2()
		
		self.durée += 1
		self.durée2 += 1
		
		self.objets_creation()
		self.objets_deplacement()
		if pyxel.btnr(pyxel.KEY_F):
			self.objets_suppression1()
		if pyxel.btnr(pyxel.KEY_KP_0):
			self.objets_suppression2()

	def draw(self):
		pyxel.cls(10)
		pyxel.bltm(0,0,0,0,0,256,256)


		if self.joueur1.vies > 0:
			pyxel.text(5,5, 'PV:'+ str(self.joueur1.vies),0)
			self.joueur1.affichage(8,8,3)
			self.game = True

		if self.joueur2.vies > 0:
			pyxel.text(100,5, 'PV:'+ str(self.joueur2.vies),0)
			self.joueur2.affichage2(8,8,3)
			self.game = True

		#affichage des objets.
		if self.game:
			for objet in self.objets_liste:
				objet.affichage(8,8,8)	

		#condition de victoire.
		
		if self.joueur1.vies <= 0:
		    pyxel.text(3,50, "le Joueur 2 a gagne avec " + str(self.joueur2.vies) + " PV",13)
		    self.joueur2.affichage(8,8,3)
		    self.game = False

		if self.joueur2.vies <= 0:
		    pyxel.text(3,50, "le Joueur 1 a gagne avec " + str(self.joueur1.vies) + " PV",13)
		    self.joueur1.affichage(8,8,3)
		    self.game = False

J1 = Joueur(30,97,100,10,2)
J2 = Joueur(80,97,100,10,2)
Jeu(J1,J2)