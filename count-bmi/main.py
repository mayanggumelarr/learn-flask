from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        berat_badan = float(request.form["berat_badan"])
        tinggi_badan = float(request.form["tinggi_badan"])
        bmi = berat_badan/(tinggi_badan*tinggi_badan)
        print(bmi)
        return render_template("bmi.html", bmi=bmi, berat_badan=berat_badan, tinggi_badan=tinggi_badan)
    return render_template("bmi.html", bmi=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
    
