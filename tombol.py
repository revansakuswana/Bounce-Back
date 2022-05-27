import pygame
from pygame.locals import *
#mendeskripsikan variabel variable yang digunakan
lebar = 600
tinggi = 600
layar = pygame.display.set_mode((lebar, tinggi))


#membuat variable tombol_ditekan = false
tombol_ditekan = False

#membuat class tombol
class tombol():
	#warna warna pada tombol
	warna_tombol = (0, 0, 0)
	warna_latar_tombol = (75, 225, 255)
	click_col = (50, 150, 255)
	warna_tulisan = (0,0,0)
	width = 180
	height = 70

	def __init__(self, x, y, tulisan):
		self.x = x
		self.y = y
		self.tulisan = tulisan

	def tampil_tombol(self):
		#menjadikan tombol_ditekan menjadi global
		global tombol_ditekan
		aksi_tombol = False

		#mengambil posisi mose
		pos = pygame.mouse.get_pos()

		#mendapatkan posisi tombol pada layar
		button_rect = Rect(self.x, self.y, self.width, self.height)
		
		#mengecek tombol yang dikelik
		if button_rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1:
				tombol_ditekan = True
				pygame.draw.rect(layar, self.click_col, button_rect)
			elif pygame.mouse.get_pressed()[0] == 0 and tombol_ditekan == True:
				tombol_ditekan = False
				aksi_tombol = True
			else:
				pygame.draw.rect(layar, self.warna_latar_tombol, button_rect)
		else:
			pygame.draw.rect(layar, self.warna_tombol, button_rect)
		
		#menambahkan bayangan pada tombol
		pygame.draw.line(layar, (0,0,0), (self.x, self.y), (self.x + self.width, self.y), 2)
		pygame.draw.line(layar, (0,0,0), (self.x, self.y), (self.x, self.y + self.height), 2)
		#mengembalikan aksi yang akan dilakukan
		return aksi_tombol
