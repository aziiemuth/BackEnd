from flask import Flask, render_template, request, redirect, url_for
import pymysql
import pymysql.cursors

application = Flask(__name__)

conn = cursor = None

# Fungsi koneksi database
def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost", user="root", passwd="", database="stok")
    cursor = conn.cursor()

# Fungsi untuk menutup koneksi
def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

# Fungsi view index() untuk menampilkan data dari database
@application.route('/')
def index():
    openDb()
    container = []
    sql = "SELECT * FROM barang"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        container.append(data)
    closeDb()
    return render_template('index.html', container=container)

# Fungsi view tambah() untuk membuat form tambah
@application.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kodebrg = request.form['kode']
        namabrg = request.form['nama']
        harga = request.form['harga']
        jumlah = request.form['jumlah']
        openDb()
        sql = "INSERT INTO barang (kodebrg, namabrg, harga, jumlah) VALUES (%s, %s, %s, %s)"
        val = (kodebrg, namabrg, harga, jumlah)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('tambah.html')

# Fungsi view edit() untuk form edit
@application.route('/edit/<id_barang>', methods=['GET', 'POST'])
def edit(id_barang):
    openDb()
    cursor.execute('SELECT * FROM barang WHERE id_barang=%s', (id_barang,))
    data = cursor.fetchone()
    if request.method == 'POST':
        id_barang = request.form['id_barang']
        kodebrg = request.form['kode']
        namabrg = request.form['nama']
        harga = request.form['harga']
        jumlah = request.form['jumlah']
        sql = "UPDATE barang SET kodebrg=%s, namabrg=%s, harga=%s, jumlah=%s WHERE id_barang=%s"
        val = (kodebrg, namabrg, harga, jumlah, id_barang)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        closeDb()
        return render_template('edit.html', data=data)

# Fungsi untuk menghapus data
@application.route('/hapus/<id_barang>', methods=['GET', 'POST'])
def hapus(id_barang):
    openDb()
    cursor.execute('DELETE FROM barang WHERE id_barang=%s', (id_barang,))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)
