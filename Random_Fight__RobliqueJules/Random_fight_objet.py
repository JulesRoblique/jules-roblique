import pyxel

class Objet:
	def __init__(self,x,y,type):
		self.x = x
		self.y = y
		self.type = type

	def objet_contact(self,x,y):
		for x1 in range(x,x+8):
			if pyxel.pget(x1,y+8) == 3:
				self.contact_b = True

	def objets_deplacement(self):
		self.contact_b = False
		for objet in self.objets_liste:
			self.objet_contact(self.x,self,y)
			if objet.contact_b == False:
				objet.y += 1
    
    #faire tomber les objets tout en créant une collision lorsqu'il touche le sol.


	def affichage(self,largeur,hauteur,couleur):
		#if self.type == 1:
			#pyxel.blt(self.x,self.y,0,16,32,8,8,7)
		if self.type == 2:
			pyxel.blt(self.x,self.y,0,16,24,8,8,7)
		if self.type == 3:
			pyxel.blt(self.x,self.y,0,34,17,4,6,7)
		if self.type == 4:
			pyxel.blt(self.x,self.y,0,24,32,8,8,7)
		if self.type == 5:
			pyxel.blt(self.x,self.y,0,24,24,8,8,7)
		if self.type == 6:
			pyxel.blt(self.x,self.y,0,24,40,8,8,7)
		if self.type == 7:
			pyxel.blt(self.x,self.y,0,16,40,8,8,7)
		if self.type == 8:
			pyxel.blt(self.x,self.y,0,24,16,8,8,7)
		if self.type == 9:
			pyxel.blt(self.x,self.y,0,17,16,8,8,7)
		#if self.type == 10:
			#pyxel.blt(self.x,self.y,0,40,16,8,8,7)


#fusil = Objet(0,0,1)
botte = Objet(0,0,2)
gant = Objet(0,0,3)
heal = Objet(0,0,4)
onde_choc = Objet(0,0,5)
bouclier = Objet(0,0,6)
carte_reverse = Objet(0,0,7)
gel = Objet(0,0,8)
flamme = Objet(0,0,9)
#champignon = Objet(0,0,10)

#aide pour se rappeler des types.