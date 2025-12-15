# Instagram Comment Scraper

## Deskripsi
Script Python untuk melakukan scraping (ekstraksi) komentar dari postingan Instagram menggunakan Selenium WebDriver. Script ini dirancang untuk mengambil data komentar secara otomatis dan menyimpannya dalam format CSV.

## Fitur
- Login otomatis ke Instagram
- Otomatis menangani popup (Save Login Info, Notifications)
- Otomatis memuat komentar lama dengan mengklik tombol "Load more"
- Ekstraksi username dan teks komentar
- Penyimpanan hasil dalam format CSV dengan encoding UTF-8
- Support untuk emoji dan karakter khusus
- Filter duplikat komentar otomatis
- Struktur kode modular (3 file terpisah)

## Requirements
- Python 3.7 atau lebih tinggi
- Google Chrome browser
- Koneksi internet aktif

## Instalasi

### 1. Clone atau Download Project
```bash
cd d:\SEMESTER 5\TEORI\DataMINIG\scraping
```

### 2. Buat Virtual Environment (Opsional tapi Direkomendasikan)
```bash
python -m venv .venv
```

### 3. Aktifkan Virtual Environment
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install selenium pandas webdriver-manager
```

Atau menggunakan requirements.txt (jika ada):
```bash
pip install -r requirements.txt
```

## Konfigurasi

### 1. Setup Kredensial Instagram
Buka file `config.py` dan isi dengan kredensial Anda:

```python
# Konfigurasi Login Instagram
INSTAGRAM_USERNAME = "username_anda"  # Ganti dengan username Instagram Anda
INSTAGRAM_PASSWORD = "password_anda"  # Ganti dengan password Instagram Anda
```

⚠️ **PENTING**: Jangan share file `config.py` ke publik karena berisi password Anda!

### 2. Setup URL Postingan
Masih di file `config.py`, atur URL postingan yang ingin di-scrape:

```python
# Konfigurasi Scraping
POST_URL = "https://www.instagram.com/p/DSKpDExgYeO/?img_index=1"  # Ganti dengan link postingan target
MAX_COMMENTS = 50  # Target jumlah komentar
SCROLL_PAUSE = 2  # Jeda scroll dalam detik
LOAD_MORE_ATTEMPTS = 5  # Berapa kali mencoba klik "Load More"
```

## Cara Penggunaan

### 1. Jalankan Script
```bash
python main.py
```

### 2. Proses Otomatis
Script akan menjalankan proses berikut secara otomatis:

1. **Setup Browser**
   - Browser Chrome akan terbuka secara otomatis
   - Halaman login Instagram akan dimuat

2. **Login Otomatis**
   - Script akan mengisi username dan password secara otomatis
   - Klik tombol login
   - Menangani popup "Save Login Info" (klik "Not Now")
   - Menangani popup "Turn on Notifications" (klik "Not Now")

3. **Navigasi ke Postingan**
   - Membuka URL postingan yang telah dikonfigurasi
   - Menunggu halaman dimuat sempurna

4. **Load Komentar**
   - Mencoba klik tombol "Load more comments" beberapa kali
   - Melakukan scroll untuk memuat lebih banyak komentar

5. **Ekstraksi Data**
   - Mengambil username dan teks komentar
   - Menampilkan preview di terminal
   - Memfilter duplikat otomatis

6. **Simpan Hasil**
   - Menyimpan hasil ke file `hasil_komentar_ig.csv`
   - Menampilkan preview data

### 3. Output di Terminal
Contoh output yang akan ditampilkan:
```
>>> Menyiapkan browser...
>>> Memulai login otomatis...
>>> Menunggu proses login...
>>> Popup 'Save Login Info' ditutup
>>> Popup 'Notifications' ditutup
>>> Login berhasil!

>>> Membuka: https://www.instagram.com/p/DSKpDExgYeO/?img_index=1

>>> Mencoba memuat komentar lama...
Tombol Load More ditekan (1)...
Tombol Load More ditekan (2)...

