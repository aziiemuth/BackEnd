from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def karyawan():
    try:
        if request.method == 'GET':
            data = [{
                'nama': 'Galih Saputra',
                'pekerjaan': 'Software Engineer',
                'usia': '30'
            }]
        elif request.method == 'POST':
            data = [{
                'nama': 'Dina Kurnia',
                'pekerjaan': 'Data Scientist',
                'usia': '28'
            }]
        elif request.method == 'PUT':
            data = [{
                'nama': 'Reza Mahendra',
                'pekerjaan': 'UI/UX Designer',
                'usia': '25'
            }]
        else:  # DELETE method
            data = [{
                'nama': 'Lina Susanti',
                'pekerjaan': 'DevOps Engineer',
                'usia': '32'
            }]
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    
    return make_response(jsonify({'data': data}), 200)

if __name__ == '__main__':
    app.run(debug=True)
