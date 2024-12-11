from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['cruddb']
collection = db['users']

@app.route('/')
def index():
    users = collection.find()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        alamat = request.form['alamat']
        jurusan = request.form['jurusan']
        email = request.form['email']
        collection.insert_one({'nim': nim, 'nama': nama, 'alamat': alamat, 'jurusan': jurusan, 'email': email})
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    user = collection.find_one({'_id': ObjectId(id)})
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        alamat = request.form['alamat']
        jurusan = request.form['jurusan']
        email = request.form['email']
        collection.update_one({'_id': ObjectId(id)}, {'$set': {'nim': nim, 'nama': nama, 'alamat': alamat, 'jurusan': jurusan, 'email': email}})
        return redirect(url_for('index'))
    return render_template('edit.html', user=user)

@app.route('/delete/<id>')
def delete(id):
    collection.delete_one({'_id': ObjectId(id)})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
