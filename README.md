## Nama dan NIM Anggota Kelompok
| Nama | NIM | Github |
| :---: | :---: | :---: |
| Galih Ramadhan             | 120140104 | [ramadhangalih12](https://github.com/ramadhangalih12)     |
| Revansa Helsa Kuswana      | 120140096 | [revansakuswana](https://github.com/revansakuswana)       |
| Tumbur Aprian Simorangkir  | 120140106 | [naufaldewanto37](https://github.com/naufaldewanto37)     |
| Tamara Dwi Rahmadona       | 119140196 | [Zkaaaaaaa](https://github.com/Zkaaaaaaa)                 |
| Muhammad Bayu Pradana      | 119140144 | [Bayuprdana](https://github.com/Bayuprdana)               |
| Andri Setiawan             | 120140191 | [Andri450](https://github.com/Andri450)                   |

## Bounce-Back
#### Deskripsi Projek
Bounce Back merupakan game yang mampu menampilkan objek pemantul yang warnanya dapat dipilih oleh user dan menampilkan objek bola, bata, bonus, score dan menghentikan game ketika menu permainan ditampilkan. Ketika bola menyentuh bagian bawah layar, maka game akan berakhir. Selain itu program akan menampilkan sebuah menu dimana pemain dapat memainkan game dimulai dari awal atau pemain ingin mengakhiri permainan.

## Cara Menjalankan Kontainer
Clone repositori ini atau [unduh disini](https://github.com/riecho14/Docker-Dendam-Si-Tikus/archive/refs/heads/main.zip) lalu pindahkan pygame scripts ke folder `~/Downloads` seperti pada gambar berikut:

![1](https://github.com/riecho14/Docker-Dendam-Si-Tikus/blob/a2eb90dc3131332f08d6dcbeefd0014c4d22d89b/1.png)

Selanjutnya buka terminal pada direktori folder tersebut lalu jalankan perintah build seperti berikut:

    make build-dendamsitikus

lalu pastikan ada repositori "dendamsitikus" pada docker, dengan cara jalankan command images untuk melihat daftar images pada local storage seperti berikut:

    docker images

Jika proses build telah selesai, jalankan perintah run seperti berikut:

untuk Windows

    make run-windows

untuk Linux

    make run-linux

untuk Mac

    make run-mac

Langkah terakhir yaitu menjalankan pygame melalui container yang telah kita buat dengan perintah seperti berikut:

    python3 -m main.py

## Video Demo Kontainer

[![LIHAT VIDEO DISINI](http://img.youtube.com/vi/SO_tl0iAmhU/0.jpg)](http://www.youtube.com/watch?v=SO_tl0iAmhU)

KLIK GAMBAR UNTUK MELIHAT VIDEO
