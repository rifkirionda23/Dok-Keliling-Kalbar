from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    locations = []
    with open("data/lokasi_foto.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            locations.append({
                "nama": row["Nama_Lokasi"],
                "kabupaten": row["Kabupaten"],
                "lat": float(row["lat"]),
                "lon": float(row["lon"]),
                "foto": row["foto"]
            })
    return jsonify(locations)

if __name__ == "__main__":
    app.run(debug=True)
