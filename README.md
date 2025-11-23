# 🧑‍💻 Aplikasi CRUD Flask - Sistem Data Kampus

Proyek ini adalah aplikasi web berbasis **Python Flask** yang terhubung ke **PostgreSQL**.  
Aplikasi ini menyediakan fitur CRUD (Create, Read, Update, Delete) untuk mengelola data:
- Mahasiswa  
- Mata Kuliah  
- Kelas  
- Relasi Mahasiswa dan Kelas

---

## 🚀 Fitur Utama
- Tambah, lihat, dan hapus data mahasiswa  
- Tambah, lihat, dan hapus data mata kuliah  
- Tambah, lihat, dan hapus data kelas  
- Relasi mahasiswa dengan kelas (many-to-many)  
- Interface sederhana berbasis HTML

---

## 🗂️ Struktur Folder
```
flask_crud/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── mahasiswa.html
│   ├── matakuliah.html
│   ├── kelas.html
│   └── mahasiswa_kelas.html
└── requirements.txt
```

---

## ⚙️ Instalasi dan Konfigurasi

### 1. Clone Repository
```bash
git clone https://github.com/username/flask-crud-kampus.git
cd flask-crud-kampus
```

### 2. Buat Virtual Environment (Opsional)
```bash
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate   # (Windows)
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Buat Database di PostgreSQL
Buat database baru bernama `kampus`:
```sql
CREATE DATABASE kampus;
```

### 5. Jalankan Script SQL
Gunakan SQL berikut untuk membuat tabel:
```sql
-- Jalankan script pembuatan tabel dan data awal
-- (gunakan file .sql yang telah kamu buat)
```

### 6. Jalankan Aplikasi Flask
```bash
python app.py
```

Lalu buka browser dan akses:
```
http://127.0.0.1:5000
```

---

## 🧩 Teknologi yang Digunakan
- **Python 3.x**
- **Flask**
- **PostgreSQL**
- **psycopg2**
- **HTML + Jinja2**
