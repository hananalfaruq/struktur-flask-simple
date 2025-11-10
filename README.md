# 🎓 Flask PostgreSQL CRUD – Mahasiswa App

Aplikasi **REST API sederhana** menggunakan **Flask** dan **PostgreSQL** untuk mengelola data mahasiswa.  
Aplikasi ini memiliki 4 endpoint utama: **GET**, **POST**, **DETAIL (GET by NIM)**, dan **DELETE**.

---

## 📚 Fitur Utama

- ✅ Menampilkan semua data mahasiswa  
- ➕ Menambahkan data mahasiswa baru  
- 🔍 Melihat detail mahasiswa berdasarkan NIM  
- ❌ Menghapus data mahasiswa berdasarkan NIM  

---

## 🗃️ Struktur Database

**Nama Database:** `kampus`  
**Tabel:** `mahasiswa`

| Kolom          | Tipe Data    | Keterangan |
|----------------|--------------|-------------|
| nim            | VARCHAR(20)  | Primary Key |
| nama           | VARCHAR(100) | Nama mahasiswa |
| tahun_masuk    | INT          | Tahun pertama kuliah |
| alamat         | TEXT         | Alamat rumah |
| tanggal_lahir  | DATE         | Format: YYYY-MM-DD |

---

## ⚙️ Instalasi dan Menjalankan Aplikasi

### 1️⃣ Clone repository
```bash
git clone https://github.com/username/nama-repo.git
cd nama-repo
