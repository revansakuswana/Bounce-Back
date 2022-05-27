import pygame
from pygame import *
#mendeskripsikan variabel variable yang digunakan
lebar = 600
tinggi = 600
layar = pygame.display.set_mode((lebar, tinggi))

#membuat class dayung
class dayung():
	def __init__(self):
		self.kembali()

	#fungsi pergerakan dayung
	def gerak(self):
		self.arah = 0
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and self.rect.left > 0:
			self.rect.x -= self.pindah
			self.arah = -1
		if key[pygame.K_RIGHT] and self.rect.right < lebar:
			self.rect.x += self.pindah
			self.arah = 1

	#fungsi penampilan dayung warna merah dalam layar
	def tampil_merah(self):
		pygame.draw.rect(layar, (255,0,0), self.rect)
		pygame.draw.rect(layar, (100, 100, 100), self.rect, 3)

	#fungsi penampilan dayung warna kuning dalam layar
	def tampil_kuning(self):
		pygame.draw.rect(layar, (255,255,0), self.rect)
		pygame.draw.rect(layar, (100, 100, 100), self.rect, 3)

	#fungsi penampilan dayung warna hijau dalam layar
	def tampil_hijau(self):
		pygame.draw.rect(layar, (0,255,0), self.rect)
		pygame.draw.rect(layar, (100, 100, 100), self.rect, 3)

	#mendeskripsikan kembali posisi awal bonus
	def kembali(self):
		self.height = 20
		self.width = lebar // 6
		self.x = int((lebar / 2) - (self.width / 2))
		self.y = tinggi - (self.height * 2)
		self.pindah = 10
		self.rect = Rect(self.x, self.y, self.width, self.height)
		self.arah = 0


#
