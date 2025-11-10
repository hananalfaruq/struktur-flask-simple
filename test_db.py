from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Ganti username, password, dan nama database sesuai punya kamu
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/kampus'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Coba koneksi
with app.app_context():
    try:
        # Jalankan query sederhana
        db.session.execute('SELECT 1')
        print("✅ Koneksi ke PostgreSQL BERHASIL!")
    except Exception as e:
        print("❌ Koneksi GAGAL:", e)
