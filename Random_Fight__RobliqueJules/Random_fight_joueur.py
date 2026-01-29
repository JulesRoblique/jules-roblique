import pyxel

class Joueur:
	def __init__(self,x,y,vies,dégâts,vitesse):
		self.x = x
		self.y = y
		self.vies = vies
		self.dégâts = dégâts
		self.vitesse = vitesse
		self.coups_liste = []
		self.saut_en_cours = False
		self.objectif = None



	def affichage(self,largeur,hauteur,couleur):
		if pyxel.btn(pyxel.KEY_F) and pyxel.btn(pyxel.KEY_Q):
			pyxel.blt(self.x,self.y,0,8,16,8,16,14)
		elif pyxel.btn(pyxel.KEY_F) and pyxel.btn(pyxel.KEY_D):
			pyxel.blt(self.x,self.y,0,0,16,8,16,14)
		elif pyxel.btn(pyxel.KEY_F) and pyxel.btn(pyxel.KEY_Z):
			pyxel.blt(self.x,self.y,0,8,16,8,16,14)
		elif pyxel.btn(pyxel.KEY_D):
			pyxel.blt(self.x,self.y,0,16,0,8,16,14)
		elif pyxel.btn(pyxel.KEY_Q):
			pyxel.blt(self.x,self.y,0,32,0,8,16,14)
		elif pyxel.btn(pyxel.KEY_Z):
			pyxel.blt(self.x,self.y,0,48,0,8,16,14)
		elif pyxel.btn(pyxel.KEY_F):
			pyxel.blt(self.x,self.y,0,0,16,8,16,14)
		else: 
			pyxel.blt(self.x,self.y,0,0,0,8,16,14)

    #2 affichages pour avoir les 2 designs différents, permettant d'avoir (sans appuyer sur une touche) 2 personnages ne se ressemblant pas.

	def affichage2(self,largeur,hauteur,couleur):
		if pyxel.btn(pyxel.KEY_KP_0) and pyxel.btn(pyxel.KEY_LEFT):
			pyxel.blt(self.x,self.y,0,40,40,8,16,14)
		elif pyxel.btn(pyxel.KEY_KP_0) and pyxel.btn(pyxel.KEY_RIGHT):
			pyxel.blt(self.x,self.y,0,32,40,8,16,14)
		elif pyxel.btn(pyxel.KEY_KP_0) and pyxel.btn(pyxel.KEY_UP):
			pyxel.blt(self.x,self.y,0,32,40,8,16,14)
		elif pyxel.btn(pyxel.KEY_RIGHT):
			pyxel.blt(self.x,self.y,0,48,24,8,16,14)
		elif pyxel.btn(pyxel.KEY_LEFT):
			pyxel.blt(self.x,self.y,0,32,24,8,16,14)
		elif pyxel.btn(pyxel.KEY_KP_0):
			pyxel.blt(self.x,self.y,0,32,40,8,16,14)
		elif pyxel.btn(pyxel.KEY_UP):
			pyxel.blt(self.x,self.y,0,56,0,8,16,14)
		else: 
			pyxel.blt(self.x,self.y,0,8,0,8,16,14)



	def contact(self,x,y):
		for x1 in range(x,x+8):
			if pyxel.pget(x1,y+16) == 3:
				self.contact_b = True
			if pyxel.pget(x1,y-1) == 3:
				self.contact_h = True

		for y1 in range(y, y+17):
			if pyxel.pget(x-1,y1) == 3:
				self.contact_g = True
			if pyxel.pget(x+8,y1-1) == 3:
				self.contact_d = True
				
	#afin de faire les collisions avec le decor, permettant ainsi la gravité.

	def deplacement(self):
		self.contact_h = False
		self.contact_b = False
		self.contact_g = False
		self.contact_d = False

		self.contact(self.x,self.y)

		if pyxel.btn(pyxel.KEY_D) and self.x<120:
			self.x += self.vitesse
		if pyxel.btn(pyxel.KEY_Q) and self.x>0:
			self.x += - self.vitesse
		if pyxel.btnp(pyxel.KEY_Z) and self.y>0 and self.contact_b == True:
			self.objectif = self.y - 30
			self.saut_en_cours = True

		if self.saut_en_cours:
			self.y -= 3
		if self.y == self.objectif or self.contact_h:
			self.saut_en_cours = False

		if not self.contact_b and not self.saut_en_cours:
			self.y += 2
	
	#essayer de faire un saut fluide
	#2 déplacements pour pas que les joueurs ont les mêmes touches de déplacements.

	def deplacement2(self):
		self.contact_h = False
		self.contact_b = False
		self.contact_g = False
		self.contact_d = False
		self.contact(self.x,self.y)

		if pyxel.btn(pyxel.KEY_RIGHT) and self.x<120:
			self.x += self.vitesse
		if pyxel.btn(pyxel.KEY_LEFT) and self.x>0:
			self.x += - self.vitesse
		if pyxel.btnp(pyxel.KEY_UP) and self.y>0 and self.contact_b == True:
			self.objectif = self.y - 30
			self.saut_en_cours = True

		if self.saut_en_cours:
			self.y -= 3
		if self.y == self.objectif or self.contact_h:
			self.saut_en_cours = False

		if not self.contact_b and not self.saut_en_cours:
			self.y += 2


	def coups_creation(self):
		if pyxel.btnp(pyxel.KEY_F):
			self.coups_liste.append([self.x+4, self.y-4])
			
	#2 coups créations pour ne pas que les joueurs utilisent les mêmes touches pour mettre un coup.
	
	def coups_creation2(self):
		if pyxel.btnp(pyxel.KEY_KP_0):
			self.coups_liste.append([self.x+4, self.y-4])