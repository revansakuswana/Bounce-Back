import pygame
from random import randint
from pygame.locals import *
#mendeskripsikan variabel variable yang digunakan
lebar = 600
tinggi = 600
layar = pygame.display.set_mode((lebar, tinggi))
kolom = 6
baris = 4
bata_oren = (255,100,0)
bata_abu_abu = (128,128,128)

#membuat class bata
class bata():
	def __init__(self):
		self.width = lebar // kolom
		self.height = 50

	#membuat bata sesuai dengan banyaknya dalam layar
	def tambah_bata(self):
		self.bata = []
		satuan_bata = []
		for row in range(baris):
			baris_bata = []
			for col in range(kolom):
				#menetapkan posisi bata pada layar
				blok_x = col * self.width
				blok_y = row * self.height
				rect = pygame.Rect(blok_x, blok_y, self.width, self.height)
				if row < 4:
					strength = randint(1,1)
				#menambahkan letak dan banyak hit pada bata
				satuan_bata = [rect, strength]
				#menambahkan satuan_bata ke dalam baris_bata
				baris_bata.append(satuan_bata)
			#menambahkan baris_bata ke dalam bata untuk keseluruhan bata
			self.bata.append(baris_bata)

	#menambahkan 1 baris bata dari atas
	def tambah_bata_baru(self):
		self.bata_baru = []
		satuan_bata_baru = []
		for row in range(1):
			baris_bata_baru = []
			for col in range(kolom):
				#menetapkan posisi bata pada layar
				blok_x = col * self.width
				blok_y = row * self.height
				rect = pygame.Rect(blok_x, blok_y, self.width, self.height)
				if row < 4:
					strength = randint(1,2)
				#menambahkan letak dan banyak hit pada bata
				satuan_bata_baru = [rect, strength]
				#menambahkan satuan_bata ke dalam baris_bata
				baris_bata_baru.append(satuan_bata_baru)
			#menambahkan baris_bata ke dalam bata untuk keseluruhan bata
			self.bata_baru.append(baris_bata_baru)

	#meampilkan seluruh bata
	def tampil(self):
		for row in self.bata:
			for blok in row:
				#mendeskripsikan warna bata sesuai jumlah hit
				if blok[1] == 2:
					warna_bata = bata_abu_abu
				elif blok[1] == 1:
					warna_bata = bata_oren
				pygame.draw.rect(layar, warna_bata, blok[0])
				pygame.draw.rect(layar, (255,255,255), (blok[0]), 2)

	#meampilkan 1 baris bata
	def tampil_bata_baru(self):	
		for row in self.bata_baru:
			for blok in row:
				#mendeskripsikan warna bata sesuai jumlah hit
				if blok[1] == 2:
					warna_bata = bata_abu_abu
				elif blok[1] == 1:
					warna_bata = bata_oren
				pygame.draw.rect(layar, warna_bata, blok[0])
				pygame.draw.rect(layar, (255,255,255), (blok[0]), 2)
