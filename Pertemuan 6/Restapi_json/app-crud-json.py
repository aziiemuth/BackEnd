from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)

# Path ke file JSON
DATA_FILE = 'data/clients.json'

# Fungsi untuk memuat data dari file JSON
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

# Fungsi untuk menyimpan data ke file JSON
def save_data(clients):
    with open(DATA_FILE, 'w') as file:
        json.dump(clients, file, indent=4)

# Route untuk menampilkan semua client
@app.route('/')
def index():
    clients = load_data()
    return render_template('clients.html', clients=clients)

# Route untuk menambahkan client baru
@app.route('/add', methods=['POST'])
def add_client():
    clients = load_data()
    name = request.form.get('name')
    email = request.form.get('email')
    if name and email:
        clients.append({"name": name, "email": email})
        save_data(clients)
    return redirect(url_for('index'))

# Route untuk mengedit client
@app.route('/edit/<int:client_id>', methods=['GET', 'POST'])
def edit_client(client_id):
    clients = load_data()
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        if name and email:
            clients[client_id]['name'] = name
            clients[client_id]['email'] = email
            save_data(clients)
        return redirect(url_for('index'))
    return render_template('edit.html', client=clients[client_id], client_id=client_id)

# Route untuk menghapus client
@app.route('/delete/<int:client_id>')
def delete_client(client_id):
    clients = load_data()
    clients.pop(client_id)
    save_data(clients)
    return redirect(url_for('index'))

# Route untuk mendapatkan data client dalam format JSON
@app.route('/api/clients')
def api_clients():
    clients = load_data()
    return jsonify(clients)

if __name__ == '__main__':
    app.run(debug=True)
