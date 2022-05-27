#import modul dan file lainnya
import pygame
from pygame import draw
from pygame.locals import *
from random import randint
from bata import bata
from dayung import dayung
from bonus import bonus
from tombol import tombol

pygame.init()#hasil import modul untuk menjalankan program dibawahnya

#mendeskripsikan panjang dan lebar tampilan
lebar = 600
tinggi = 600

#membuat layar dengan ukuran besar x lebar
layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption('Breakout')

#mendefinisikan jenis dan ukuran tulisan
tulisan = pygame.font.SysFont('Constantia', 30)
warna_tulisan = (0,176,240)

#mendeskripsikan variabel variable yang digunakan
point = 0
bata_hancur = 0
hancurkan_baris = False
waktu = pygame.time.Clock()
fps = 60
bola_gerak = False
bola_keluar = 0

#fungsi untuk menampilkan tulisan
def tampil_tulisan(text, tulisan, warna_tulisan, x, y):
	tampilan = tulisan.render(text, True, warna_tulisan)
	layar.blit(tampilan, (x, y))

#membuat class bola
class bola():
	def __init__(self, x, y):
		self.kembali(x, y)

	#fungsi pergerakan bola
	def gerak(self):
		#mendeskripsikan variabel pada class bola
		batas = 5
		global point
		global bata_hancur
		global hancurkan_baris
		hancurkan_bata = 1
		baris = 0

		#menghitung banyaknya baris bata
		for baris_bata in bata.bata:
			kolom = 0
			#menghitung banyaknya kolom bata
			for kolom_bata in baris_bata:
				#ketika bola menyentuh bata
				if self.rect.colliderect(kolom_bata[0]):
					#ketika bola menyentuh bagian atas bata
					if abs(self.rect.bottom - kolom_bata[0].top) < batas and self.gerak_y > 0:
						self.gerak_y *= -1
					#ketika bola menyentuh bagian bawah bata
					if abs(self.rect.top - kolom_bata[0].bottom) < batas and self.gerak_y < 0:
						self.gerak_y *= -1						
					#ketika bola menyentuh bagian kiri bata
					if abs(self.rect.right - kolom_bata[0].left) < batas and self.gerak_x > 0:
						self.gerak_x *= -1
					#ketika bola menyentuh bagian kanan bata
					if abs(self.rect.left - kolom_bata[0].right) < batas and self.gerak_x < 0:
						self.gerak_x *= -1
					#kondisi dimana jika bata harus dihancurkan 2 kali
					if bata.bata[baris][kolom][1] > 1:
						bata.bata[baris][kolom][1] -= 1
					#kondisi dimana jika bata terkena bola akan hancur
					else:
						bata.bata[baris][kolom][0] = (0, 0, 0, 0)
						point +=1
						bata_hancur += 1
				#perulangan untuk menurunkan dan mengubah bata menjadi kolom+1
				x=0
				for  x in range(4):
					#kondisi dimana 1 baris bata hancur		
					if bata.bata[x][0][0] == (0, 0, 0, 0) and bata.bata[x][1][0] == (0, 0, 0, 0)and bata.bata[x][2][0] == (0, 0, 0, 0)and bata.bata[x][x][0] == (0, 0, 0, 0)and bata.bata[x][4][0] == (0, 0, 0, 0)and bata.bata[x][5][0] == (0, 0, 0, 0):
						a=3
						b=0
						while(a>=0):
							for b in range(6):
								#kondisi dimana bata akan turun satu baris
								if bata.bata[a][b][0] != (0,0,0,0):
									bata.bata[a][b][0][1] += 50
							a-=1
						a=3
						b=0
						while(a>=0):
							for b in range(6):
								#kondisi dimana jika masih ada bata baris bata menjadi baris+1
								if bata.bata[a][b][0] != (0,0,0,0):
									bata.bata[a+1][b] = bata.bata[a][b]
							a-=1
						hancurkan_baris = True

				if bata.bata[baris][kolom][0] != (0, 0, 0, 0):
					hancurkan_bata = 0
				kolom += 1
			baris += 1

		#kondisi dimana bola menyentu kiri atau kanan layar
		if self.rect.left < 0 or self.rect.right > lebar:
			self.gerak_x *= -1
		#kondisi dimana bola menyentu atas layar
		if self.rect.top < 0:
			self.gerak_y *= -1
		#kondisi dimana bola menyentu bawah layar 
		if self.rect.bottom > tinggi:
			self.bola_keluar = -1

		#kondisi dimana bola menyentu
		if self.rect.colliderect(dayung):
			#jika terkena dibagian atas dayung
			if abs(self.rect.bottom - dayung.rect.top) < batas and self.gerak_y > 0:
				self.gerak_y *= -1
				self.gerak_x += dayung.arah
				if self.gerak_x > self.kecepatan_max:
					self.gerak_x = self.kecepatan_max
				elif self.gerak_x < 0 and self.gerak_x < -self.kecepatan_max:
					self.gerak_x = -self.kecepatan_max
			#jika terkena dibagian bawah,kiri,atas dayung
			else:
				self.gerak_x *= -1
		#dimana posisi menjadi posisi + gerak
		self.rect.x += self.gerak_x
		self.rect.y += self.gerak_y
		#mengembalikan nilai bola_keluar
		return self.bola_keluar

	#fungsi penampilan bola dalam layar
	def tampil(self):
		pygame.draw.circle(layar, (142, 135, 123), (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad)
		pygame.draw.circle(layar, (100, 100, 100), (self.rect.x + self.ball_rad, self.rect.y + self.ball_rad), self.ball_rad, 3)

	#mendeskripsikan kembali posisi awal bola
	def kembali(self, x, y):
		self.ball_rad = 10
		self.x = x - self.ball_rad
		self.y = y
		self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
		self.gerak_x = 4
		self.gerak_y = -4
		self.kecepatan_max = 5
		self.bola_keluar = 0


#mendeskripsikan file ke dalam variable
bata = bata()
bata.tambah_bata()
dayung = dayung()
bonus = bonus()
bola = bola(dayung.x + (dayung.width // 2), dayung.y - dayung.height)
lanjut = tombol(200, 200, 'Lanjut')
ulang = tombol(200, 300, 'Ulang')
keluar = tombol(200, 400, 'Keluar')
merah = tombol(200, 200, 'Marah')
kuning = tombol(200, 300, 'Kuning')
hijau = tombol(200, 400, 'Hijau')
warna_dayung=0

#melakukan perulangan sampai nilai run = flase
run = True
while run:
	#60 pergerakan dalam 1 waktu
	waktu.tick(fps)
	#untuk menutup layar tanpa objek
	layar.fill((255,255,255))
	
	#dimana kondisi awal pemain memilih warna dayung
	if warna_dayung == 0 :
		if merah.tampil_tombol():
			warna_dayung = 1
			bola_gerak = True
		elif kuning.tampil_tombol():
			warna_dayung = 2
			bola_gerak = True
		elif hijau.tampil_tombol():
			warna_dayung = 3
			bola_gerak = True
		tampil_tulisan('MERAH', tulisan, warna_tulisan, 240,  220)
		tampil_tulisan('KUNING', tulisan, warna_tulisan, 240, 320)
		tampil_tulisan('HIJAU', tulisan, warna_tulisan, 240, 420)

	#menampilkan objek objek kelas diatas
	if warna_dayung == 1 :
		dayung.tampil_merah()
	elif warna_dayung == 2 :
		dayung.tampil_kuning()
	elif warna_dayung == 3 :
		dayung.tampil_hijau()
	bata.tampil()
	bola.tampil()
	
	#selama bola didalam daerah bola
	if bola_gerak:
		#mengerakkan dayung dan bola
		tampil_tulisan('Score : '+str(point), tulisan, warna_tulisan, 100, tinggi // 2 + 100)	
		dayung.gerak()
		bola_keluar = bola.gerak()
		if bola_keluar != 0:
			bola_gerak = False

	#kondisi dimana satu baris bata kosong
	if hancurkan_baris == True:
		#menampilkan 1 baris bata pada bagian atas
		bata.tambah_bata_baru()
		bata.tampil_bata_baru()
		b=0
		for b in range(6):
			bata.bata[0][b] = bata.bata_baru[0][b]
		hancurkan_baris = False

	#mengeluarkan dan mengerakan bonus apabila 3 bata hancyr
	if (bata_hancur%3==0 and bata_hancur != 0):
		bonus.tampil()
		bonus.gerak()
		#kondisi dimana bonus mengenai dayung
		if bonus.rect.colliderect(dayung):
			bata_hancur = 0
			point += 5
	elif(bata_hancur%3==2):
		#mengembalikan bonus keposisi awal
		bonus.kembali()

	#jika bola sudah menyentu bawah layar
	if not bola_gerak and warna_dayung != 0:
		if bola_keluar == -1:
			tampil_tulisan('Permainan Berakhir', tulisan, warna_tulisan, 180, tinggi // 2 + 50)
			tampil_tulisan('Tekan SPASI Untuk Ke Menu', tulisan, warna_tulisan, 120, tinggi // 2 + 100)

	#mendeskripsikan semua tombol yang dapat dilakukan di game
	for event in pygame.event.get():
		#kondisi dimana pemain menekan "x"
		if event.type == pygame.QUIT:
			run = False
		#kondisi dimana pemain menekan spasi
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			while True:#melakukan perulangan sampai diberhentikan mengunakan break 
				tampil_tulisan('Lanjut', tulisan, warna_tulisan, 250,  220)
				tampil_tulisan('Ulang', tulisan, warna_tulisan, 250, 320)
				tampil_tulisan('Keluar', tulisan, warna_tulisan, 250, 420)
				pygame.display.update()
				event = pygame.event.wait()
				#menekan tombol lanjut untuk melanjutkan permainan
				if lanjut.tampil_tombol():
					break
				#menekan tombol keluar untuk menutup aplikasi permainan
				if keluar.tampil_tombol():
					run = False
					break
				#menekan tombol ulang untuk mengulang permainan
				if ulang.tampil_tombol():
					#membuat semua ke posisi awal
					bola_gerak = False
					bola.kembali(dayung.x + (dayung.width // 2), dayung.y - dayung.height)
					point = 0
					bata_hancur = 0
					warna_dayung = 0
					bonus.kembali()
					dayung.kembali()
					bata.tambah_bata()
					break
				
	pygame.display.update()
pygame.quit()
