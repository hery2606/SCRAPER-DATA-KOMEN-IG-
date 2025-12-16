# Instagram Comment Scraper

## Deskripsi

Script Python untuk melakukan scraping (ekstraksi) komentar dari postingan Instagram menggunakan Selenium WebDriver. Script ini dirancang untuk mengambil data komentar secara otomatis dan menyimpannya dalam format CSV.

Project ini juga dilengkapi **UI berbasis React + Tailwind (Glassmorphism)** sebagai frontend untuk mempermudah penggunaan.

---

## Fitur

* Login otomatis ke Instagram menggunakan file konfigurasi
* Otomatis menangani popup (Save Login Info, Notifications)
* Otomatis memuat komentar lama (Load more comments)
* Ekstraksi **username & teks komentar** saja (tanpa likes / reply)
* Filter duplikat komentar otomatis
* Penyimpanan hasil ke **CSV (UTF-8, support emoji)**
* UI modern **Glassmorphism + Loading + Skeleton Table**
* Export CSV langsung dari UI
* Struktur kode modular (Backend & Frontend terpisah)

---

## Teknologi yang Digunakan

### Backend

* Python 3.7+
* FastAPI
* Selenium WebDriver
* webdriver-manager
* python-dotenv

### Frontend

* React (Create React App)
* Tailwind CSS
* Fetch API

---

## Struktur Project

```
SCRAPING-DATA-KOMEN-IG-
│
├── API/                      # Backend (FastAPI + Selenium)
│   ├── main.py
│   ├── scraper.py
│   ├── config.py
│   ├── requirements.txt
│   └── .env.example
│
├── UI/                       # Frontend (React)
│   └── instagram-scraper-ui/
│       ├── src/
│       ├── package.json
│       ├── tailwind.config.js
│       └── postcss.config.js
│
├── README.md
└── .gitignore
```

---

# 🚀 Cara Menjalankan Project

## A. Menjalankan Backend (FastAPI)

### 1. Masuk ke folder backend

```bash
cd API
```

### 2. Buat & aktifkan virtual environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Jika manual:

```bash
pip install fastapi uvicorn selenium webdriver-manager python-dotenv pandas
```

### 4. Konfigurasi kredensial

Salin file contoh:

```bash
copy .env.example .env   # Windows
cp .env.example .env     # Linux/Mac
```

Isi file `.env`:

```env
INSTAGRAM_USERNAME=username_anda
INSTAGRAM_PASSWORD=password_anda
```

⚠️ **File `.env` TIDAK BOLEH di-commit ke Git**

---

### 5. Jalankan backend

```bash
python -m uvicorn main:app --reload
```

Backend aktif di:

* [http://127.0.0.1:8000](http://127.0.0.1:8000)
* Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## B. Menjalankan Frontend (React)

### 1. Masuk ke folder UI

```bash
cd UI/instagram-scraper-ui
```

### 2. Install dependencies

```bash
npm install
```

Pastikan Node.js ≥ 18

```bash
node -v
npm -v
```

### 3. Jalankan frontend

```bash
npm start
```

Frontend berjalan di:

```
http://localhost:3000
```

---

## Alur Aplikasi

1. User input URL postingan Instagram di UI
2. Frontend mengirim request ke backend FastAPI
3. Selenium membuka Instagram & login
4. Komentar di-scrape (username + komentar)
5. Data dikirim kembali ke frontend
6. User dapat melihat hasil & export CSV

---

## Output CSV

File CSV berisi:

| Username | Komentar      |
| -------- | ------------- |
| user1    | Keren banget! |
| user2    | Nice post 👍  |

Encoding: **utf-8-sig** (aman untuk Excel & emoji)

---

## Troubleshooting

### Backend tidak bisa diakses

* Pastikan backend berjalan di port 8000
* Pastikan virtual environment aktif

### Selenium error / Chrome tidak terbuka

* Pastikan Google Chrome terinstall
* Versi Chrome up-to-date
* webdriver-manager akan otomatis menyesuaikan driver

### Tidak ada komentar terambil

* Pastikan postingan public
* Instagram bisa mengubah struktur HTML
* Tambah delay / load more di `config.py`

---

## Keamanan

❌ Jangan commit `.env`
❌ Jangan hardcode password
✅ Gunakan environment variable
✅ Ganti password jika terlanjur bocor

---

## Catatan Penting

⚠️ Script ini dibuat **untuk tujuan edukasi & akademik**.
Gunakan secara bijak dan patuhi Terms of Service Instagram.

---

## Lisensi

Proyek ini dibuat untuk keperluan akademik dan pembelajaran.

---

**Dibuat untuk Mata Kuliah Data Mining – Semester 5**
