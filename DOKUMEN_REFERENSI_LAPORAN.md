# REFERENSI PENULISAN LAPORAN TUGAS BESAR
## Proyek: API Daftar Tugas (To-Do List) Cloud-Native

Dokumen ini disusun untuk memberikan informasi teknis lengkap guna memenuhi kebutuhan sistematika laporan kuliah.

---

### BAB I – PENDAHULUAN
- **Latar Belakang:** Kebutuhan akan aplikasi manajemen tugas yang dapat diakses secara fleksibel dan skalabel. Proyek ini mendemonstrasikan implementasi API berbasis web yang dideploy menggunakan teknologi Cloud (PaaS).
- **Tujuan:** 
    1. Mengimplementasikan API CRUD menggunakan framework Flask.
    2. Mengintegrasikan database PostgreSQL sebagai penyimpanan data persisten.
    3. Melakukan deployment ke platform Railway (Platform-as-a-Service).
- **Manfaat:** Memahami siklus pengembangan perangkat lunak modern (DevOps) dan penggunaan layanan Cloud untuk mempercepat deployment tanpa mengelola infrastruktur server secara manual.

---

### BAB II – LANDASAN TEORI
- **PaaS (Platform-as-a-Service):** Layanan cloud yang menyediakan platform bagi pengembang untuk membangun, menjalankan, dan mengelola aplikasi tanpa kerumitan membangun infrastruktur sendiri.
- **Justifikasi Memilih Railway:**
    1. **Kemudahan Integrasi Git:** Deployment otomatis setiap kali ada perubahan kode di GitHub.
    2. **Managed Database:** PostgreSQL disediakan sebagai service terpisah yang mudah dikonfigurasi.
    3. **Efisiensi Biaya & Waktu:** Sangat cocok untuk mahasiswa karena setup-nya cepat dan memiliki free tier/credits yang memadai.

---

### BAB III – PERANCANGAN
- **Arsitektur Sistem:**
    - **Frontend:** Client (Browser/CURL/Postman).
    - **Backend:** Flask (Python) berjalan di container Railway.
    - **Database:** PostgreSQL (Railway Managed Service).
    - **Proxy/Gateway:** Railway Networking (menangani HTTPS/SSL).
- **Struktur Berkas (Folder):**
    ```text
    /TM2
    ├── app.py              # Logika API & Endpoint
    ├── models.py           # Skema Database (SQLAlchemy)
    ├── requirements.txt    # Daftar Dependensi
    ├── Procfile            # Instruksi proses Gunicorn
    ├── railway.toml        # Konfigurasi Build & Deploy Railway
    ├── migrations/         # File migrasi database (Flask-Migrate)
    ├── .gitignore          # File yang diabaikan Git
    └── README.md           # Dokumentasi singkat
    ```
- **Skema Database (Tabel: `todos`):**
    - `id` (Integer, Primary Key)
    - `title` (String 100, Not Null)
    - `description` (String 255)
    - `done` (Boolean, Default: False)
    - `created_at` (DateTime, Default: UTC)

---

### BAB IV – IMPLEMENTASI
- **Teknologi:** Python 3.10+, Flask, Flask-SQLAlchemy, Flask-Migrate, Gunicorn.
- **Konfigurasi Variabel Lingkungan (Environment Variables):**
    - `DATABASE_URL`: `${{Postgres.DATABASE_URL}}` (Referensi dinamis ke database).
    - `SECRET_KEY`: Kunci enkripsi untuk keamanan session.
    - `PORT`: Diatur otomatis oleh Railway.
- **Proses Deployment:**
    1. Inisialisasi Git dan Push ke GitHub.
    2. Menghubungkan repo GitHub ke Railway.
    3. Menambahkan plugin PostgreSQL di dashboard Railway.
    4. Konfigurasi `railway.toml` untuk menjalankan `flask db upgrade` otomatis sebelum aplikasi start.

---

### BAB V – PENGUJIAN
- **Endpoint yang Berhasil Diuji:**
    - `GET /`: Informasi API.
    - `GET /health`: Status kesehatan (Database Connected).
    - `GET /todos`: List semua tugas.
    - `POST /todos`: Pembuatan tugas baru (JSON body).
    - `PUT /todos/<id>`: Update status tugas (Selesai/Belum).
    - `DELETE /todos/<id>`: Penghapusan tugas dari database.
- **Hasil Pengujian Lengkap (Verified):**
    - **Health Check:** Database terverifikasi `"connected"`.
    - **CRUD Cycle:** Berhasil membuat data (POST), mengubah status menjadi selesai (PUT), dan menghapus data (DELETE) secara permanen dari PostgreSQL.
- **Monitoring:** Menggunakan log bawaan Railway untuk memantau trafik dan memastikan tidak ada error selama operasi CRUD.

---

### BAB VI – PENUTUP
- **Kesimpulan:** Implementasi Flask API pada platform Railway berhasil dilakukan dengan integrasi PostgreSQL yang mulus.
- **Kendala & Solusi:**
    1. **Kendala DATABASE_URL:** Awalnya aplikasi gagal terhubung karena menggunakan `localhost`. 
       **Solusi:** Menggunakan variabel referensi `${{Postgres.DATABASE_URL}}` di dashboard Railway.
    2. **Kendala Port Binding:** Aplikasi tidak merespon (Empty Response).
       **Solusi:** Menambahkan `-b 0.0.0.0:$PORT` pada perintah Gunicorn untuk memastikan aplikasi mendengarkan pada port yang disediakan Railway.
- **Saran:** Untuk pengembangan selanjutnya, disarankan menambahkan sistem autentikasi (JWT) dan dokumentasi API interaktif menggunakan Swagger (Flasgger).

---

### DAFTAR PUSTAKA
1. Flask Documentation. (2024). *Flask: A Python Microframework*. https://flask.palletsprojects.com/
2. Railway Documentation. (2024). *Deploying Applications on Railway*. https://docs.railway.app/
3. SQLAlchemy Docs. (2024). *SQLAlchemy ORM for Python*. https://www.sqlalchemy.org/
4. Grinberg, M. (2018). *Flask Web Development*. O'Reilly Media.
5. Python Dotenv. (2024). *Managing Environment Variables in Python*. https://pypi.org/project/python-dotenv/

---

### LAMPIRAN
- **URL Publik:** https://web-production-87460.up.railway.app
- **Repository:** https://github.com/zamzamyst/flask-todo-list-api.git
- **Tangkapan Layar:** (Dapat diambil dari dashboard Railway dan hasil browser).
