"""
Membuat API dengan FLask
"""
from flask import Flask, jsonify,render_template

app=Flask(__name__)

@app.route("/", methods=["GET"])
def halaman_utama():
    return "Halo, Selamat Datang di Halaman utama"

if __name__ == "__main__":
    app.run()