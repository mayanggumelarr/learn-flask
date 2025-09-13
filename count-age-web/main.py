from flask import Flask, render_template, request              # import Flask dan render templates yang isinya file2 selain py
from datetime import datetime

app = Flask(__name__)              # semua isian flask entah fungsi atau apapun

@app.route("/")                            # gerbang pakai sesuatu di flask (@app) + route adalah untuk membuka website di halaman home
def home():                                      # fungsi utama
    return render_template('home.html') #melempar variabel atau berbagai fungsi di python ke home (passing)

@app.route("/usia", methods=["GET", "POST"])             # URL bisa method GET(Tampil) dan POST(Kirim data)
def cek_usia():
    if request.method=="POST":
            tahun_lahir = int(request.form['tahun_lahir'])
            tahun_sekarang = datetime.now().year
            usia = tahun_sekarang - tahun_lahir
            print(usia)
            return render_template('usia.html', usia=usia, tahun_lahir=tahun_lahir)
    return render_template('usia.html', usia=None)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
'''

@app.route("/about")               # gerbang pakai sesuatu di flask (@app) + route adalah untuk membuka website di halaman about
def about():                                      # fungsi utama
    web_title = "Halaman About"
    return render_template('about.html', data=web_title) '''