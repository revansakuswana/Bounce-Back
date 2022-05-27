import pygame
from random import randint
from pygame.locals import *

#mendeskripsikan panjang dan lebar tampilan
lebar = 600
tinggi = 600

#membuat layar dengan ukuran besar x lebar
layar = pygame.display.set_mode((lebar, tinggi))

class bonus():
	def __init__(self):
		self.kembali()

	#fungsi pergerakan bonus
	def gerak(self):
		self.direction = 0
		#dimana posisi menjadi posisi + gerak
		self.rect.y += self.kecepatan

	#fungsi penampilan bola dalam layar
	def tampil(self):
		pygame.draw.rect(layar, (0, 255, 0), self.rect)
		pygame.draw.rect(layar, (100, 100, 100), self.rect, 3)

	#mendeskripsikan kembali posisi awal bonus
	def kembali(self):
		self.height = 10
		self.width = 10
		self.x = randint(20,580)
		self.y = 10
		self.kecepatan = 4
		self.rect = Rect(self.x, self.y, self.width, self.height)
		self.direction = 0