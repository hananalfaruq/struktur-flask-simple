from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Ganti sesuai kredensial PostgreSQL kamu
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123@localhost:5432/kampus'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model tabel mahasiswa
class Mahasiswa(db.Model):
    __tablename__ = 'mahasiswa'

    nim = db.Column(db.String(20), primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    tahun_masuk = db.Column(db.Integer, nullable=False)
    alamat = db.Column(db.Text, nullable=False)
    tanggal_lahir = db.Column(db.Date, nullable=False)

    def to_dict(self):
        return {
            "nim": self.nim,
            "nama": self.nama,
            "tahun_masuk": self.tahun_masuk,
            "alamat": self.alamat,
            "tanggal_lahir": self.tanggal_lahir.strftime("%Y-%m-%d")
        }

# 🔹 Endpoint: GET (semua data mahasiswa)
@app.route('/mahasiswa', methods=['GET'])
def get_all_mahasiswa():
    data = Mahasiswa.query.all()
    return jsonify([m.to_dict() for m in data])

# 🔹 Endpoint: POST (tambah mahasiswa baru)
@app.route('/mahasiswa', methods=['POST'])
def add_mahasiswa():
    data = request.json
    try:
        mhs = Mahasiswa(
            nim=data['nim'],
            nama=data['nama'],
            tahun_masuk=data['tahun_masuk'],
            alamat=data['alamat'],
            tanggal_lahir=datetime.strptime(data['tanggal_lahir'], "%Y-%m-%d")
        )
        db.session.add(mhs)
        db.session.commit()
        return jsonify({"message": "Mahasiswa berhasil ditambahkan!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400

# 🔹 Endpoint: DETAIL (GET by NIM)
@app.route('/mahasiswa/<string:nim>', methods=['GET'])
def get_detail_mahasiswa(nim):
    mhs = Mahasiswa.query.get(nim)
    if not mhs:
        return jsonify({"message": "Mahasiswa tidak ditemukan"}), 404
    return jsonify(mhs.to_dict())

# 🔹 Endpoint: DELETE (hapus mahasiswa berdasarkan NIM)
@app.route('/mahasiswa/<string:nim>', methods=['DELETE'])
def delete_mahasiswa(nim):
    mhs = Mahasiswa.query.get(nim)
    if not mhs:
        return jsonify({"message": "Mahasiswa tidak ditemukan"}), 404
    db.session.delete(mhs)
    db.session.commit()
    return jsonify({"message": "Mahasiswa berhasil dihapus!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)