--- Memulai Ekstraksi ---
Deteksi awal: Ditemukan 150 elemen teks potensial.
[V] user1: Keren banget!...
[V] user2: Nice post 👍...
[V] user3: Love it! 😍...

✓ SUKSES! 45 komentar disimpan ke 'hasil_komentar_ig.csv'

Preview data:
   Username              Komentar
0    user1          Keren banget!
1    user2        Nice post 👍
2    user3          Love it! 😍
...
```

## Output
Hasil scraping akan disimpan dalam file **hasil_komentar_ig.csv** dengan format:

| Username | Komentar |
|----------|----------|
| user1    | Keren banget! |
| user2    | Nice post 👍 |
| user3    | Love it! 😍 |

File CSV menggunakan encoding `utf-8-sig` agar dapat dibuka dengan baik di Microsoft Excel dan mendukung emoji.

## Struktur Project
```
scraping/
├── main.py                    # File utama untuk menjalankan program
├── scraper.py                 # Class untuk logic scraping
├── config.py                  # Konfigurasi (username, password, URL)
├── readme                     # Dokumentasi (file ini)
├── hasil_komentar_ig.csv     # Output hasil scraping (generated)
├── .venv/                     # Virtual environment (opsional)
└── .gitignore                 # Ignore file config.py (jika pakai Git)
```

### Penjelasan File:
- **main.py**: Entry point, mengatur alur program dari setup browser hingga save CSV
- **scraper.py**: Berisi class `InstagramScraper` dengan method login dan extract comments
- **config.py**: Menyimpan semua konfigurasi (username, password, URL postingan)

## Troubleshooting

### Browser tidak terbuka
- Pastikan Google Chrome sudah terinstall
- Coba update Chrome ke versi terbaru
- Pastikan ChromeDriver compatible dengan versi Chrome Anda

### Login gagal atau error
- Periksa kembali username dan password di `config.py`
- Pastikan koneksi internet stabil
- Instagram mungkin meminta verifikasi (cek email/SMS)
- Coba gunakan akun yang sudah pernah login di browser sebelumnya

### Tidak ada komentar yang terambil
- Periksa apakah postingan memiliki komentar
- Instagram sering mengubah struktur HTML mereka
- Coba tambah nilai `SCROLL_PAUSE` dan `LOAD_MORE_ATTEMPTS` di config.py
- Pastikan postingan bersifat public (bukan private)

### Browser langsung tertutup
- Comment baris `driver.quit()` di `main.py` untuk melihat error
- Uncomment baris tersebut jika sudah selesai testing

### Error "ElementNotFound"
- Instagram mungkin mengubah selector HTML
- Tunggu beberapa detik lebih lama dengan menambah `time.sleep()`
- Update selector di `scraper.py` sesuai struktur HTML terbaru

## Tips Penggunaan

### 1. Untuk Scraping Banyak Postingan
Edit `config.py` dan ubah `POST_URL` setiap kali scraping, atau:
- Buat list URL di config
- Loop di `main.py` untuk scrape multiple posts

### 2. Menghindari Deteksi Bot
- Jangan scrape terlalu banyak dalam waktu singkat
- Tambah jeda random: `time.sleep(random.uniform(2, 5))`
- Gunakan headless mode dengan hati-hati (lebih mudah terdeteksi)

### 3. Menyimpan Config dengan Aman
Buat file `.gitignore` dan tambahkan:
```
config.py
.venv/
hasil_komentar_ig.csv
__pycache__/
```

## Catatan Penting
⚠️ **Peringatan:**
- Script ini hanya untuk tujuan edukasi dan penelitian
- Pastikan Anda mematuhi Terms of Service Instagram
- Jangan melakukan scraping berlebihan yang dapat membebani server Instagram
- Gunakan dengan bijak dan bertanggung jawab
- Instagram dapat memblokir akun jika mendeteksi aktivitas mencurigakan
- **JANGAN SHARE** file `config.py` yang berisi password Anda

## Lisensi
Proyek ini dibuat untuk keperluan akademik dan pembelajaran.

## Kontak
Untuk pertanyaan atau saran, silakan hubungi developer.

---
**Dibuat untuk keperluan Data Mining - Semester 5**