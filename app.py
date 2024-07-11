from flask import Flask, request, render_template, redirect, jsonify, url_for, flash
import pandas as pd
import joblib
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'your_secret_key'

# Konfigurasi MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'hipertensi'

mysql = MySQL(app)

# Load model
model = joblib.load('static/model/niv.pkl')

def predict_blood_pressure(model, input_data):
    y_pred = model.predict(input_data)
    return y_pred

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/klasifikasi', methods=['GET', 'POST'])
def klasifikasi():
    if request.method == 'POST':
        try:
            # Ambil data dari form
            age = int(request.form['age'])
            Smoker = int(request.form['Smoker'])
            cigsPerDay = int(request.form['cigsPerDay'])
            BPMeds = int(request.form['BPMeds'])
            diabetes = int(request.form['diabetes'])
            totChol = int(request.form['totChol'])
            SysBP = int(request.form['SysBP'])
            DiaBP = int(request.form['DiaBP'])
            heartRate = int(request.form['heartRate'])
            BMI = float(request.form['BMI'])
            glucose = int(request.form['glucose'])

            # Buat input data frame
            input_data = {
                'age': [age],
                'Smoker': [Smoker],
                'cigsPerDay': [cigsPerDay],
                'BPMeds': [BPMeds],
                'diabetes': [diabetes],
                'totChol': [totChol],
                'SysBP': [SysBP],
                'DiaBP': [DiaBP],
                'heartRate': [heartRate],
                'BMI': [BMI],
                'glucose': [glucose]
            }
            input_df = pd.DataFrame(input_data)

            # Prediksi
            predicted_class = predict_blood_pressure(model, input_df)
            grade_id = int(predicted_class[0])

            # Ambil grade label dari database
            cursor = mysql.connection.cursor()
            query = "SELECT cgrade FROM grade WHERE id = %s"
            cursor.execute(query, (grade_id,))
            grade_label = cursor.fetchone()[0]

            # Ambil semua solusi dan saran dari database
            query_detail = "SELECT saran, solusi FROM detail WHERE grade_id = %s"
            cursor.execute(query_detail, (grade_id,))
            results = cursor.fetchall()

            saran_list = [result[0] for result in results]
            solusi_list = [result[1] for result in results]

            response = {
                'prediction': grade_id,
                'grade_label': grade_label,
                'saran': saran_list,
                'solusi': solusi_list
            }

        except Exception as e:
            response = {'error': str(e)}

        return jsonify(response)

    return render_template('index', prediction=None)

# Route untuk halaman utama
@app.route('/dashboard')
def dashboard():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM grade")
    grades = cur.fetchall()

    cur.execute("SELECT detail.id, grade.cgrade, detail.saran, detail.solusi FROM detail INNER JOIN grade ON detail.grade_id = grade.id")
    details = cur.fetchall()

    cur.close()
    return render_template('dashboard1.html', details=details, grades=grades)


# Route untuk menambahkan detail
@app.route('/add_detail', methods=['POST'])
def add_detail():
    if request.method == 'POST':
        grade_id = request.form['grade']
        saran = request.form['saran']
        solusi = request.form['solusi']
        # Lakukan insert data ke database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO detail (grade_id, saran, solusi) VALUES (%s, %s, %s)", (grade_id, saran, solusi))
        mysql.connection.commit()
        cur.close()

        flash('Data berhasil ditambahkan', 'success')
        return redirect(url_for('dashboard2'))

    return render_template('dashboard/dashboard.html')

@app.route('/edit_detail/<int:id>', methods=['POST', 'GET'])
def edit_detail(id):
    cur = mysql.connection.cursor()

    # Ambil data grade untuk dropdown
    cur.execute("SELECT * FROM grade")
    grades = cur.fetchall()

    # Ambil data detail berdasarkan id untuk ditampilkan di form edit
    cur.execute("SELECT id, grade_id, saran, solusi FROM detail WHERE id = %s", [id])
    detail = cur.fetchone()

    if request.method == 'POST':
        saran = request.form['saran']
        solusi = request.form['solusi']
        grade_id = request.form['grade']
        # Lakukan update data di database
        cur.execute("UPDATE detail SET grade_id=%s, saran=%s, solusi=%s WHERE id=%s", (grade_id, saran, solusi, id))
        mysql.connection.commit()
        cur.close()

        flash('Data berhasil diubah', 'success')
        return redirect(url_for('dashboard2'))  # Redirect ke halaman utama setelah berhasil

    cur.close()
    return render_template('dashboard/dashboard.html', detail=detail, grades=grades)  # Tampilkan form edit detail dengan opsi grade

@app.route('/delete_detail/<int:id>', methods=['POST', 'DELETE'])
def delete_detail(id):
    cur = mysql.connection.cursor()

    # Ambil data grade untuk dropdown
    cur.execute("SELECT * FROM grade")
    grades = cur.fetchall()

    # Ambil data detail berdasarkan id untuk ditampilkan di form edit
    cur.execute("SELECT id, grade_id, saran, solusi FROM detail WHERE id = %s", [id])
    detail = cur.fetchone()

    if request.method == 'POST':
        cur.execute("DELETE FROM detail WHERE id = %s", [id])
        mysql.connection.commit()
        cur.close()
        flash('Data berhasil dihapus', 'success')
        return redirect(url_for('dashboard2'))

    cur.close()
    return render_template('dashboard/dashboard.html', detail=detail, grades=grades)

@app.route('/dashboard2')
def dashboard2():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM grade")
    grades = cur.fetchall()

    cur.execute("SELECT detail.id, grade.cgrade, detail.saran, detail.solusi FROM detail INNER JOIN grade ON detail.grade_id = grade.id")
    details = cur.fetchall()

    cur.close()
    return render_template('dashboard/dashboard.html', details=details, grades=grades)

@app.route('/chart')
def chart():
    return render_template('dashboard/chart.html')

@app.route('/kontak')
def kontak():
    return render_template('contact.html')

@app.route('/artikel1')
def artikel1():
    return render_template('artikel1.html')

@app.route('/artikel2')
def artikel2():
    return render_template('artikel2.html')

@app.route('/artikel3')
def artikel3():
    return render_template('artikel3.html')

@app.route('/artikel4')
def artikel4():
    return render_template('artikel4.html')

@app.route('/artikel5')
def artikel5():
    return render_template('artikel5.html')

@app.route('/artikel6')
def artikel6():
    return render_template('artikel6.html')

if __name__ == '__main__':
    app.run(debug=True)
