from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# --- Konfigurasi koneksi ke PostgreSQL ---
conn = psycopg2.connect(
    host="localhost",
    database="kampus",
    user="postgres",
    password="123"  # Ganti sesuai konfigurasi PostgreSQL kamu
)

# ---------------- HALAMAN UTAMA ----------------
@app.route('/')
def index():
    return render_template('index.html')


# ---------------- CRUD MAHASISWA ----------------
@app.route('/mahasiswa')
def mahasiswa():
    cur = conn.cursor()
    cur.execute("SELECT * FROM mahasiswa ORDER BY id_mahasiswa;")
    data = cur.fetchall()
    cur.close()
    return render_template('mahasiswa.html', mahasiswa=data)

@app.route('/tambah_mahasiswa', methods=['POST'])
def tambah_mahasiswa():
    nim = request.form['nim']
    nama = request.form['nama']
    tanggal_lahir = request.form['tanggal_lahir']
    alamat = request.form['alamat']
    tahun_masuk = request.form['tahun_masuk']

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO mahasiswa (nim, nama, tanggal_lahir, alamat, tahun_masuk) VALUES (%s, %s, %s, %s, %s)",
        (nim, nama, tanggal_lahir, alamat, tahun_masuk)
    )
    conn.commit()
    cur.close()
    return redirect(url_for('mahasiswa'))

@app.route('/hapus_mahasiswa/<int:id_mahasiswa>')
def hapus_mahasiswa(id_mahasiswa):
    cur = conn.cursor()
    cur.execute("DELETE FROM mahasiswa WHERE id_mahasiswa = %s", (id_mahasiswa,))
    conn.commit()
    cur.close()
    return redirect(url_for('mahasiswa'))


# ---------------- CRUD MATAKULIAH ----------------
@app.route('/matakuliah')
def matakuliah():
    cur = conn.cursor()
    cur.execute("SELECT * FROM matakuliah ORDER BY id_mk;")
    data = cur.fetchall()
    cur.close()
    return render_template('matakuliah.html', matakuliah=data)

@app.route('/tambah_matakuliah', methods=['POST'])
def tambah_matakuliah():
    kode_mk = request.form['kode_mk']
    nama_mk = request.form['nama_mk']
    sks = request.form['sks']

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO matakuliah (kode_mk, nama_mk, sks) VALUES (%s, %s, %s)",
        (kode_mk, nama_mk, sks)
    )
    conn.commit()
    cur.close()
    return redirect(url_for('matakuliah'))

@app.route('/hapus_matakuliah/<int:id_mk>')
def hapus_matakuliah(id_mk):
    cur = conn.cursor()
    cur.execute("DELETE FROM matakuliah WHERE id_mk = %s", (id_mk,))
    conn.commit()
    cur.close()
    return redirect(url_for('matakuliah'))


# ---------------- CRUD KELAS ----------------
@app.route('/kelas')
def kelas():
    cur = conn.cursor()
    cur.execute("""
        SELECT k.id_kelas, mk.nama_mk, k.nama_kelas, k.semester, k.tahun_ajaran
        FROM kelas k
        JOIN matakuliah mk ON k.id_mk = mk.id_mk
        ORDER BY k.id_kelas;
    """)
    data = cur.fetchall()
    cur.close()
    return render_template('kelas.html', kelas=data)

@app.route('/tambah_kelas', methods=['POST'])
def tambah_kelas():
    id_mk = request.form['id_mk']
    nama_kelas = request.form['nama_kelas']
    semester = request.form['semester']
    tahun_ajaran = request.form['tahun_ajaran']

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO kelas (id_mk, nama_kelas, semester, tahun_ajaran) VALUES (%s, %s, %s, %s)",
        (id_mk, nama_kelas, semester, tahun_ajaran)
    )
    conn.commit()
    cur.close()
    return redirect(url_for('kelas'))

@app.route('/hapus_kelas/<int:id_kelas>')
def hapus_kelas(id_kelas):
    cur = conn.cursor()
    cur.execute("DELETE FROM kelas WHERE id_kelas = %s", (id_kelas,))
    conn.commit()
    cur.close()
    return redirect(url_for('kelas'))


# ---------------- RELASI MAHASISWA - KELAS ----------------
@app.route('/mahasiswa_kelas')
def mahasiswa_kelas():
    cur = conn.cursor()
    cur.execute("""
        SELECT mk.id, m.nama, k.nama_kelas, k.tahun_ajaran
        FROM mahasiswa_kelas mk
        JOIN mahasiswa m ON mk.id_mahasiswa = m.id_mahasiswa
        JOIN kelas k ON mk.id_kelas = k.id_kelas
        ORDER BY mk.id;
    """)
    data = cur.fetchall()
    cur.close()
    return render_template('mahasiswa_kelas.html', mahasiswa_kelas=data)

@app.route('/tambah_mahasiswa_kelas', methods=['POST'])
def tambah_mahasiswa_kelas():
    id_mahasiswa = request.form['id_mahasiswa']
    id_kelas = request.form['id_kelas']

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO mahasiswa_kelas (id_mahasiswa, id_kelas) VALUES (%s, %s)",
        (id_mahasiswa, id_kelas)
    )
    conn.commit()
    cur.close()
    return redirect(url_for('mahasiswa_kelas'))

@app.route('/hapus_mahasiswa_kelas/<int:id>')
def hapus_mahasiswa_kelas(id):
    cur = conn.cursor()
    cur.execute("DELETE FROM mahasiswa_kelas WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    return redirect(url_for('mahasiswa_kelas'))


if __name__ == '__main__':
    app.run(debug=True)
