from flask import Flask
import xml.dom.minidom as minidom

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/mahasiswa')
def main():
    # gunakan fungsi parse() untuk me-load xml ke memori
    # dan melakukan parsing
    doc = minidom.parse("mahasiswa.xml")

    # Cetak isi node dan tag pertamanya
    nama = doc.getElementsByTagName("nama")[0].firstChild.data
    alamat = doc.getElementsByTagName("alamat")[0].firstChild.data
    jurusan = doc.getElementsByTagName("jurusan")[0].firstChild.data
    list_hobi = doc.getElementsByTagName("hobi")

    response = f"Nama: {nama}\nAlamat: {alamat}\nJurusan: {jurusan}\n"
    response += f"Memiliki {len(list_hobi)} hobi:\n"

    for hobi in list_hobi:
        response += f"- {hobi.getAttribute('name')}\n"

    return response  # Mengembalikan response string

if __name__ == "__main__":
    app.run()
