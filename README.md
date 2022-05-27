## Nama dan NIM Anggota Kelompok
| Nama | NIM | Github |
| :---: | :---: | :---: |
| Galih Ramadhan             | 120140104 | [ramadhangalih12](https://github.com/ramadhangalih12)     |
| Revansa Helsa Kuswana      | 120140096 | [revansakuswana](https://github.com/revansakuswana)       |
| Muhammad Bayu Pradana      | 119140144 | [Bayuprdana](https://github.com/Bayuprdana)               |
| Tamara Dwi Rahmadona       | 119140196 | [tamaradona](https://github.com/tamaradona)               |
| Tumbur Aprian Simorangkir  | 120140106 |                                                           |


## Bounce-Back
#### Deskripsi Projek
Bounce Back merupakan game yang mampu menampilkan objek pemantul yang warnanya dapat dipilih oleh user dan menampilkan objek bola, bata, bonus, score dan menghentikan game ketika menu permainan ditampilkan. Ketika bola menyentuh bagian bawah layar, maka game akan berakhir. Selain itu program akan menampilkan sebuah menu dimana pemain dapat memainkan game dimulai dari awal atau pemain ingin mengakhiri permainan.

## Cara Menjalankan Kontainer
Clone repositori ini atau [unduh disini](git@github.com:revansakuswana/Bounce-Back.git)lalu pindahkan pygame scripts ke folder `~/Downloads` seperti pada gambar berikut:

![]()

Selanjutnya buka terminal pada direktori folder tersebut lalu jalankan perintah build seperti berikut:

    make build

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

[![LIHAT VIDEO DISINI]()

KLIK GAMBAR UNTUK MELIHAT VIDEO
